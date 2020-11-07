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
        numberOfTeams = request.form["number_of_teams"]
        mainController = MainController()
        newLeagueOrError = mainController.addLeague(leagueName, numberOfTeams)
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
    leagueId = request.args.get("league_id")
    mainController = MainController()
    leagueOrError = mainController.getLeague(int(leagueId))
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", errorMessage=leagueOrError.errorMessage())
    else:
        leagueUrl = f"{os.getenv('SERVER_BASE_URL')}leaguehomepage?league_id={leagueId}"
        return render_template("leagueHomepage.html", league=leagueOrError, league_url=leagueUrl)


@app.route("/updateleague", methods=["GET"])
def updateLeague():
    league_id = request.args.get("league_id")
    print(league_id)
    mainController = MainController()
    leagueOrError = mainController.getLeague(int(league_id))
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", errorMessage=leagueOrError.errorMessage())
    else:
        return render_template("updateLeaguePage.html", league=leagueOrError)


if __name__ == "__main__":
    app.run(debug=True)
