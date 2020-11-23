class TeamStatsModel:

    def __init__(self, teamId: int, ppg: float, stddev: float, awal: float, rawTeamScore: float, rawTeamSuccess: float,
                 rawTeamLuck: int, plusMinus: float, maxScore: float, minScore: float):
        self.__teamId = teamId
        self.__ppg = ppg
        self.__stddev = stddev
        self.__awal = awal
        self.__rawTeamScore = rawTeamScore
        self.__rawTeamSuccess = rawTeamSuccess
        self.__rawTeamLuck = rawTeamLuck
        self.__plusMinus = plusMinus
        self.__maxScore = maxScore
        self.__minScore = minScore

    def getTeamId(self):
        return self.__teamId

    def getPpg(self):
        return self.__ppg

    def getStddev(self):
        return self.__stddev

    def getAwal(self):
        return self.__awal

    def getRawTeamScore(self):
        return self.__rawTeamScore

    def getRawTeamSuccess(self):
        return self.__rawTeamSuccess

    def getRawTeamLuck(self):
        return self.__rawTeamLuck

    def getPlusMinus(self):
        return self.__plusMinus

    def getMaxScore(self):
        return self.__maxScore

    def getMinScore(self):
        return self.__minScore