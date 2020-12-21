from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class SslCalculator:

    def __init__(self, awal: float, wal: float, totalTeamPoints: float, maxScore: float, minScore: float, gamesPlayed: int, totalLeaguePoints: float):
        self.__awal = awal
        self.__wal = wal
        self.__totalTeamPoints = totalTeamPoints
        self.__maxScore = maxScore
        self.__minScore = minScore
        self.__gamesPlayed = gamesPlayed
        self.__totalLeaguePoints = totalLeaguePoints
        self.__rounder = Rounder()
        self.__awalMultiplier = 1000
        self.__walMultiplier = 1000
        self.__pointsMultiplier = 200

    def getRawTeamScore(self):
        """
        Returns the Raw Team Score that the team with the given stats has.
        """
        rawTeamScore = (((self.__awal/self.__gamesPlayed) * self.__awalMultiplier) + ((self.__totalTeamPoints / self.__totalLeaguePoints) * self.__pointsMultiplier) + (
                    self.__maxScore + self.__minScore)) / 10
        return self.__rounder.normalRound(rawTeamScore, 1)

    def getRawTeamSuccess(self):
        """
        Returns the Raw Team Success that the team with the given stats has.
        """
        rawTeamSuccess = (((self.__wal/self.__gamesPlayed) * self.__walMultiplier) + ((self.__totalTeamPoints / self.__totalLeaguePoints) * self.__pointsMultiplier) + (
                    self.__maxScore + self.__minScore)) / 10
        return self.__rounder.normalRound(rawTeamSuccess, 1)

    def getRawTeamLuck(self):
        """
        Returns the Raw Team Luck that the team with the given stats has.
        """
        return self.__rounder.normalRound(self.getRawTeamSuccess() - self.getRawTeamScore(), 1)
