import ast

from flask import redirect, url_for, request, render_template

from app import app
from controllers.MainController import MainController
from helpers.Error import Error
from packages.Exceptions.DatabaseError import DatabaseError


@app.route("/add-update-weeks/<int:leagueId>/<year>/<week>", methods=["GET"])
@app.route("/add-update-weeks/<int:leagueId>/<year>", defaults={"week": None}, methods=["GET"])
def addUpdateWeeks(leagueId, year, week):
    errorMessage = request.args.get("error_message")
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except DatabaseError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    else:
        if week is not None:
            # if we got a week passed in, render the page with that week displayed
            week = int(week)
            return render_template("addUpdateWeeksPage.html", league=league, selected_year=year,
                                   week_number=week, error_message=errorMessage)
        else:
            yearDict = league["years"][str(year)]
            if len(yearDict["weeks"]) == 0:
                # no weeks added yet, add an empty week
                weekDict = {"weekNumber": 1, "matchups": []}
                matchupIdCounter = 1
                for i in range(1, len(yearDict["teams"]), 2):
                    matchup = {"matchupId": matchupIdCounter,
                               "teamA": yearDict["teams"][i - 1],
                               "teamB": yearDict["teams"][i],
                               "teamAScore": None,
                               "teamBScore": None}
                    matchupIdCounter += 1
                    weekDict["matchups"].append(matchup)
                yearDict["weeks"].append(weekDict)
                league["years"][str(year)] = yearDict
                return render_template("addUpdateWeeksPage.html", league=league, selected_year=year,
                                       week_number=1, error_message=errorMessage)
            else:
                # default to last (most recent) week in this league
                week = len(yearDict["weeks"])
                return render_template("addUpdateWeeksPage.html", league=league, selected_year=year,
                                       week_number=week, error_message=errorMessage)


@app.route("/update-week", methods=["POST"])
def updateWeek():
    # helper function to get team by id
    def getTeamById(league: dict, teamId: int, year: int):
        for team in league["years"][year]["teams"]:
            if team["teamId"] == teamId:
                return team

    # helper function to check if week exists in league
    def weekExists(league: dict, weekNum: int, year: int):
        for week in league["years"][year]["weeks"]:
            if week["weekNumber"] == weekNum:
                return True
        return False

    # convert dict
    newDataStr = request.data.decode("UTF-8")
    newDataDict = ast.literal_eval(newDataStr)
    leagueId = int(newDataDict["league_id"])
    weekNumber = int(newDataDict["week_number"])
    yearNumber = newDataDict["year_number"]
    weekDict = {"weekNumber": weekNumber, "matchups": []}
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except DatabaseError as e:
        return redirect(url_for('index', error_message=str(e)))
    else:
        matchupIdCounter = 1
        for i in range(1, len(league["years"][yearNumber]["teams"]), 2):
            matchup = {"matchupId": matchupIdCounter,
                       "teamA": getTeamById(league, int(newDataDict[f"teamAId_matchup_{matchupIdCounter}"]),
                                            yearNumber),
                       "teamB": getTeamById(league, int(newDataDict[f"teamBId_matchup_{matchupIdCounter}"]),
                                            yearNumber),
                       "teamAScore": float(newDataDict[f"teamAScore_matchup_{matchupIdCounter}"]),
                       "teamBScore": float(newDataDict[f"teamBScore_matchup_{matchupIdCounter}"])}
            weekDict["matchups"].append(matchup)
            matchupIdCounter += 1
        # check if this league has this week already, if so, overwrite it, if not, add it
        if weekExists(league, weekNumber, yearNumber):
            # overwrite week
            league["years"][yearNumber]["weeks"][weekNumber - 1] = weekDict
        else:
            # add week
            league["years"][yearNumber]["weeks"].append(weekDict)
        # update league in database
        try:
            mainController.updateLeague(league["_id"],
                                        league["leagueName"],
                                        league["years"])
        except DatabaseError as e:
            return redirect(url_for("addUpdateWeeks", league_id=leagueId, week=weekNumber, year=yearNumber,
                                    error_message=str(e)))
        return redirect(url_for('addUpdateWeeks', leagueId=league["_id"], year=yearNumber, week=weekNumber))


@app.route("/add-week/<int:leagueId>/<year>", methods=["GET"])
def addWeek(leagueId, year):
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except DatabaseError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    weekNumber = len(league["years"][year]["weeks"]) + 1
    # add an empty week
    weekDict = {"weekNumber": weekNumber, "matchups": []}
    matchupIdCounter = 1
    for i in range(1, len(league["years"][year]["teams"]), 2):
        matchup = {"matchupId": matchupIdCounter,
                   "teamA": league["years"][year]["teams"][i - 1],
                   "teamB": league["years"][year]["teams"][i],
                   "teamAScore": None,
                   "teamBScore": None}
        matchupIdCounter += 1
        weekDict["matchups"].append(matchup)
    league["years"][year]["weeks"].append(weekDict)
    return render_template("addUpdateWeeksPage.html", league=league, week_number=weekNumber,
                           selected_year=year)


# TODO: use DELETE instead of GET
@app.route("/delete-week/<int:leagueId>/<year>/<int:week>", methods=["GET"])
def deleteWeek(leagueId, year, week):
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except DatabaseError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    # don't allow user to delete week 1
    if week == 1:
        error = Error("Week 1 cannot be deleted.")
        # check if week 1 already existed
        if len(league["years"][year]["weeks"]) == 0:
            # week 1 didn't exist
            return redirect(url_for('addUpdateWeeks', leagueId=league["_id"], year=year))
        else:
            # week 1 exists
            return render_template("addUpdateWeeksPage.html", league=league, week_number=week,
                                   selected_year=year, error_message=error.errorMessage())
    # returnWeek is where the user is returned if the week is ineligible for deletion
    returnWeek = len(league["years"][year]["weeks"])
    if week == len(league["years"][year]["weeks"]):
        # if this is the last week added [most recent week]
        try:
            league = mainController.deleteWeek(leagueId, int(year))
        except DatabaseError as e:
            return redirect(url_for('index', error_message=str(e)))
        # successfully deleted week
        return redirect(url_for('addUpdateWeeks', leagueId=league["_id"], year=year))
    else:
        # determine if this is an unsaved, added week that is being deleted OR a non-last week
        if week > returnWeek:
            return render_template("addUpdateWeeksPage.html", league=league, week_number=returnWeek,
                                   selected_year=year)
        else:
            error = Error("Only the most recent week can be deleted.")
            return render_template("addUpdateWeeksPage.html", league=league, week_number=returnWeek,
                                   selected_year=year, error_message=error.errorMessage())
