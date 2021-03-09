import copy
import os
import ast

from flask import Flask, render_template, request, redirect, url_for

from controllers.MainController import MainController
from helpers.Constants import Constants
from helpers.Error import Error
from helpers.ExplanationDivsAsStrings import ExplanationDivsAsStrings
from helpers.LeagueModelNavigator import LeagueModelNavigator

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    """
    This is for the browser icon.
    """
    return redirect(url_for('static', filename='icons/football_icon.ico'))


@app.route("/")
def index():
    errorMessage = request.args.get("error_message")
    return render_template("indexHomepage.html", error_message=errorMessage)


@app.route("/add-league", methods=["POST"])
def addLeague():
    # convert the POST request headers into a python dictionary
    newDataStr = request.data.decode("UTF-8")
    newDataDict = ast.literal_eval(newDataStr)
    # retrieve the values from our dictionary
    leagueName = newDataDict["league_name"]
    numberOfTeams = int(newDataDict["number_of_teams"])
    mainController = MainController()
    newLeagueIdOrError = mainController.addLeague(leagueName, numberOfTeams)
    if isinstance(newLeagueIdOrError, Error):
        return render_template("addLeaguePage.html", error_message=newLeagueIdOrError.errorMessage())
    else:
        return redirect(url_for("updateLeague", league_id=newLeagueIdOrError))


@app.route("/new-league", methods=["GET"])
def newLeague():
    errorMessage = request.args.get("error_message")
    return render_template("addLeaguePage.html", error_message=errorMessage)


@app.route("/league-homepage", methods=["GET"])
def leagueHomepage():
    leagueId = int(request.args.get("league_id"))
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return redirect(url_for("index", error_message=leagueOrError.errorMessage()))
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    # check if this league has at least 1 week in any of its years. if not, redirect to update league page.
    for year in leagueOrError["years"]:
        # check if this is year 0
        # TODO make a LMN method to check for year 0
        if year != str(0):
            for week in leagueOrError["years"][year]["weeks"]:
                # TODO make LMN method maybe
                # check if this is year 0
                if len(week) > 1:
                    leagueUrl = f"{os.getenv('SERVER_BASE_URL')}league-homepage?league_id={leagueId}"
                    return render_template("leagueHomepage.html", league=leagueOrError, league_url=leagueUrl)
    # no valid weeks found, send to update league page
    selectedYear = sorted(list(leagueOrError["years"].keys()))[-1]
    return redirect(url_for("updateLeague", league_id=leagueId, year=selectedYear))


@app.route("/update-league", methods=["GET", "POST"])
def updateLeague():
    # helper function to get team by id
    def getTeamNameById(teams: list, teamId: int):
        for team in teams:
            if team["teamId"] == teamId:
                return team["teamName"]

    if request.method == "GET":
        leagueId = int(request.args.get("league_id"))
        selectedYear = request.args.get("year")
        errorMessage = request.args.get("error_message")
        mainController = MainController()
        leagueOrError = mainController.getLeague(leagueId)
        # TODO LMN method to get "default" (probably highest) year from league
        if not selectedYear:
            selectedYear = list(sorted(leagueOrError["years"].keys()))[-1]
        selectedYear = int(selectedYear)
        if isinstance(leagueOrError, Error):
            return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
        if errorMessage:
            return render_template("updateLeaguePage.html", league=leagueOrError, selected_year=selectedYear, error_message=errorMessage)
        return render_template("updateLeaguePage.html", league=leagueOrError, selected_year=selectedYear)
    else:
        # we got a POST
        # convert headers
        newDataStr = request.data.decode("UTF-8")
        newDataDict = ast.literal_eval(newDataStr)
        leagueId = int(newDataDict["league_id"])
        # update league name
        leagueName = newDataDict["league_name"]
        # update the given year
        yearNumber = newDataDict["year_number"]
        # get original year
        originalYear = newDataDict["original_year_number"]
        # number of teams cant be changed by the user, but we send it into our request
        numberOfTeams = int(newDataDict["number_of_teams"])
        mainController = MainController()
        leagueOrError = mainController.getLeague(leagueId)
        # check if user updated the year and if they updated the year to be one that already exists
        # if so, return an error message
        if yearNumber != originalYear:
            # user updated year number
            for year in leagueOrError["years"].keys():
                if year == yearNumber:
                    # user chose a year that is already in league
                    return redirect(url_for("updateLeague", league_id=leagueId, year=originalYear, error_message="Year already exists."))
        # update team names
        teams = []
        for teamId in range(1, numberOfTeams + 1):
            teams.append({"teamId": int(teamId), "teamName": newDataDict[f"team_{teamId}"]})
        if isinstance(leagueOrError, Error):
            # could not find league
            return redirect(url_for("index", error_message=leagueOrError.errorMessage()))
        years = leagueOrError["years"]
        currentYear = years[originalYear]
        currentYear["year"] = int(yearNumber)
        currentYear["teams"] = teams
        # check it its year 0
        # TODO LMN method for this
        if currentYear["year"] != 0:
            for week in currentYear["weeks"]:
                for matchup in week["matchups"]:
                    matchup["teamA"]["teamName"] = getTeamNameById(teams, matchup["teamA"]["teamId"])
                    matchup["teamB"]["teamName"] = getTeamNameById(teams, matchup["teamB"]["teamId"])
        # copy year
        newYear = currentYear
        # remove old year and put new one in
        del years[originalYear]
        years[yearNumber] = newYear
        # now update league in database
        updated = mainController.updateLeague(leagueId, leagueName, years)
        leagueOrError = mainController.getLeague(leagueId)
        if isinstance(leagueOrError, Error):
            # could not find league
            return redirect(url_for("index", error_message=leagueOrError.errorMessage()))
        elif isinstance(updated, Error):
            # could not update league
            return redirect(url_for("updateLeague", league_id=leagueId, year=originalYear, error_message=updated.errorMessage()))
        else:
            # successfully updated league
            return redirect(url_for("updateLeague", league_id=leagueId, year=yearNumber))


@app.route("/delete-league", methods=["GET"])
def deleteLeague():
    leagueId = int(request.args.get("league_id"))
    mainController = MainController()
    response = mainController.deleteLeague(leagueId)
    if isinstance(response, Error):
        # could not delete league
        return render_template("indexHomepage.html", error_message=response.errorMessage())
    else:
        return redirect(url_for("index"))


@app.route("/add-update-weeks", methods=["GET"])
def addUpdateWeeks():
    leagueId = int(request.args.get("league_id"))
    year = request.args.get("year")
    week = request.args.get("week")
    errorMessage = request.args.get("error_message")
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        # could not load league
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    else:
        if week:
            # if we got a week passed in, render the page with that week displayed
            week = int(week)
            return render_template("addUpdateWeeksPage.html", league=leagueOrError, selected_year=year, week_number=week, error_message=errorMessage)
        else:
            yearDict = leagueOrError["years"][str(year)]
            if len(yearDict["weeks"]) == 0:
                # no weeks added yet, add an empty week
                weekDict = {"weekNumber": 1, "matchups": []}
                matchupIdCounter = 1
                for i in range(1, len(yearDict["teams"]), 2):
                    matchup = {"matchupId": matchupIdCounter,
                               "teamA": yearDict["teams"][i - 1],
                               "teamB": yearDict["teams"][i],
                               "teamAScore": None,
                               "teamBScore": None}
                    matchupIdCounter += 1
                    weekDict["matchups"].append(matchup)
                yearDict["weeks"].append(weekDict)
                leagueOrError["years"][str(year)] = yearDict
                return render_template("addUpdateWeeksPage.html", league=leagueOrError, selected_year=year, week_number=1, error_message=errorMessage)
            else:
                # default to last (most recent) week in this league
                week = len(yearDict["weeks"])
                return render_template("addUpdateWeeksPage.html", league=leagueOrError, selected_year=year, week_number=week, error_message=errorMessage)


@app.route("/add-year", methods=["GET"])
def addYear():
    leagueId = int(request.args.get("league_id"))
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    # TODO LMN method to get the highest number year in the league
    latestYear = int(max(list(leagueOrError["years"].keys())))
    newYear = latestYear + 1
    # create new teams with names based on the owner name
    newTeams = copy.deepcopy(leagueOrError["years"]["0"]["teams"])
    for team in newTeams:
        team["teamName"] += "'s Team"
    # create a new year
    yearDict = {"year": newYear, "teams": newTeams, "weeks": []}
    leagueOrError["years"][str(newYear)] = yearDict
    updatedYears = leagueOrError["years"]
    leagueName = leagueOrError["leagueName"]
    # now update league in database
    updated = mainController.updateLeague(leagueId, leagueName, updatedYears)
    # TODO check for errors
    return redirect(url_for("updateLeague", league_id=leagueId, year=newYear))


@app.route("/delete-year", methods=["GET"])
def deleteYear():
    leagueId = int(request.args.get("league_id"))
    selectedYear = request.args.get("selected_year")
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    del leagueOrError["years"][selectedYear]
    updatedYears = leagueOrError["years"]
    leagueOrError = mainController.getLeague(leagueId)
    updated = mainController.updateLeague(leagueId, leagueOrError["leagueName"], updatedYears)
    # TODO check for errors
    # find a year to return the user to
    redirectYear = sorted(list(updatedYears))[-1]
    return redirect(url_for("updateLeague", league_id=leagueId, year=redirectYear))


@app.route("/update-week", methods=["POST"])
def updateWeek():
    # helper function to get team by id
    def getTeamById(league: dict, teamId: int, year: int):
        for team in league["years"][year]["teams"]:
            if team["teamId"] == teamId:
                return team

    # helper function to check if week exists in league
    def weekExists(league: dict, weekNum: int, year: int):
        for week in league["years"][year]["weeks"]:
            if week["weekNumber"] == weekNum:
                return True
        return False

    # convert dict
    newDataStr = request.data.decode("UTF-8")
    newDataDict = ast.literal_eval(newDataStr)
    leagueId = int(newDataDict["league_id"])
    weekNumber = int(newDataDict["week_number"])
    yearNumber = newDataDict["year_number"]
    weekDict = {"weekNumber": weekNumber, "matchups": []}
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)

    if isinstance(leagueOrError, Error):
        return redirect(url_for('index', error_message=leagueOrError.errorMessage()))
    else:
        matchupIdCounter = 1
        for i in range(1, len(leagueOrError["years"][yearNumber]["teams"]), 2):
            matchup = {"matchupId": matchupIdCounter,
                       "teamA": getTeamById(leagueOrError, int(newDataDict[f"teamAId_matchup_{matchupIdCounter}"]),
                                            yearNumber),
                       "teamB": getTeamById(leagueOrError, int(newDataDict[f"teamBId_matchup_{matchupIdCounter}"]),
                                            yearNumber),
                       "teamAScore": float(newDataDict[f"teamAScore_matchup_{matchupIdCounter}"]),
                       "teamBScore": float(newDataDict[f"teamBScore_matchup_{matchupIdCounter}"])}
            weekDict["matchups"].append(matchup)
            matchupIdCounter += 1
        # check if this league has this week already, if so, overwrite it, if not, add it
        if weekExists(leagueOrError, weekNumber, yearNumber):
            # overwrite week
            leagueOrError["years"][yearNumber]["weeks"][weekNumber - 1] = weekDict
        else:
            # add week
            leagueOrError["years"][yearNumber]["weeks"].append(weekDict)

        # update league in database
        response = mainController.updateLeague(leagueOrError["_id"],
                                               leagueOrError["leagueName"],
                                               leagueOrError["years"])
        if isinstance(response, Error):
            # could not update week
            return redirect(url_for("addUpdateWeeks", league_id=leagueId, week=weekNumber, year=yearNumber, error_message=response.errorMessage()))
        newLeagueOrError = mainController.getLeague(leagueId)
        if isinstance(newLeagueOrError, Error):
            return redirect(url_for('index', error_message=newLeagueOrError.errorMessage()))
        else:
            return redirect(url_for('addUpdateWeeks', league_id=leagueOrError["_id"], week=weekNumber, year=yearNumber))


@app.route("/add-week", methods=["GET"])
def addWeek():
    leagueId = int(request.args.get("league_id"))
    yearNumber = request.args.get("year_number")
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    weekNumber = len(leagueOrError["years"][yearNumber]["weeks"]) + 1
    # add an empty week
    weekDict = {"weekNumber": weekNumber, "matchups": []}
    matchupIdCounter = 1
    for i in range(1, len(leagueOrError["years"][yearNumber]["teams"]), 2):
        matchup = {"matchupId": matchupIdCounter,
                   "teamA": leagueOrError["years"][yearNumber]["teams"][i - 1],
                   "teamB": leagueOrError["years"][yearNumber]["teams"][i],
                   "teamAScore": None,
                   "teamBScore": None}
        matchupIdCounter += 1
        weekDict["matchups"].append(matchup)
    leagueOrError["years"][yearNumber]["weeks"].append(weekDict)
    return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=weekNumber, selected_year=yearNumber)


@app.route("/delete-week", methods=["GET"])
def deleteWeek():
    leagueId = int(request.args.get("league_id"))
    week = int(request.args.get("week"))
    year = request.args.get("year")
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        # couldn't get league from database
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    # don't allow user to delete week 1
    if week == 1:
        error = Error("Week 1 cannot be deleted.")
        # check if week 1 already existed
        if len(leagueOrError["years"][year]["weeks"]) == 0:
            # week 1 didn't exist
            return redirect(url_for('addUpdateWeeks', league_id=leagueOrError["_id"], year=year))
        else:
            # week 1 exists
            return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=week, selected_year=year, error_message=error.errorMessage())
    # returnWeek is where the user is returned if the week is ineligible for deletion
    returnWeek = len(leagueOrError["years"][year]["weeks"])
    if week == len(leagueOrError["years"][year]["weeks"]):
        # if this is the last week added [most recent week]
        leagueOrError = mainController.deleteWeek(leagueId, int(year))
        if isinstance(leagueOrError, Error):
            # couldn't delete week
            return redirect(url_for('index'))
        else:
            # successfully deleted week
            return redirect(url_for('addUpdateWeeks', league_id=leagueOrError["_id"], year=year))
    else:
        # determine if this is an unsaved, added week that is being deleted OR a non-last week
        if week > returnWeek:
            return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=returnWeek, selected_year=year)
        else:
            error = Error("Only the most recent week can be deleted.")
            return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=returnWeek, selected_year=year, error_message=error.errorMessage())


@app.route("/team-stats", methods=["GET"])
def teamStats():
    leagueId = int(request.args.get("league_id"))
    year = request.args.get("year")
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    if isinstance(leagueModelOrError, Error):
        return render_template("teamStatsPage.html", league=leagueOrError,
                               error_message=leagueModelOrError.errorMessage())
    if year is None:
        # give most recent year if none is given
        years = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
        year = years[-1]
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
        year = 0
    else:
        yearList = [year]
    statsModels = mainController.getTeamStatsModel(leagueModelOrError, yearList)
    # grab Constants class to use for titles of table
    constants = Constants
    return render_template("teamStatsPage.html", league=leagueOrError, stats_models=statsModels, constants=constants, selected_year=year)


@app.route("/head-to-head-stats", methods=["GET"])
def headToHeadStats():
    leagueId = int(request.args.get("league_id"))
    team1Id = request.args.get("team1")
    team2Id = request.args.get("team2")
    year = request.args.get("year")
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    if isinstance(leagueModelOrError, Error):
        return render_template("headToHeadStatsPage.html", league=leagueOrError, given_team_1_id=None,
                               given_team_2_id=None, error_message=leagueModelOrError.errorMessage())
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
    if team1Id and team2Id:
        # if the user submitted this matchup
        team1Id = int(team1Id)
        team2Id = int(team2Id)
    else:
        # no submitted matchup, default to first 2 teams
        team1Id = 1
        team2Id = 2
        for i in range(2, leagueModelOrError.getNumberOfTeams()):
            if LeagueModelNavigator.teamsPlayEachOther(leagueModelOrError, year, team1Id, i):
                team2Id = i
                break
    # check if these teams play each other ever
    for y in yearList:
        if not LeagueModelNavigator.teamsPlayEachOther(leagueModelOrError, y, team1Id, team2Id):
            # create an error message
            message = f"These teams did not face each other in {year}."
            if year == '0':
                message = "These owners have not faced each other ever."
            return render_template("headToHeadStatsPage.html", league=leagueOrError, given_team_1_id=team1Id, given_team_2_id=team2Id, selected_year=year, error_message=message)
    # get the stats model
    statsModelsOrError = mainController.getHeadToHeadStatsModel(leagueModelOrError, yearList, team1Id, team2Id)
    # grab Constants class to use for dropdown
    constants = Constants
    return render_template("headToHeadStatsPage.html", league=leagueOrError, given_team_1_id=team1Id,
                           given_team_2_id=team2Id, stats_models=statsModelsOrError, constants=constants, selected_year=year)


@app.route("/league-stats", methods=["GET"])
def leagueStats():
    leagueId = int(request.args.get("league_id"))
    statSelection = request.args.get("stat_selection")
    year = request.args.get("year")
    statOptions = Constants.LEAGUE_STATS_STAT_TITLES
    if not statSelection:
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
    # grab Constants class to use for titles of table
    constants = Constants
    return render_template("leagueStatsPage.html", league=leagueOrError, stat_options=statOptions,
                           selected_stat=statSelection, stats_models=statsModelOrError, selected_year=year, constants=constants)


@app.route("/graphs", methods=["GET"])
def graphs():
    leagueId = int(request.args.get("league_id"))
    selectedGraph = request.args.get("graph_selection")
    year = request.args.get("year")
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


@app.route("/stats-explained", methods=["GET"])
def statsExplained():
    leagueId = int(request.args.get("league_id"))
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

@app.route("/about", methods=["GET"])
def about():
    leagueId = int(request.args.get("league_id"))
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    return render_template("aboutPage.html", league=leagueOrError)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=80)
