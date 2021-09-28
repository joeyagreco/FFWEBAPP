from flask import render_template

from app import app
from controllers.MainController import MainController
from helpers.Constants import Constants
from helpers.LeagueModelNavigator import LeagueModelNavigator


@app.route("/league-stats/<int:leagueId>/<year>/all-scores", methods=["GET"])
def allScores(leagueId, year):
    league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.ALL_SCORES_STAT_TITLE)
    return render_template("leagueStatsPage.html", league=league, selected_stat=Constants.ALL_SCORES_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>/<year>/league-averages", methods=["GET"])
def leagueAverages(leagueId, year):
    league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.LEAGUE_AVERAGES_STAT_TITLE)
    return render_template("leagueStatsPage.html", league=league, selected_stat=Constants.LEAGUE_AVERAGES_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>/<year>/losing-streaks", methods=["GET"])
def losingStreaks(leagueId, year):
    league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.LOSING_STREAKS_STAT_TITLE)
    return render_template("leagueStatsPage.html", league=league, selected_stat=Constants.LOSING_STREAKS_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>/<year>/margins-of-victory", methods=["GET"])
def marginsOfVictory(leagueId, year):
    league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.MARGINS_OF_VICTORY_STAT_TITLE)
    return render_template("leagueStatsPage.html", league=league, selected_stat=Constants.MARGINS_OF_VICTORY_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>/<year>/owner-comparison", methods=["GET"])
def ownerComparison(leagueId, year):
    league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.OWNER_COMPARISON_STAT_TITLE)
    return render_template("leagueStatsPage.html", league=league, selected_stat=Constants.OWNER_COMPARISON_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>/<year>/winning-streaks", methods=["GET"])
def winningStreaks(leagueId, year):
    league, statsModel = __getLeagueAndStatsModel(leagueId, year, Constants.WINNING_STREAKS_STAT_TITLE)
    return render_template("leagueStatsPage.html", league=league, selected_stat=Constants.WINNING_STREAKS_STAT_TITLE,
                           stats_models=statsModel, selected_year=year,
                           constants=Constants)


@app.route("/league-stats/<int:leagueId>", methods=["GET"])
def leagueStats(leagueId):
    statOptions = Constants.LEAGUE_STATS_STAT_TITLES
    statSelection = statOptions[0]
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    # give most recent year
    years = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
    year = years[-1]
    yearList = [year]
    statsModelOrError = mainController.getLeagueStatsModel(leagueModelOrError, yearList, statSelection)
    return render_template("leagueStatsPage.html", league=leagueOrError, selected_stat=statSelection,
                           stats_models=statsModelOrError, selected_year=year,
                           constants=Constants)


def __getLeagueAndStatsModel(leagueId, year, statSelection):
    statOptions = Constants.LEAGUE_STATS_STAT_TITLES
    if statSelection is None:
        statSelection = statOptions[0]
    mainController = MainController()
    leagueOrError = mainController.getLeague(leagueId)
    leagueModelOrError = mainController.getLeagueModel(leagueId)
    if year is None:
        # give most recent year if none is given
        years = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
        year = years[-1]
        yearList = [year]
    elif year == "0":
        # give them all years (ALL TIME)
        yearList = sorted(LeagueModelNavigator.getAllYearsWithWeeks(leagueModelOrError, asInts=True))
    else:
        yearList = [year]
    return leagueOrError, mainController.getLeagueStatsModel(leagueModelOrError, yearList, statSelection)
