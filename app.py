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
        updated = mainController.updateLeague(leagueId, leagueName, teams, [])
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
    if isinstance(leagueOrError, Error):
        # could not load league
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    else:
        if week:
            # if we got a week passed in, render the page with that week displayed
            week = int(week)
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
                week = len(leagueOrError["weeks"])
                return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=week)


@app.route("/update-week", methods=["POST"])
def updateWeek():
    # helper function to get team by id
    def getTeamById(league: dict, teamId: int):
        for team in league["teams"]:
            if team["teamId"] == teamId:
                return team

    # helper function to check if week exists in league
    def weekExists(league: dict, weekNum: int):
        for week in league["weeks"]:
            if week["weekNumber"] == weekNum:
                return True
        return False

    leagueId = int(request.form["league_id"])
    weekNumber = int(request.form["week_number"])
    weekDict = {"weekNumber": weekNumber, "matchups": []}
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)

    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    else:
        matchupIdCounter = 1
        for i in range(1, len(leagueOrError["teams"]), 2):
            matchup = {"matchupId": matchupIdCounter,
                       "teamA": getTeamById(leagueOrError, int(request.form[f"teamAId_matchup_{matchupIdCounter}"])),
                       "teamB": getTeamById(leagueOrError, int(request.form[f"teamBId_matchup_{matchupIdCounter}"])),
                       "teamAScore": int(request.form[f"teamAScore_matchup_{matchupIdCounter}"]),
                       "teamBScore": int(request.form[f"teamBScore_matchup_{matchupIdCounter}"])}
            weekDict["matchups"].append(matchup)
            matchupIdCounter += 1
        # check if this league has this week already, if so, overwrite it, if not, add it
        if weekExists(leagueOrError, weekNumber):
            # overwrite week
            leagueOrError["weeks"][weekNumber - 1] = weekDict
        else:
            # add week
            leagueOrError["weeks"].append(weekDict)

        # update league in database
        response = mainController.updateLeague(leagueOrError["_id"],
                                               leagueOrError["leagueName"],
                                               leagueOrError["teams"],
                                               leagueOrError["weeks"])
        if isinstance(response, Error):
            # could not update week
            return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=weekNumber,
                                   error_message=response.errorMessage())
        newLeagueOrError = mainController.getLeague(leagueId)

        if isinstance(newLeagueOrError, Error):
            return render_template("indexHomepage.html", error_message=newLeagueOrError.errorMessage())
        else:
            return render_template("addUpdateWeeksPage.html", league=newLeagueOrError, week_number=weekNumber)


@app.route("/add-week", methods=["GET"])
def addWeek():
    leagueId = int(request.args.get("league_id"))
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    weekNumber = len(leagueOrError["weeks"]) + 1
    # add an empty week
    weekDict = {"weekNumber": weekNumber, "matchups": []}
    matchupIdCounter = 1
    for i in range(1, len(leagueOrError["teams"]), 2):
        matchup = {"matchupId": matchupIdCounter, "teamA": leagueOrError["teams"][i - 1],
                   "teamB": leagueOrError["teams"][i], "teamAScore": None, "teamBScore": None}
        matchupIdCounter += 1
        weekDict["matchups"].append(matchup)
    leagueOrError["weeks"].append(weekDict)
    return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=weekNumber)


@app.route("/delete-week", methods=["GET"])
def deleteWeek():
    leagueId = int(request.args.get("league_id"))
    week = int(request.args.get("week"))
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    if isinstance(leagueOrError, Error):
        # couldn't get league from database
        return render_template("indexHomepage.html", error_message=leagueOrError.errorMessage())
    # don't allow user to delete week 1
    if week == 1:
        error = Error("Week 1 cannot be deleted.")
        return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=week, error_message=error.errorMessage())
    # returnWeek is where the user is returned if the week is ineligible for deletion
    returnWeek = len(leagueOrError["weeks"])
    if week == len(leagueOrError["weeks"]):
        # if this is the last week added [most recent week]
        leagueOrError = mainController.deleteWeek(leagueId)
        if isinstance(leagueOrError, Error):
            # couldn't delete week
            return redirect(url_for('index'))
        else:
            # successfully deleted week
            return redirect(url_for('addUpdateWeeks', league_id=leagueOrError["_id"]))
    else:
        # determine if this is an unsaved, added week that is being deleted OR a non-last week
        if week > returnWeek:
            return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=returnWeek)
        else:
            error = Error("Only the most recent week can be deleted.")
            return render_template("addUpdateWeeksPage.html", league=leagueOrError, week_number=returnWeek,
                                   error_message=error.errorMessage())


if __name__ == "__main__":
    app.run(debug=True)
