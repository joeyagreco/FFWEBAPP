class LeagueStatMarginOfVictoryModel:

    def __init__(self, marginOfVictory: float, winningTeamName: str, winningTeamPoints: float, losingTeamName: str, losingTeamPoints: float, week: int):
        self.__marginOfVictory = marginOfVictory
        self.__winningTeamName = winningTeamName
        self.__winningTeamPoints = winningTeamPoints
        self.__losingTeamName = losingTeamName
        self.__losingTeamPoints = losingTeamPoints
        self.__week = week

    def getMarginOfVictory(self):
        return self.__marginOfVictory

    def getWinningTeamName(self):
        return self.__winningTeamName

    def getWinningTeamPoints(self):
        return self.__winningTeamPoints

    def getLosingTeamName(self):
        return self.__losingTeamName

    def getLosingTeamPoints(self):
        return self.__losingTeamPoints

    def getWeek(self):
        return self.__week
