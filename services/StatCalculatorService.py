from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.ScoresCalculator import ScoresCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator


class StatCalculatorService:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getTeamStats(self):
        """
        Returns a list of TeamStatsModels, one for each team in the given league.
        """
        for team in self.__leagueModel.getTeams():
            print(f"Team ID: {team.getTeamId()}")
            scoresCalculator = ScoresCalculator(team.getTeamId(), self.__leagueModel)
            print(f"Min Score: {scoresCalculator.getMinScore()}")
            print(f"Max Score: {scoresCalculator.getMaxScore()}")
            ppgCalculator = PpgCalculator(team.getTeamId(), self.__leagueModel)
            print(f"PPG: {ppgCalculator.getPpg()}")
            recordCalculator = RecordCalculator(team.getTeamId(), self.__leagueModel)
            print(f"Wins: {recordCalculator.getWins()}")
            print(f"Losses: {recordCalculator.getLosses()}")
            print(f"Ties: {recordCalculator.getTies()}")
            print(f"Plus/Minus: {scoresCalculator.getPlusMinus()}")
            print()

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None

