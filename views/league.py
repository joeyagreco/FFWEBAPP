import ast

from flask import redirect, url_for, request, render_template

from app import app
from controllers.MainController import MainController
from helpers.Error import Error
from helpers.LeagueModelNavigator import LeagueModelNavigator


@app.route("/league-homepage/<int:leagueId>", methods=["GET"])
def leagueHomepage(leagueId):
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return redirect(url_for("index", error_message=leagueOrError.errorMessage()))
    # check if this league has at least 1 week in any of its years. if not, redirect to update league page.
    for year in leagueOrError["years"]:
        # check if this is year 0
        if year != str(0):
            for week in leagueOrError["years"][year]["weeks"]:
                # check if this is year 0
                if len(week) > 1:
                    return render_template("leagueHomepage.html", league=leagueOrError)
    # no valid weeks found, send to update league page
    selectedYear = sorted(list(leagueOrError["years"].keys()))[-1]
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
    newLeagueIdOrError = mainController.addLeague(leagueName, numberOfTeams)
    if isinstance(newLeagueIdOrError, Error):
        return render_template("addLeaguePage.html", error_message=newLeagueIdOrError.errorMessage())
    else:
        return redirect(url_for("updateLeague", leagueId=newLeagueIdOrError))


@app.route("/new-league", methods=["GET"])
def newLeague():
    errorMessage = request.args.get("error_message")
    return render_template("addLeaguePage.html", error_message=errorMessage)


@app.route("/update-league/<int:leagueId>/<year>", methods=["GET", "POST"])
@app.route("/update-league/<int:leagueId>", defaults={"year": None})
def updateLeague(leagueId, year):
    # helper function to get team by id
    def getTeamNameById(teams: list, teamId: int):
        for team in teams:
            if team["teamId"] == teamId:
                return team["teamName"]

    if request.method == "GET":
        # leagueId = int(request.args.get("league_id"))
        # year = request.args.get("year")
        errorMessage = request.args.get("error_message")
        mainController = MainController()
        leagueOrError = mainController.getLeague(leagueId)
        leagueModelOrError = mainController.getLeagueModel(leagueId)
        if year is None:
            year = LeagueModelNavigator.getMostRecentYear(leagueModelOrError, asInt=True)
        year = int(year)
        if isinstance(leagueOrError, Error):
            return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
        if errorMessage:
            return render_template("updateLeaguePage.html", league=leagueOrError, selected_year=year,
                                   error_message=errorMessage)
        return render_template("updateLeaguePage.html", league=leagueOrError, selected_year=year)
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
                    return redirect(url_for("updateLeague", leagueId=leagueId, year=originalYear,
                                            error_message="Year already exists."))
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
            return redirect(
                url_for("updateLeague", league_id=leagueId, year=originalYear, error_message=updated.errorMessage()))
        else:
            # successfully updated league
            return redirect(url_for("updateLeague", leagueId=leagueId, year=yearNumber))


# TODO: use DELETE instead of GET
@app.route("/delete-league/<int:leagueId>", methods=["GET"])
def deleteLeague(leagueId):
    mainController = MainController()
    response = mainController.deleteLeague(leagueId)
    if isinstance(response, Error):
        # could not delete league
        return render_template("indexHomepage.html", error_message=response.errorMessage())
    else:
        return redirect(url_for("index"))
