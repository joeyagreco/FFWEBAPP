from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from models.league_stat_models.MarginOfVictoryModel import MarginOfVictoryModel
from models.league_stat_models.ScoreModel import ScoreModel


class EveryGameCalculator:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getAllMarginOfVictories(self):
        """
        Returns a list of MarginOfVictoryModels.
        """
        models = []
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamAScore() > matchup.getTeamBScore():
                    # team A won
                    mov = matchup.getTeamAScore() - matchup.getTeamBScore()
                    teamFor = matchup.getTeamA()
                    teamForPoints = matchup.getTeamAScore()
                    teamAgainst = matchup.getTeamB()
                    teamAgainstPoints = matchup.getTeamBScore()
                    weekNumber = week.getWeekNumber()
                elif matchup.getTeamBScore() > matchup.getTeamAScore():
                    # team B won
                    mov = matchup.getTeamBScore() - matchup.getTeamAScore()
                    teamFor = matchup.getTeamB()
                    teamForPoints = matchup.getTeamBScore()
                    teamAgainst = matchup.getTeamA()
                    teamAgainstPoints = matchup.getTeamAScore()
                    weekNumber = week.getWeekNumber()
                else:
                    # tie, dont care about this
                    continue
                model = MarginOfVictoryModel(mov, teamFor, teamForPoints, teamAgainst, teamAgainstPoints, weekNumber)
                models.append(model)
        return models

    def getAllScores(self):
        """
        Returns a list of ScoreModels.
        """
        leagueModelNavigator = LeagueModelNavigator()
        models = []
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                weekNumber = week.getWeekNumber()
                # team A score
                teamAScore = matchup.getTeamAScore()
                teamAFor = matchup.getTeamA()
                teamAAgainst = matchup.getTeamB()
                teamAOutcome = leagueModelNavigator.getGameOutcomeAsString(matchup, matchup.getTeamA().getTeamId())
                # team B score
                teamBScore = matchup.getTeamBScore()
                teamBFor = matchup.getTeamB()
                teamBAgainst = matchup.getTeamA()
                teamBOutcome = leagueModelNavigator.getGameOutcomeAsString(matchup, matchup.getTeamB().getTeamId())
                # create both team models and add to list
                teamAModel = ScoreModel(teamAScore, teamAFor, teamAAgainst, teamAOutcome, weekNumber)
                teamBModel = ScoreModel(teamBScore, teamBFor, teamBAgainst, teamBOutcome, weekNumber)
                models.append(teamAModel)
                models.append(teamBModel)
        return models
