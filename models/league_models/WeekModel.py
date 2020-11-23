class WeekModel:

    # def __init__(self, weekNumber: int, matchups: List[MatchupModel]):
    def __init__(self, weekNumber: int, matchups):
        self.__weekNumber = weekNumber
        self.__matchups = matchups

    def getWeekNumber(self):
        return self.__weekNumber

    def getMatchups(self):
        return self.__matchups
