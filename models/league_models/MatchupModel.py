from models.league_models.TeamModel import TeamModel


class MatchupModel:

    def __init__(self, matchupId: int, teamA: TeamModel, teamB: TeamModel, teamAScore: float, teamBScore: float):
        self.__matchupId = matchupId
        self.__teamA = teamA
        self.__teamB = teamB
        self.__teamAScore = teamAScore
        self.__teamBScore = teamBScore

    def getMatchupId(self):
        return self.__matchupId

    def getTeamA(self):
        return self.__teamA

    def getTeamB(self):
        return self.__teamB

    def getTeamAScore(self):
        return self.__teamAScore

    def getTeamBScore(self):
        return self.__teamBScore
