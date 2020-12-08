from models.league_models.LeagueModel import LeagueModel
from models.team_stat_models.TeamStatsModel import TeamStatsModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.ScoresCalculator import ScoresCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator
from packages.StatCalculators.SslCalculator import SslCalculator


class StatCalculatorService:

    def getTeamStats(self, leagueModel: LeagueModel):
        """
        Returns a list of TeamStatsModels, one for each team in the given league.
        """
        teamStatsModels = []
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
            teamStatsModels.append(teamModel)
        return teamStatsModels

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None
