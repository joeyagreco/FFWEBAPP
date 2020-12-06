class TeamStatsModel:

    def __init__(self, teamId: int, teamName: str, wins: int, losses: int, ties: int, winPercentage: float,
                 ppg: float, ppgAgainst: float, plusMinus: float, stddev: float, maxScore: float, minScore: float,
                 awal: float, rawTeamScore: float, rawTeamSuccess: float, rawTeamLuck: int):
        self.__teamId = teamId
        self.__teamName = teamName
        self.__wins = wins
        self.__losses = losses
        self.__ties = ties
        self.__winPercentage = winPercentage
        self.__ppg = ppg
        self.__ppgAgainst = ppgAgainst
        self.__plusMinus = plusMinus
        self.__stddev = stddev
        self.__maxScore = maxScore
        self.__minScore = minScore
        self.__awal = awal
        self.__rawTeamScore = rawTeamScore
        self.__rawTeamSuccess = rawTeamSuccess
        self.__rawTeamLuck = rawTeamLuck

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

    def getPpgAgainst(self):
        return self.__ppgAgainst

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



