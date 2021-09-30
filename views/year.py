import copy

from flask import redirect, url_for, render_template

from app import app
from controllers.MainController import MainController
from helpers.Error import Error
from helpers.LeagueModelNavigator import LeagueModelNavigator


@app.route("/add-year/<int:leagueId>", methods=["GET"])
def addYear(leagueId):
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
    return redirect(url_for("updateLeague", leagueId=leagueId, year=newYear))


# TODO: use DELETE instead of GET
@app.route("/delete-year/<int:leagueId>/<year>", methods=["GET"])
def deleteYear(leagueId, year):
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    del leagueOrError["years"][year]
    updatedYears = leagueOrError["years"]
    leagueOrError = mainController.getLeague(leagueId)
    mainController.updateLeague(leagueId, leagueOrError["leagueName"], updatedYears)
    # TODO check for errors
    # find a year to return the user to
    redirectYear = sorted(list(updatedYears))[-1]
    return redirect(url_for("updateLeague", leagueId=leagueId, year=redirectYear))
