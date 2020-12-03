from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class SslCalculator:

    def __init__(self, awal: float, wal: float, ppg: float, maxScore: float, minScore: float):
        self.__awal = awal
        self.__wal = wal
        self.__ppg = ppg
        self.__maxScore = maxScore
        self.__minScore = minScore
        self.__rounder = Rounder()
        self.__awalMultiplier = 50
        self.__walMultiplier = 50
        self.__ppgMultiplier = 2

    def getRawTeamScore(self):
        """
        Returns the Raw Team Score that the team with the given stats has.
        """
        rawTeamScore = ((self.__awal * self.__awalMultiplier) + (self.__ppg * self.__ppgMultiplier) + (
                    self.__maxScore + self.__minScore)) / 10
        return self.__rounder.normalRound(rawTeamScore, 1)

    def getRawTeamSuccess(self):
        """
        Returns the Raw Team Success that the team with the given stats has.
        """
        rawTeamSuccess = ((self.__wal * self.__walMultiplier) + (self.__ppg * self.__ppgMultiplier) + (
                    self.__maxScore + self.__minScore)) / 10
        return self.__rounder.normalRound(rawTeamSuccess, 1)

    def getRawTeamLuck(self):
        """
        Returns the Raw Team Luck that the team with the given stats has.
        """
        return self.__rounder.normalRound(self.getRawTeamSuccess() - self.getRawTeamScore(), 1)
