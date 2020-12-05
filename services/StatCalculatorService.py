from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.ScoresCalculator import ScoresCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator
from packages.StatCalculators.SslCalculator import SslCalculator


class StatCalculatorService:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getTeamStats(self):
        """
        Returns a list of TeamStatsModels, one for each team in the given league.
        """
        for team in self.__leagueModel.getTeams():
            print(f"Team Name: {team.getTeamName()}")
            print(f"Team ID: {team.getTeamId()}")
            scoresCalculator = ScoresCalculator(team.getTeamId(), self.__leagueModel)
            maxScore = scoresCalculator.getMaxScore()
            minScore = scoresCalculator.getMinScore()
            print(f"Max Score: {maxScore}")
            print(f"Min Score: {minScore}")
            ppgCalculator = PpgCalculator(team.getTeamId(), self.__leagueModel)
            ppg = ppgCalculator.getPpg()
            print(f"PPG: {ppg}")
            ppgAgainst = ppgCalculator.getPpgAgainst()
            print(f"PPG Against: {ppgAgainst}")
            print(f"Plus/Minus: {scoresCalculator.getPlusMinus()}")
            print(f"Standard Deviation: {scoresCalculator.getStandardDeviation()}")
            recordCalculator = RecordCalculator(team.getTeamId(), self.__leagueModel)
            wins = recordCalculator.getWins()
            print(f"Wins: {wins}")
            print(f"Losses: {recordCalculator.getLosses()}")
            ties = recordCalculator.getTies()
            print(f"Ties: {ties}")
            print(f"Win %: {recordCalculator.getWinPercentage()}")
            awalCalculator = AwalCalculator(team.getTeamId(), self.__leagueModel, wins, ties)
            awal = awalCalculator.getAwal()
            wal = awalCalculator.getWal()
            print(f"AWAL: {awal}")
            print(f"WAL: {wal}")
            sslCalculator = SslCalculator(awal, wal, ppg, maxScore, minScore)
            rtsc = sslCalculator.getRawTeamScore()
            rtsu = sslCalculator.getRawTeamSuccess()
            rtl = sslCalculator.getRawTeamLuck()
            print(f"Raw Team Score: {rtsc}")
            print(f"Raw Team Success: {rtsu}")
            print(f"Raw Team Luck: {rtl}")
            print()

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None

