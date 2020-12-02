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

    def getRawTeamScore(self):
        """
        Returns the Raw Team Score that the team with self.__teamId has in the given league.
        """
        awalMultiplier = 50
        ppgMultiplier = 2
        rawTeamScore = ((self.__awal * awalMultiplier) + (self.__ppg * ppgMultiplier) + (
                    self.__maxScore + self.__minScore)) / 10
        return self.__rounder.normalRound1(rawTeamScore)
