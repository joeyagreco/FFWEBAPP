import ast

from flask import redirect, url_for, request, render_template

from app import app
from controllers.MainController import MainController
from helpers.Error import Error
from helpers.LeagueModelNavigator import LeagueModelNavigator
from packages.Exceptions.DatabaseError import DatabaseError


@app.route("/league-homepage/<int:leagueId>", methods=["GET"])
def leagueHomepage(leagueId):
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except DatabaseError as e:
        return redirect(url_for("index", error_message=str(e)))
    # check if this league has at least 1 week in any of its years. if not, redirect to update league page.
    for year in league["years"]:
        # check if this is year 0
        if year != str(0):
            for week in league["years"][year]["weeks"]:
                # check if this is year 0
                if len(week) > 1:
                    return render_template("leagueHomepage.html", league=league)
    # no valid weeks found, send to update league page
    selectedYear = sorted(list(league["years"].keys()))[-1]
    return redirect(url_for("updateLeague", leagueId=leagueId, year=selectedYear))


@app.route("/add-league", methods=["POST"])
def addLeague():
    # convert the POST request headers into a python dictionary
    newDataStr = request.data.decode("UTF-8")
    newDataDict = ast.literal_eval(newDataStr)
    # retrieve the values from our dictionary
    leagueName = newDataDict["league_name"]
    numberOfTeams = int(newDataDict["number_of_teams"])
    mainController = MainController()
    try:
        newLeagueId = mainController.addLeague(leagueName, numberOfTeams)
    except DatabaseError as e:
        return render_template("addLeaguePage.html", error_message=str(e))
    return redirect(url_for("updateLeague", leagueId=newLeagueId))


@app.route("/new-league", methods=["GET"])
def newLeague():
    errorMessage = request.args.get("error_message")
    return render_template("addLeaguePage.html", error_message=errorMessage)


@app.route("/update-league/<int:leagueId>/<year>", methods=["GET", "POST"])
@app.route("/update-league/<int:leagueId>", defaults={"year": None}, methods=["GET", "POST"])
def updateLeague(leagueId, year):
    # helper function to get team by id
    def getTeamNameById(teams: list, teamId: int):
        for team in teams:
            if team["teamId"] == teamId:
                return team["teamName"]

    if request.method == "GET":
        errorMessage = request.args.get("error_message")
        mainController = MainController()
        try:
            league = mainController.getLeague(leagueId)
            leagueModel = mainController.getLeagueModel(leagueId)
        except DatabaseError as e:
            return render_template("indexHomepage.html", error_message=str(e))
        if year is None:
            year = LeagueModelNavigator.getMostRecentYear(leagueModel, asInt=True)
        if errorMessage:
            return render_template("updateLeaguePage.html", league=league, selected_year=year,
                                   error_message=errorMessage)
        return render_template("updateLeaguePage.html", league=league, selected_year=year)
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
        try:
            league = mainController.getLeague(leagueId)
        except DatabaseError as e:
            return render_template("indexHomepage.html", error_message=str(e))
        # check if user updated the year and if they updated the year to be one that already exists
        # if so, return an error message
        if yearNumber != originalYear:
            # user updated year number
            for year in league["years"].keys():
                if year == yearNumber:
                    # user chose a year that is already in league
                    return redirect(url_for("updateLeague", leagueId=leagueId, year=originalYear,
                                            error_message="Year already exists."))
        # update team names
        teams = []
        for teamId in range(1, numberOfTeams + 1):
            teams.append({"teamId": int(teamId), "teamName": newDataDict[f"team_{teamId}"]})
        if isinstance(league, Error):
            # could not find league
            return redirect(url_for("index", error_message=league.errorMessage()))
        years = league["years"]
        currentYear = years[originalYear]
        currentYear["year"] = int(yearNumber)
        currentYear["teams"] = teams
        # check it its year 0
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
        try:
            mainController.updateLeague(leagueId, leagueName, years)
        except DatabaseError as e:
            return redirect(
                url_for("updateLeague", leagueId=leagueId, year=originalYear, error_message=str(e)))
        # successfully updated league
        return redirect(url_for("updateLeague", leagueId=leagueId, year=yearNumber))


# TODO: use DELETE instead of GET
@app.route("/delete-league/<int:leagueId>", methods=["GET"])
def deleteLeague(leagueId):
    mainController = MainController()
    try:
        mainController.deleteLeague(leagueId)
    except DatabaseError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return redirect(url_for("index"))
