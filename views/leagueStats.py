from flask import redirect, url_for, render_template

from app import app
from controllers.MainController import MainController
from helpers.Constants import Constants
from helpers.LeagueModelNavigator import LeagueModelNavigator
from packages.Exceptions.DatabaseError import DatabaseError
from packages.Exceptions.InvalidStatSelectionError import InvalidStatSelectionError
from packages.Exceptions.LeagueNotFoundError import LeagueNotFoundError


@app.route("/league-stats/<int:leagueId>/<year>/all-scores", methods=["GET"])
def allScores(leagueId, year):
    try:
        league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.ALL_SCORES_STAT_TITLE)
    except (DatabaseError, InvalidStatSelectionError, LeagueNotFoundError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return render_template("league_stats/allScoresPage.html", league=league,
                           selected_stat=Constants.ALL_SCORES_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>/<year>/league-averages", methods=["GET"])
def leagueAverages(leagueId, year):
    try:
        league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.LEAGUE_AVERAGES_STAT_TITLE)
    except (DatabaseError, InvalidStatSelectionError, LeagueNotFoundError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return render_template("league_stats/leagueAveragesPage.html", league=league,
                           selected_stat=Constants.LEAGUE_AVERAGES_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>/<year>/losing-streaks", methods=["GET"])
def losingStreaks(leagueId, year):
    try:
        league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.LOSING_STREAKS_STAT_TITLE)
    except (DatabaseError, InvalidStatSelectionError, LeagueNotFoundError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return render_template("league_stats/losingStreaksPage.html", league=league,
                           selected_stat=Constants.LOSING_STREAKS_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>/<year>/margins-of-victory", methods=["GET"])
def marginsOfVictory(leagueId, year):
    try:
        league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.MARGINS_OF_VICTORY_STAT_TITLE)
    except (DatabaseError, InvalidStatSelectionError, LeagueNotFoundError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return render_template("league_stats/marginsOfVictoryPage.html", league=league,
                           selected_stat=Constants.MARGINS_OF_VICTORY_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>/<year>/owner-comparison", methods=["GET"])
def ownerComparison(leagueId, year):
    if year != "0":
        return redirect(url_for("ownerComparison", leagueId=leagueId, year="0"))
    try:
        league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.OWNER_COMPARISON_STAT_TITLE)
    except (DatabaseError, InvalidStatSelectionError, LeagueNotFoundError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return render_template("league_stats/ownerComparisonPage.html", league=league,
                           selected_stat=Constants.OWNER_COMPARISON_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants, disable_year_dropdown=True)


@app.route("/league-stats/<int:leagueId>/<year>/winning-streaks", methods=["GET"])
def winningStreaks(leagueId, year):
    try:
        league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.WINNING_STREAKS_STAT_TITLE)
    except (DatabaseError, InvalidStatSelectionError, LeagueNotFoundError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return render_template("league_stats/winningStreaksPage.html", league=league,
                           selected_stat=Constants.WINNING_STREAKS_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>", methods=["GET"])
def leagueStats(leagueId):
    # default league stats route
    mainController = MainController()
    try:
        leagueModel = mainController.getLeagueModel(leagueId)
    except (DatabaseError, InvalidStatSelectionError, LeagueNotFoundError) as e:
        return render_template("indexHomepage.html", error_message=str(e))
    # give most recent year
    years = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModel, asInts=True))
    year = years[-1]
    # TODO: make this choose the first league stats page automatically
    return redirect(url_for("allScores", leagueId=leagueId, year=year))


def __getLeagueAndStatsModel(leagueId, year, statSelection):
    """
    Raises DatabaseError
    Raises InvalidStatSelectionError
    Raises LeagueNotFoundError
    """
    statOptions = Constants.LEAGUE_STATS_STAT_TITLES
    if statSelection is None:
        statSelection = statOptions[0]
    mainController = MainController()
    league = mainController.getLeague(leagueId)
    leagueModel = mainController.getLeagueModel(leagueId)
    if year is None:
        # give most recent year if none is given
        years = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModel, asInts=True))
        year = years[-1]
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModel, asInts=True))
    else:
        yearList = [year]
    return league, mainController.getLeagueStatsModel(leagueModel, yearList, statSelection)
