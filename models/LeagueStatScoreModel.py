class LeagueStatScoreModel:

    def __init__(self, teamName: str, score: float, week: int):
        self.__teamName = teamName
        self.__score = score
        self.__week = week

    def getTeamName(self):
        return self.__teamName

    def getScore(self):
        return self.__score

    def getWeek(self):
        return self.__week
