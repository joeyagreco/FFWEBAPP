from flask import request, render_template

from app import app
from controllers.MainController import MainController
from helpers.Constants import Constants
from helpers.ExplanationDivsAsStrings import ExplanationDivsAsStrings
from helpers.LeagueModelNavigator import LeagueModelNavigator
from packages.Exceptions.DatabaseError import DatabaseError
from packages.Exceptions.InvalidStatSelectionError import InvalidStatSelectionError
from packages.Exceptions.LeagueNotFoundError import LeagueNotFoundError


@app.route("/team-stats/<int:leagueId>/<year>", methods=["GET"])
@app.route("/team-stats/<int:leagueId>", defaults={"year": None}, methods=["GET"])
def teamStats(leagueId, year):
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except LeagueNotFoundError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    try:
        leagueModel = mainController.getLeagueModel(leagueId)
    except DatabaseError as e:
        return render_template("teamStatsPage.html", league=league,
                               error_message=str(e))
    if year is None:
        year = LeagueModelNavigator.getMostRecentYear(leagueModel, asInt=True)
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModel, asInts=True))
    else:
        yearList = [year]
    statsModels = mainController.getTeamStatsModel(leagueModel, yearList)
    return render_template("teamStatsPage.html", league=league, stats_models=statsModels, constants=Constants,
                           selected_year=year)


@app.route("/head-to-head-stats/<int:leagueId>/<year>", methods=["GET"])
@app.route("/head-to-head-stats/<int:leagueId>", defaults={"year": None}, methods=["GET"])
def headToHeadStats(leagueId, year):
    team1Id = request.args.get("team1")
    team2Id = request.args.get("team2")
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except LeagueNotFoundError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    try:
        leagueModel = mainController.getLeagueModel(leagueId)
    except DatabaseError as e:
        return render_template("headToHeadStatsPage.html", league=league, given_team_1_id=None,
                               given_team_2_id=None, error_message=str(e))
    if year is None:
        year = LeagueModelNavigator.getMostRecentYear(leagueModel, asInt=True)
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModel, asInts=True))
    else:
        yearList = [year]
    if team1Id and team2Id:
        # if the user submitted this matchup
        team1Id = int(team1Id)
        team2Id = int(team2Id)
    else:
        # no submitted matchup, default to first 2 teams
        team1Id = 1
        team2Id = 2
        for i in range(2, leagueModel.getNumberOfTeams()):
            if LeagueModelNavigator.teamsPlayEachOther(leagueModel, yearList, team1Id, i):
                team2Id = i
                break
    # check if these teams/owners have played each other ever
    for y in yearList:
        # these teams/owners have played each other
        if LeagueModelNavigator.teamsPlayEachOther(leagueModel, [y], team1Id, team2Id):
            # get the stats model
            statsModelsOrError = mainController.getHeadToHeadStatsModel(leagueModel, yearList, team1Id, team2Id)
            return render_template("headToHeadStatsPage.html", league=league, given_team_1_id=team1Id,
                                   given_team_2_id=team2Id, stats_models=statsModelsOrError, constants=Constants,
                                   selected_year=year)
        # these teams/owners have never faced each other
        # create an error message
        message = f"These teams did not face each other in {year}."
        if year == '0':
            message = "These owners have not faced each other ever."
        return render_template("headToHeadStatsPage.html", league=league, given_team_1_id=team1Id,
                               given_team_2_id=team2Id, selected_year=year, error_message=message)


@app.route("/graphs/<int:leagueId>/<year>", methods=["GET"])
@app.route("/graphs/<int:leagueId>", defaults={"year": None}, methods=["GET"])
def graphs(leagueId, year):
    selectedGraph = request.args.get("graph_selection")
    # default selected graph
    if not selectedGraph:
        selectedGraph = Constants.GRAPH_OPTIONS[0]
    screenWidth = request.args.get("screen_width")
    if screenWidth:
        screenWidth = float(screenWidth)
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
        leagueModel = mainController.getLeagueModel(leagueId)
    except (DatabaseError, LeagueNotFoundError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    if year is None:
        # give most recent year if none is given
        years = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModel, asInts=True))
        year = years[-1]
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModel, asInts=True))
    else:
        yearList = [year]
    try:
        divAsString = mainController.getGraphDiv(leagueModel, yearList, screenWidth, selectedGraph)
    except InvalidStatSelectionError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    graphOptions = Constants.GRAPH_OPTIONS
    return render_template("graphsPage.html", league=league, graph_options=graphOptions,
                           selected_graph=selectedGraph, graph_div=divAsString, selected_year=year)


@app.route("/stats-explained/<int:leagueId>", methods=["GET"])
def statsExplained(leagueId):
    selectedStat = request.args.get("selected_stat")
    statList = sorted(Constants.ALL_STAT_TITLES)
    # set default stat selection if none given
    if not selectedStat:
        selectedStat = statList[0]
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except LeagueNotFoundError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    statInfo = ExplanationDivsAsStrings.retrieveStatList(selectedStat)
    return render_template("statsBase.html",
                           league=league,
                           stat_list=statList,
                           selected_stat=selectedStat,
                           purpose_div=statInfo[0],
                           formula_div=statInfo[1],
                           formula_explained_div=statInfo[2])
