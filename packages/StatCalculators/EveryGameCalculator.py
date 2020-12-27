from models.league_models.LeagueModel import LeagueModel


class EveryGameCalculator:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel