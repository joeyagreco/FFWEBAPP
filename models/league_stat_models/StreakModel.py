class StreakModel:

    def __init__(self, **stats):
        self.__owner = stats["owner"]
        self.__streakNumber = stats["streakNumber"]
        self.__firstDate = stats["firstDate"]
        self.__firstTeam = stats["firstTeam"]
        self.__lastDate = stats["lastDate"]
        self.__lastTeam = stats["lastTeam"]
        self.__ongoing = stats["ongoing"]

    def getOwner(self):
        return self.__owner

    def getStreakNumber(self):
        return self.__streakNumber

    def getFirstDate(self):
        return self.__firstDate

    def getFirstTeam(self):
        return self.__firstTeam

    def getLastDate(self):
        return self.__lastDate

    def getLastTeam(self):
        return self.__lastTeam

    def getOngoing(self):
        return self.__ongoing
