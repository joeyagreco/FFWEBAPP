from typing import List

from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from models.league_stat_models.MarginOfVictoryModel import MarginOfVictoryModel
from models.league_stat_models.ScoreModel import ScoreModel


class EveryGameCalculator:

    def __init__(self, leagueModel: LeagueModel, years: list):
        self.__leagueModel = leagueModel
        self.__years = years

    def getAllMarginOfVictories(self) -> List[MarginOfVictoryModel]:
        """
        Returns a list of MarginOfVictoryModels.
        """
        models = []
        decimalPlacesRoundedTo = Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        for year in self.__years:
            for week in self.__leagueModel.years[str(year)].getWeeks():
                for matchup in week.getMatchups():
                    if matchup.teamAScore > matchup.teamBScore:
                        # team A won
                        mov = matchup.teamAScore - matchup.teamBScore
                        mov = Rounder.normalRound(mov, decimalPlacesRoundedTo)
                        teamFor = matchup.teamA
                        teamForPoints = matchup.teamAScore
                        teamAgainst = matchup.teamB
                        teamAgainstPoints = matchup.teamBScore
                        weekNumber = week.getWeekNumber()
                    elif matchup.teamBScore > matchup.teamAScore:
                        # team B won
                        mov = matchup.teamBScore - matchup.teamAScore
                        mov = Rounder.normalRound(mov, decimalPlacesRoundedTo)
                        teamFor = matchup.teamB
                        teamForPoints = matchup.teamBScore
                        teamAgainst = matchup.teamA
                        teamAgainstPoints = matchup.teamAScore
                        weekNumber = week.getWeekNumber()
                    else:
                        # tie, dont care about this
                        continue
                    model = MarginOfVictoryModel(marginOfVictory=mov,
                                                 winningTeam=teamFor,
                                                 winningTeamPoints=teamForPoints,
                                                 losingTeam=teamAgainst,
                                                 losingTeamPoints=teamAgainstPoints,
                                                 week=weekNumber,
                                                 year=year)
                    models.append(model)
        return models

    def getAllScores(self) -> List[ScoreModel]:
        """
        Returns a list of ScoreModels.
        """
        models = []
        decimalPlacesRoundedTo = Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        for year in self.__years:
            for week in self.__leagueModel.years[str(year)].getWeeks():
                for matchup in week.getMatchups():
                    weekNumber = week.getWeekNumber()
                    # team A score
                    teamAScore = matchup.teamAScore
                    teamAScore = Rounder.normalRound(teamAScore, decimalPlacesRoundedTo)
                    teamAFor = matchup.teamA
                    teamAAgainst = matchup.teamB
                    teamAOutcome = LeagueModelNavigator.getGameOutcomeAsString(matchup, matchup.teamA.teamId)
                    # team B score
                    teamBScore = matchup.teamBScore
                    teamBScore = Rounder.normalRound(teamBScore, decimalPlacesRoundedTo)
                    teamBFor = matchup.teamB
                    teamBAgainst = matchup.teamA
                    teamBOutcome = LeagueModelNavigator.getGameOutcomeAsString(matchup, matchup.teamB.teamId)
                    # create both team models and add to list
                    teamAModel = ScoreModel(score=teamAScore,
                                            teamFor=teamAFor,
                                            teamAgainst=teamAAgainst,
                                            outcome=teamAOutcome,
                                            week=weekNumber,
                                            year=year)
                    teamBModel = ScoreModel(score=teamBScore,
                                            teamFor=teamBFor,
                                            teamAgainst=teamBAgainst,
                                            outcome=teamBOutcome,
                                            week=weekNumber,
                                            year=year)
                    models.append(teamAModel)
                    models.append(teamBModel)
        return models
