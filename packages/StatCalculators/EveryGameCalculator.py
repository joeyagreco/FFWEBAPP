from typing import List

from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from models.league_stat_models.MarginOfVictoryModel import MarginOfVictoryModel
from models.league_stat_models.ScoreModel import ScoreModel


class EveryGameCalculator:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getAllMarginOfVictories(self) -> List[MarginOfVictoryModel]:
        """
        Returns a list of MarginOfVictoryModels.
        """
        models = []
        decimalPlacesRoundedTo = Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamAScore() > matchup.getTeamBScore():
                    # team A won
                    mov = matchup.getTeamAScore() - matchup.getTeamBScore()
                    mov = Rounder.normalRound(mov, decimalPlacesRoundedTo)
                    teamFor = matchup.getTeamA()
                    teamForPoints = matchup.getTeamAScore()
                    teamAgainst = matchup.getTeamB()
                    teamAgainstPoints = matchup.getTeamBScore()
                    weekNumber = week.getWeekNumber()
                elif matchup.getTeamBScore() > matchup.getTeamAScore():
                    # team B won
                    mov = matchup.getTeamBScore() - matchup.getTeamAScore()
                    mov = Rounder.normalRound(mov, decimalPlacesRoundedTo)
                    teamFor = matchup.getTeamB()
                    teamForPoints = matchup.getTeamBScore()
                    teamAgainst = matchup.getTeamA()
                    teamAgainstPoints = matchup.getTeamAScore()
                    weekNumber = week.getWeekNumber()
                else:
                    # tie, dont care about this
                    continue
                model = MarginOfVictoryModel(marginOfVictory=mov,
                                             winningTeam=teamFor,
                                             winningTeamPoints=teamForPoints,
                                             losingTeam=teamAgainst,
                                             losingTeamPoints=teamAgainstPoints,
                                             week=weekNumber)
                models.append(model)
        return models

    def getAllScores(self) -> List[ScoreModel]:
        """
        Returns a list of ScoreModels.
        """
        models = []
        decimalPlacesRoundedTo = Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                weekNumber = week.getWeekNumber()
                # team A score
                teamAScore = matchup.getTeamAScore()
                teamAScore = Rounder.normalRound(teamAScore, decimalPlacesRoundedTo)
                teamAFor = matchup.getTeamA()
                teamAAgainst = matchup.getTeamB()
                teamAOutcome = LeagueModelNavigator.getGameOutcomeAsString(matchup, matchup.getTeamA().getTeamId())
                # team B score
                teamBScore = matchup.getTeamBScore()
                teamBScore = Rounder.normalRound(teamBScore, decimalPlacesRoundedTo)
                teamBFor = matchup.getTeamB()
                teamBAgainst = matchup.getTeamA()
                teamBOutcome = LeagueModelNavigator.getGameOutcomeAsString(matchup, matchup.getTeamB().getTeamId())
                # create both team models and add to list
                teamAModel = ScoreModel(score=teamAScore,
                                        teamFor=teamAFor,
                                        teamAgainst=teamAAgainst,
                                        outcome=teamAOutcome,
                                        week=weekNumber)
                teamBModel = ScoreModel(score=teamBScore,
                                        teamFor=teamBFor,
                                        teamAgainst=teamBAgainst,
                                        outcome=teamBOutcome,
                                        week=weekNumber)
                models.append(teamAModel)
                models.append(teamBModel)
        return models
