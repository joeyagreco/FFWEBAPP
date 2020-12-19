class HeadToHeadStatsModel:

    def __init__(self, **stats):
        self.__teamId = stats["teamId"]
        self.__teamName = stats["teamName"]
        self.__wins = stats["wins"]
        self.__losses = stats["losses"]
        self.__ties = stats["ties"]
        self.__winPercentage = stats["winPercentage"]
        self.__ppg = stats["ppg"]
        self.__plusMinus = stats["plusMinus"]
        self.__stddev = stats["stddev"]
        self.__maxScore = stats["maxScore"]
        self.__minScore = stats["minScore"]
        self.__awal = stats["awal"]
        self.__rawTeamScore = stats["rawTeamScore"]
        self.__rawTeamSuccess = stats["rawTeamSuccess"]
        self.__rawTeamLuck = stats["rawTeamLuck"]

    def getTeamId(self):
        return self.__teamId

    def getTeamName(self):
        return self.__teamName

    def getMaxScore(self):
        return self.__maxScore

    def getMinScore(self):
        return self.__minScore

    def getPpg(self):
        return self.__ppg

    def getPlusMinus(self):
        return self.__plusMinus

    def getStddev(self):
        return self.__stddev

    def getWins(self):
        return self.__wins

    def getLosses(self):
        return self.__losses

    def getTies(self):
        return self.__ties

    def getWinPercentage(self):
        return self.__winPercentage

    def getAwal(self):
        return self.__awal

    def getRawTeamScore(self):
        return self.__rawTeamScore

    def getRawTeamSuccess(self):
        return self.__rawTeamSuccess

    def getRawTeamLuck(self):
        return self.__rawTeamLuck




