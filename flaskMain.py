import os

from flask import Flask, render_template, request, redirect, url_for
from controllers.MainController import MainController
from fixtures.LeagueModelFixtureGeneratorDict import LeagueModelFixtureGeneratorDict
from helpers.Error import Error

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    """
    This is for the browser icon.
    """
    return redirect(url_for('static', filename='icons/football_icon.ico'))


@app.route("/")
def index():
    return render_template("indexHomepage.html")


@app.route("/addleague", methods=["POST"])
def addLeague():
    if request.method == "POST":
        leagueName = request.form["league_name"]
        numberOfTeams = int(request.form["number_of_teams"])
        teams = []
        for x in range(1, numberOfTeams + 1):
            teams.append({"teamId": x, "teamName": ""})
        mainController = MainController()
        newLeagueOrError = mainController.addLeague(leagueName, numberOfTeams, teams)
        if isinstance(newLeagueOrError, Error):
            return render_template("addLeaguePage.html", error_message=newLeagueOrError.errorMessage())
        else:
            return redirect(url_for("leagueHomepage", league_id=int(newLeagueOrError.inserted_id)))
    else:
        return render_template("addLeaguePage.html", error_message="ERROR: Not getting a POST.")


@app.route("/newleague")
def newLeague():
    return render_template("addLeaguePage.html")


@app.route("/leaguehomepage", methods=["GET"])
def leagueHomepage():
    leagueId = int(request.args.get("league_id"))
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    else:
        leagueUrl = f"{os.getenv('SERVER_BASE_URL')}leaguehomepage?league_id={leagueId}"
        return render_template("leagueHomepage.html", league=leagueOrError, league_url=leagueUrl)


@app.route("/updateleague", methods=["GET", "POST"])
def updateLeague():
    if request.method == "GET":
        print("in get update league")
        leagueId = int(request.args.get("league_id"))
        mainController = MainController()
        leagueOrError = mainController.getLeague(leagueId)
        if isinstance(leagueOrError, Error):
            return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
        else:
            return render_template("updateLeaguePage.html", league=leagueOrError)
    elif request.method == "POST":
        print("posting in update league")
        leagueId = int(request.form["league_id"])
        leagueName = request.form["league_name"]
        numberOfTeams = int(request.form["number_of_teams"])
        teams = []
        for teamId in range(1, numberOfTeams + 1):
            teams.append({"teamId": int(teamId), "teamName": request.form[f"team_{teamId}"]})
        mainController = MainController()
        updated = mainController.updateLeague(leagueId, leagueName, teams)
        leagueOrError = mainController.getLeague(leagueId)
        if isinstance(leagueOrError, Error):
            # could not find league
            return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
        elif isinstance(updated, Error):
            # could not update league
            return render_template("updateLeaguePage.html", league=leagueOrError, error_message=updated.errorMessage())
        else:
            # successfully updated league
            return render_template("updateLeaguePage.html", league=leagueOrError, updated=True)
    else:
        return render_template("indexHomepage.html", error_message="ERROR: Not getting a GET or POST.")


@app.route("/deleteleague", methods=["GET"])
def deleteLeague():
    leagueId = int(request.args.get("league_id"))
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
