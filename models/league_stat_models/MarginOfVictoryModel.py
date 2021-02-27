

class MarginOfVictoryModel:

    def __init__(self, **stats):
        self.__marginOfVictory = stats["marginOfVictory"]
        self.__winningTeam = stats["winningTeam"]
        self.__winningTeamPoints = stats["winningTeamPoints"]
        self.__losingTeam = stats["losingTeam"]
        self.__losingTeamPoints = stats["losingTeamPoints"]
        self.__week = stats["week"]
        try:
            self.__year = stats["year"]
        except:
            print(stats)

    def getMarginOfVictory(self):
        return self.__marginOfVictory

    def getWinningTeam(self):
        return self.__winningTeam

    def getWinningTeamPoints(self):
        return self.__winningTeamPoints

    def getLosingTeam(self):
        return self.__losingTeam

    def getLosingTeamPoints(self):
        return self.__losingTeamPoints

    def getWeek(self):
        return self.__week

    def getYear(self):
        try:
            return self.__year
        except:
            return "no year found"
