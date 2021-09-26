from flask import request, render_template

from app import app
from controllers.MainController import MainController
from helpers.Constants import Constants
from helpers.Error import Error
from helpers.ExplanationDivsAsStrings import ExplanationDivsAsStrings
from helpers.LeagueModelNavigator import LeagueModelNavigator


@app.route("/team-stats/<int:leagueId>/<year>", methods=["GET"])
@app.route("/team-stats/<int:leagueId>", defaults={"year": None}, methods=["GET"])
def teamStats(leagueId, year):
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    if isinstance(leagueModelOrError, Error):
        return render_template("teamStatsPage.html", league=leagueOrError,
                               error_message=leagueModelOrError.errorMessage())
    if year is None:
        year = LeagueModelNavigator.getMostRecentYear(leagueModelOrError, asInt=True)
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
    else:
        yearList = [year]
    statsModels = mainController.getTeamStatsModel(leagueModelOrError, yearList)
    return render_template("teamStatsPage.html", league=leagueOrError, stats_models=statsModels, constants=Constants,
                           selected_year=year)


@app.route("/head-to-head-stats/<int:leagueId>/<year>", methods=["GET"])
@app.route("/head-to-head-stats/<int:leagueId>", defaults={"year": None}, methods=["GET"])
def headToHeadStats(leagueId, year):
    team1Id = request.args.get("team1")
    team2Id = request.args.get("team2")
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    if isinstance(leagueModelOrError, Error):
        return render_template("headToHeadStatsPage.html", league=leagueOrError, given_team_1_id=None,
                               given_team_2_id=None, error_message=leagueModelOrError.errorMessage())
    if year is None:
        year = LeagueModelNavigator.getMostRecentYear(leagueModelOrError, asInt=True)
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
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
        for i in range(2, leagueModelOrError.getNumberOfTeams()):
            if LeagueModelNavigator.teamsPlayEachOther(leagueModelOrError, yearList, team1Id, i):
                team2Id = i
                break
    # check if these teams/owners have played each other ever
    for y in yearList:
        # these teams/owners have played each other
        if LeagueModelNavigator.teamsPlayEachOther(leagueModelOrError, [y], team1Id, team2Id):
            # get the stats model
            statsModelsOrError = mainController.getHeadToHeadStatsModel(leagueModelOrError, yearList, team1Id, team2Id)
            return render_template("headToHeadStatsPage.html", league=leagueOrError, given_team_1_id=team1Id,
                                   given_team_2_id=team2Id, stats_models=statsModelsOrError, constants=Constants,
                                   selected_year=year)
        # these teams/owners have never faced each other
        # create an error message
        message = f"These teams did not face each other in {year}."
        if year == '0':
            message = "These owners have not faced each other ever."
        return render_template("headToHeadStatsPage.html", league=leagueOrError, given_team_1_id=team1Id,
                               given_team_2_id=team2Id, selected_year=year, error_message=message)


@app.route("/league-stats/<int:leagueId>/<year>", methods=["GET"])
@app.route("/league-stats/<int:leagueId>", defaults={"year": None}, methods=["GET"])
def leagueStats(leagueId, year):
    statSelection = request.args.get("stat_selection")
    statOptions = Constants.LEAGUE_STATS_STAT_TITLES
    if statSelection is None:
        statSelection = statOptions[0]
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    if year is None:
        # give most recent year if none is given
        years = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
        year = years[-1]
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
    else:
        yearList = [year]
    statsModelOrError = mainController.getLeagueStatsModel(leagueModelOrError, yearList, statSelection)
    return render_template("leagueStatsPage.html", league=leagueOrError, stat_options=statOptions,
                           selected_stat=statSelection, stats_models=statsModelOrError, selected_year=year,
                           constants=Constants)


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
    leagueOrError = mainController.getLeague(leagueId)
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    if year is None:
        # give most recent year if none is given
        years = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
        year = years[-1]
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
    else:
        yearList = [year]
    divAsString = mainController.getGraphDiv(leagueModelOrError, yearList, screenWidth, selectedGraph)
    graphOptions = Constants.GRAPH_OPTIONS
    return render_template("graphsPage.html", league=leagueOrError, graph_options=graphOptions,
                           selected_graph=selectedGraph, graph_div=divAsString, selected_year=year)


@app.route("/stats-explained/<int:leagueId>", methods=["GET"])
def statsExplained(leagueId):
    selectedStat = request.args.get("selected_stat")
    statList = sorted(Constants.ALL_STAT_TITLES)
    # set default stat selection if none given
    if not selectedStat:
        selectedStat = statList[0]
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    statInfo = ExplanationDivsAsStrings.retrieveStatList(selectedStat)
    return render_template("statsBase.html",
                           league=leagueOrError,
                           stat_list=statList,
                           selected_stat=selectedStat,
                           purpose_div=statInfo[0],
                           formula_div=statInfo[1],
                           formula_explained_div=statInfo[2])


@app.route("/test", methods=["GET"])
def test():
    leagueId = 746608
    statOptions = Constants.LEAGUE_STATS_STAT_TITLES
    statSelection = statOptions[0]
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    # give most recent year if none is given
    years = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
    year = years[-1]
    yearList = [year]
    statsModelOrError = mainController.getLeagueStatsModel(leagueModelOrError, yearList, statSelection)
    return render_template("league_stats/leagueStatsBase.html", league=leagueOrError, stat_options=statOptions,
                           selected_stat=statSelection, stats_models=statsModelOrError, selected_year=year,
                           constants=Constants)
