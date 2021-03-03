from models.league_models.LeagueModel import LeagueModel


class StreakCalculator:

    def __init__(self, leagueModel: LeagueModel, teamId: int, years: list):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__years = years

