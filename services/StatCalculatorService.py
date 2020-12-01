from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
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
            wins = recordCalculator.getWins()
            print(f"Wins: {wins}")
            print(f"Losses: {recordCalculator.getLosses()}")
            ties = recordCalculator.getTies()
            print(f"Ties: {ties}")
            print(f"Win %: {recordCalculator.getWinPercentage()}")
            print(f"Plus/Minus: {scoresCalculator.getPlusMinus()}")
            print(f"Standard Deviation: {scoresCalculator.getStandardDeviation()}")
            awalCalculator = AwalCalculator(team.getTeamId(), self.__leagueModel, wins, ties)
            print(f"AWAL: {awalCalculator.getAwal()}")
            print()

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None

