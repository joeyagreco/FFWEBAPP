

class ScoreModel:

    def __init__(self, **stats):
        self.__score = stats["score"]
        self.__teamFor = stats["teamFor"]
        self.__teamAgainst = stats["teamAgainst"]
        self.__outcome = stats["outcome"]
        self.__week = stats["week"]

    def getScore(self):
        return self.__score

    def getTeamFor(self):
        return self.__teamFor

    def getTeamAgainst(self):
        return self.__teamAgainst

    def getOutcome(self):
        return self.__outcome

    def getWeek(self):
        return self.__week
