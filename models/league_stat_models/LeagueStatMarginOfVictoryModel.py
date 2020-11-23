class LeagueStatMarginOfVictoryModel:

    def __init__(self, marginOfVictory: float, winningTeamName: str, losingTeamName: str, week: int):
        self.__marginOfVictory = marginOfVictory
        self.__winningTeamName = winningTeamName
        self.__losingTeamName = losingTeamName
        self.__week = week

    def getMarginOfVictory(self):
        return self.__marginOfVictory

    def getWinningTeamName(self):
        return self.__winningTeamName

    def getLosingTeamName(self):
        return self.__losingTeamName

    def getWeek(self):
        return self.__week
