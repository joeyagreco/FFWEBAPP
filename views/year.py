import copy

from flask import redirect, url_for, render_template

from app import app
from controllers.MainController import MainController
from helpers.LeagueModelNavigator import LeagueModelNavigator
from packages.Exceptions.DatabaseError import DatabaseError
from packages.Exceptions.LeagueNotWellFormedError import LeagueNotWellFormedError


@app.route("/add-year/<int:leagueId>", methods=["GET"])
def addYear(leagueId):
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
        leagueModel = mainController.getLeagueModel(leagueId)
    except DatabaseError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    latestYear = LeagueModelNavigator.getMostRecentYear(leagueModel, asInt=True)
    newYear = latestYear + 1
    # create new teams with names based on the owner name
    newTeams = copy.deepcopy(league["years"]["0"]["teams"])
    for team in newTeams:
        team["teamName"] += "'s Team"
    # create a new year
    yearDict = {"year": newYear, "teams": newTeams, "weeks": []}
    league["years"][str(newYear)] = yearDict
    updatedYears = league["years"]
    leagueName = league["leagueName"]
    # now update league in database
    try:
        mainController.updateLeague(leagueId, leagueName, updatedYears)
    except (DatabaseError, LeagueNotWellFormedError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return redirect(url_for("updateLeague", leagueId=leagueId, year=newYear))


# TODO: use DELETE instead of GET
@app.route("/delete-year/<int:leagueId>/<year>", methods=["GET"])
def deleteYear(leagueId, year):
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except DatabaseError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    del league["years"][year]
    updatedYears = league["years"]
    try:
        league = mainController.getLeague(leagueId)
        mainController.updateLeague(leagueId, league["leagueName"], updatedYears)
    except (DatabaseError, LeagueNotWellFormedError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    # find a year to return the user to
    redirectYear = sorted(list(updatedYears))[-1]
    return redirect(url_for("updateLeague", leagueId=leagueId, year=redirectYear))
