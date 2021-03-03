class StreakModel:

    def __init__(self, **stats):
        self.__ownerId = stats["ownerId"]
        self.__streakNumber = stats["streakNumber"]
        self.__startDate = stats["startDate"]
        self.__startTeam = stats["startTeam"]
        self.__endDate = stats["endDate"]
        self.__endTeam = stats["endTeam"]
