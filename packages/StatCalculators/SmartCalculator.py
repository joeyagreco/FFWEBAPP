from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class SmartCalculator:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getDeservedWinsOfScore(self, score: float):
        """
        Returns [essentially] the percentile of which this score would rank in self.__leagueModel.
        This is the percentage of games this score would win if it played against every other score [thus, deserved wins].
        Note: This assumes that the given score already exists in self.__leagueModel.
        """
        leagueModelNavigator = LeagueModelNavigator()
        rounder = Rounder()
        # round the given score properly
        decimalPlacesToRoundTo = rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        score = rounder.normalRound(score, decimalPlacesToRoundTo)
        scoresBeat = 0
        scoresTied = 0
        totalScores = 0
        allScores = leagueModelNavigator.getAllScoresInLeague(self.__leagueModel)
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
        deservedWins = rounder.normalRound(rawPercentile, 2)
        return deservedWins

    def getDeservedWinsOfScores(self, scores: list):
        """
        Returns a combination of the deserved wins a team with the given scores should have.
        Note: This assumes that the given scores already exist in self.__leagueModel.
        """
        rounder = Rounder()
        deservedWins = 0
        for score in scores:
            deservedWins += self.getDeservedWinsOfScore(score)
        # round to 2 decimal places by default
        deservedWins = rounder.normalRound(deservedWins, 2)
        return deservedWins
