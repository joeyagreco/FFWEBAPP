class StreakModel:

    def __init__(self, **stats):
        self.__ownerId = stats["ownerId"]
        self.__streakNumber = stats["streakNumber"]
        self.__startDate = stats["startDate"]
        self.__startTeam = stats["startTeam"]
        self.__endDate = stats["endDate"]
        self.__endTeam = stats["endTeam"]

    def getOwnerId(self):
        return self.__ownerId

    def getStreakNumber(self):
        return self.__streakNumber

    def getStartDate(self):
        return self.__startDate

    def getStartTeam(self):
        return self.__startTeam

    def getEndDate(self):
        return self.__endDate

    def getEndTeam(self):
        return self.__endTeam
