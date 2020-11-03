from models import TeamModel


class MatchupModel:

    def __init__(self, teamA: TeamModel, teamB: TeamModel, teamAScore: float, teamBScore: float):
        self.__teamA = teamA
        self.__teamB = teamB
        self.__teamAScore = teamAScore
        self.__teamBScore = teamBScore

    def getTeamA(self):
        return self.__teamA

    def getTeamB(self):
        return self.__teamB

    def getTeamAScore(self):
        return self.__teamAScore

    def getTeamBScore(self):
        return self.__teamBScore
