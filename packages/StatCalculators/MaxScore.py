from models.league_models.LeagueModel import LeagueModel


class MaxScore:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel

    def getMaxScore(self):
        pass