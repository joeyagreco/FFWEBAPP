from models.league_models.LeagueModel import LeagueModel


class SmartCalculator:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getPercentileOfScore(self, score: float):
        """
        Returns the percentile of which this score would rank in self.__leagueModel.
        Note: This assumes that the given score already exists in self.__leagueModel.
        """
        scoresBeat = 0
        scoresTied = 0
        totalScores = 0

        return None
