import os

from flask import Flask, render_template, request, redirect, url_for
from controllers.MainController import MainController
from fixtures.LeagueModelFixtureGeneratorDict import LeagueModelFixtureGeneratorDict
from helpers.Error import Error

app = Flask(__name__)


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
        return render_template("indexHomepage.html", errorMessage=leagueOrError.errorMessage())
    else:
        leagueUrl = f"{os.getenv('SERVER_BASE_URL')}leaguehomepage?league_id={leagueId}"
        return render_template("leagueHomepage.html", league=leagueOrError, league_url=leagueUrl)


@app.route("/updateleague", methods=["GET", "POST"])
def updateLeague():
    if request.method == "GET":
        leagueId = int(request.args.get("league_id"))
        mainController = MainController()
        leagueOrError = mainController.getLeague(leagueId)
        if isinstance(leagueOrError, Error):
            return render_template("indexHomepage.html", errorMessage=leagueOrError.errorMessage())
        else:
            return render_template("updateLeaguePage.html", league=leagueOrError)
    elif request.method == "POST":
        leagueId = int(request.form["league_id"])
        leagueName = request.form["league_name"]
        numberOfTeams = int(request.form["number_of_teams"])
        teams = []
        for teamId in range(1, numberOfTeams + 1):
            teams.append({"teamId": int(teamId), "teamName": request.form[f"team_{teamId}"]})
        mainController = MainController()
        updated = mainController.updateLeague(leagueId, leagueName, teams)
        leagueOrError = mainController.getLeague(leagueId)
        if isinstance(updated, Error):
            if isinstance(leagueOrError, Error):
                # could not update league or find league
                return render_template("indexHomepage.html", errorMessage=leagueOrError.errorMessage())
            else:
                # could not update league
                return render_template("updateLeaguePage.html", error=leagueOrError)
        else:
            return render_template("updateLeaguePage.html", league=leagueOrError)
    else:
        return render_template("updateLeaguePage.html", error_message="ERROR: Not getting a GET or POST.")


if __name__ == "__main__":
    app.run(debug=True)
