import copy

from flask import redirect, url_for, request, render_template

from app import app
from controllers.MainController import MainController
from helpers.Error import Error
from helpers.LeagueModelNavigator import LeagueModelNavigator


@app.route("/add-year", methods=["GET"])
def addYear():
    leagueId = int(request.args.get("league_id"))
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    latestYear = LeagueModelNavigator.getMostRecentYear(leagueModelOrError, asInt=True)
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
    mainController.updateLeague(leagueId, leagueName, updatedYears)
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
    mainController.updateLeague(leagueId, leagueOrError["leagueName"], updatedYears)
    # TODO check for errors
    # find a year to return the user to
    redirectYear = sorted(list(updatedYears))[-1]
    return redirect(url_for("updateLeague", league_id=leagueId, year=redirectYear))
