from models.league_models.TeamModel import TeamModel


class ScoreModel:

    def __init__(self, score: float, teamFor: TeamModel, teamAgainst: TeamModel, outcome: str, week: int):
        self.__score = score
        self.__teamFor = teamFor
        self.__teamAgainst = teamAgainst
        self.__outcome = outcome
        self.__week = week

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
