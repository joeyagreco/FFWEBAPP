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
        self.__awalMultiplier = 100
        self.__walMultiplier = 100
        self.__pointsMultiplier = 20
        self.__minMaxMultiplier = 0.1

    def getTeamScore(self) -> float:
        """
        Returns the Team Score that the team with the given stats has.
        """
        teamScore = ((self.__awal / self.__gamesPlayed) * self.__awalMultiplier) + ((self.__totalTeamPoints / self.__totalLeaguePoints) * self.__pointsMultiplier) + ((self.__maxScore + self.__minScore) * self.__minMaxMultiplier)
        return Rounder.normalRound(teamScore, 1)

    def getTeamSuccess(self) -> float:
        """
        Returns the Team Success that the team with the given stats has.
        """
        teamSuccess = ((self.__wal / self.__gamesPlayed) * self.__walMultiplier) + ((self.__totalTeamPoints / self.__totalLeaguePoints) * self.__pointsMultiplier) + ((self.__maxScore + self.__minScore) * self.__minMaxMultiplier)

        return Rounder.normalRound(teamSuccess, 1)

    def getTeamLuck(self) -> float:
        """
        Returns the Team Luck that the team with the given stats has.
        """
        return Rounder.normalRound(self.getTeamSuccess() - self.getTeamScore(), 1)
