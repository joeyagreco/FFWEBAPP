from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class SmartCalculator:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getSmartWinsOfScore(self, score: float, **params):
        """
        Returns [essentially] the percentile of which this score would rank in self.__leagueModel.
        This is the percentage of games this score would win if it played against every other score.
        Note: This assumes that the given score already exists in self.__leagueModel.
        WEEK: [int] Gives smart wins through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        rounder = Rounder()
        # round the given score properly
        decimalPlacesToRoundTo = rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        score = rounder.normalRound(score, decimalPlacesToRoundTo)
        scoresBeat = 0
        scoresTied = 0
        totalScores = 0
        allScores = leagueModelNavigator.getAllScoresInLeague(self.__leagueModel, week=weekNumber)
        for s in allScores:
            totalScores += 1
            if score > s:
                scoresBeat += 1
            elif score == s:
                scoresTied += 1
        # don't include *this* score in with the other scores tied or total scores(the score will always find and tie itself)
        scoresTied -= 1
        totalScores -= 1
        rawPercentile = (scoresBeat + (scoresTied * 0.5)) / totalScores
        smartWins = rounder.normalRound(rawPercentile, 2)
        return smartWins

    def getSmartWinsOfScoresList(self, scoresList: list, **params):
        """
        Returns the smart wins a team with the given scores should have.
        Note: This assumes that the given scores already exist in self.__leagueModel.
        WEEK: [int] Gives smart wins through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        rounder = Rounder()
        smartWins = 0
        for score in scoresList:
            smartWins += self.getSmartWinsOfScore(score, week=weekNumber)
        # round to 2 decimal places by default
        smartWins = rounder.normalRound(smartWins, 2)
        return smartWins

    def getSmartWinsAdjustmentOfScores(self, scores: list, wal: float):
        """
        Returns the smart wins adjustment of a team with the given scores and the given wal.
        Note: This assumes that the given scores already exist in self.__leagueModel.
        """
        rounder = Rounder()
        smartWins = self.getSmartWinsOfScoresList(scores)
        return rounder.normalRound(smartWins - wal, 2)
