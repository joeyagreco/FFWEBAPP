from models.league_models.LeagueModel import LeagueModel
from models.team_stat_models.TeamStatsModel import TeamStatsModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.ScoresCalculator import ScoresCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator
from packages.StatCalculators.SslCalculator import SslCalculator


class StatCalculatorService:

    def __init__(self):
        pass

    def getTeamStats(self, leagueModel: LeagueModel):
        """
        Returns a list of TeamStatsModels, one for each team in the given league.
        """
        teamStatModels = []
        for team in leagueModel.getTeams():
            scoresCalculator = ScoresCalculator(team.getTeamId(), leagueModel)
            teamId = team.getTeamId()
            teamName = team.getTeamName()
            maxScore = scoresCalculator.getMaxScore()
            minScore = scoresCalculator.getMinScore()
            ppgCalculator = PpgCalculator(teamId, leagueModel)
            ppg = ppgCalculator.getPpg()
            ppgAgainst = ppgCalculator.getPpgAgainst()
            plusMinus = scoresCalculator.getPlusMinus()
            stddev = scoresCalculator.getStandardDeviation()
            recordCalculator = RecordCalculator(teamId, leagueModel)
            wins = recordCalculator.getWins()
            losses = recordCalculator.getLosses()
            ties = recordCalculator.getTies()
            winPercentage = recordCalculator.getWinPercentage()
            awalCalculator = AwalCalculator(teamId, leagueModel, wins, ties)
            awal = awalCalculator.getAwal()
            wal = awalCalculator.getWal()
            sslCalculator = SslCalculator(awal, wal, ppg, maxScore, minScore)
            rawTeamScore = sslCalculator.getRawTeamScore()
            rawTeamSuccess = sslCalculator.getRawTeamSuccess()
            rawTeamLuck = sslCalculator.getRawTeamLuck()

            teamModel = TeamStatsModel(teamId=teamId,
                                       teamName=teamName,
                                       wins=wins,
                                       losses=losses,
                                       ties=ties,
                                       winPercentage=winPercentage,
                                       ppg=ppg,
                                       ppgAgainst=ppgAgainst,
                                       plusMinus=plusMinus,
                                       stddev=stddev,
                                       maxScore=maxScore,
                                       minScore=minScore,
                                       awal=awal,
                                       rawTeamScore=rawTeamScore,
                                       rawTeamSuccess=rawTeamSuccess,
                                       rawTeamLuck=rawTeamLuck)
            teamStatModels.append(teamModel)
        return teamStatModels

            # print(f"Team ID: {team.getTeamId()}")
            # print(f"Team Name: {team.getTeamName()}")
            # scoresCalculator = ScoresCalculator(team.getTeamId(), leagueModel)
            # maxScore = scoresCalculator.getMaxScore()
            # minScore = scoresCalculator.getMinScore()
            # print(f"Max Score: {maxScore}")
            # print(f"Min Score: {minScore}")
            # ppgCalculator = PpgCalculator(team.getTeamId(), leagueModel)
            # ppg = ppgCalculator.getPpg()
            # print(f"PPG: {ppg}")
            # ppgAgainst = ppgCalculator.getPpgAgainst()
            # print(f"PPG Against: {ppgAgainst}")
            # print(f"Plus/Minus: {scoresCalculator.getPlusMinus()}")
            # print(f"Standard Deviation: {scoresCalculator.getStandardDeviation()}")
            # recordCalculator = RecordCalculator(team.getTeamId(), leagueModel)
            # wins = recordCalculator.getWins()
            # print(f"Wins: {wins}")
            # print(f"Losses: {recordCalculator.getLosses()}")
            # ties = recordCalculator.getTies()
            # print(f"Ties: {ties}")
            # print(f"Win %: {recordCalculator.getWinPercentage()}")
            # awalCalculator = AwalCalculator(team.getTeamId(), leagueModel, wins, ties)
            # awal = awalCalculator.getAwal()
            # wal = awalCalculator.getWal()
            # print(f"AWAL: {awal}")
            # print(f"WAL: {wal}")
            # sslCalculator = SslCalculator(awal, wal, ppg, maxScore, minScore)
            # rtsc = sslCalculator.getRawTeamScore()
            # rtsu = sslCalculator.getRawTeamSuccess()
            # rtl = sslCalculator.getRawTeamLuck()
            # print(f"Raw Team Score: {rtsc}")
            # print(f"Raw Team Success: {rtsu}")
            # print(f"Raw Team Luck: {rtl}")
            # print()

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None
