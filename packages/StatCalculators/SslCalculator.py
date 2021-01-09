from helpers.Rounder import Rounder


class SslCalculator:

    def __init__(self, awal: float, wal: float, totalTeamPoints: float, maxScore: float, minScore: float,
                 gamesPlayed: int, totalLeaguePoints: float):
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

    def getTeamScore(self):
        """
        Returns the Team Score that the team with the given stats has.
        """
        teamScore = (((self.__awal / self.__gamesPlayed) * self.__awalMultiplier) + (
                    (self.__totalTeamPoints / self.__totalLeaguePoints) * self.__pointsMultiplier) + (
                                self.__maxScore + self.__minScore)) / 10
        return self.__rounder.normalRound(teamScore, 1)

    def getTeamSuccess(self):
        """
        Returns the Team Success that the team with the given stats has.
        """
        teamSuccess = (((self.__wal / self.__gamesPlayed) * self.__walMultiplier) + (
                    (self.__totalTeamPoints / self.__totalLeaguePoints) * self.__pointsMultiplier) + (
                                  self.__maxScore + self.__minScore)) / 10
        return self.__rounder.normalRound(teamSuccess, 1)

    def getTeamLuck(self):
        """
        Returns the Team Luck that the team with the given stats has.
        """
        return self.__rounder.normalRound(self.getTeamSuccess() - self.getTeamScore(), 1)
