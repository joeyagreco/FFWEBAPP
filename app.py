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


@app.route("/add-league", methods=["POST"])
def addLeague():
    leagueName = request.form["league_name"]
    numberOfTeams = int(request.form["number_of_teams"])
    mainController = MainController()
    newLeagueIdOrError = mainController.addLeague(leagueName, numberOfTeams)
    if isinstance(newLeagueIdOrError, Error):
        return render_template("addLeaguePage.html", error_message=newLeagueIdOrError.errorMessage())
    else:
        return redirect(url_for("leagueHomepage", league_id=newLeagueIdOrError))


@app.route("/new-league")
def newLeague():
    return render_template("addLeaguePage.html")


@app.route("/league-homepage", methods=["GET"])
def leagueHomepage():
    leagueId = int(request.args.get("league_id"))
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    else:
        leagueUrl = f"{os.getenv('SERVER_BASE_URL')}league-homepage?league_id={leagueId}"
        return render_template("leagueHomepage.html", league=leagueOrError, league_url=leagueUrl)


@app.route("/update-league", methods=["GET", "POST"])
def updateLeague():
    if request.method == "GET":
        leagueId = int(request.args.get("league_id"))
        mainController = MainController()
        leagueOrError = mainController.getLeague(leagueId)
        if isinstance(leagueOrError, Error):
            return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
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
        if isinstance(leagueOrError, Error):
            # could not find league
            return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
        elif isinstance(updated, Error):
            # could not update league
            return render_template("updateLeaguePage.html", league=leagueOrError, error_message=updated.errorMessage())
        else:
            # successfully updated league
            return render_template("updateLeaguePage.html", league=leagueOrError)
    else:
        return render_template("indexHomepage.html", error_message="ERROR: Not getting a GET or POST.")


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
    week = request.args.get("week")
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if week:
        # if we got a week passed in, render the page with that week displayed
        return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=week)
    else:
        if len(leagueOrError["weeks"]) == 0:
            # no weeks added yet, add an empty week
            weekDict = {"weekNumber": 1, "matchups": []}
            matchupIdCounter = 1
            for i in range(1, len(leagueOrError["teams"]), 2):
                matchup = {"matchupId": matchupIdCounter, "teamA": leagueOrError["teams"][i - 1],
                           "teamB": leagueOrError["teams"][i], "teamAScore": None, "teamBScore": None}
                matchupIdCounter += 1
                weekDict["matchups"].append(matchup)
            leagueOrError["weeks"].append(weekDict)
            return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=1)
        else:
            # default to last (most recent) week in this league
            week = len(leagueOrError) - 1
            return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=week)


@app.route("/add-week", methods=["POST"])
def addWeek():
    # helper function to get team by id
    def getTeamById(league: dict, teamId: int):
        for team in league["teams"]:
            if team["teamId"] == teamId:
                return team

    print(request.form)
    leagueId = int(request.form["league_id"])
    weekNumber = int(request.form["week_number"])
    weekDict = {"weekNumber": weekNumber, "matchups": []}
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)

    matchupIdCounter = 1
    for i in range(1, len(leagueOrError["teams"]), 2):
        matchup = {"matchupId": matchupIdCounter,
                   "teamA": getTeamById(leagueOrError, int(request.form[f"teamAId_matchup_{matchupIdCounter}"])),
                   "teamB": getTeamById(leagueOrError, int(request.form[f"teamBId_matchup_{matchupIdCounter}"])),
                   "teamAScore": request.form[f"teamAScore_matchup_{matchupIdCounter}"],
                   "teamBScore": request.form[f"teamBScore_matchup_{matchupIdCounter}"]}
        weekDict["matchups"].append(matchup)
        matchupIdCounter += 1
    leagueOrError["weeks"].append(weekDict)
    print(leagueOrError)



if __name__ == "__main__":
    app.run(debug=True)
