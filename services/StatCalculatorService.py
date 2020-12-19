from helpers.Error import Error
from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.headToHead_stat_models.HeadToHeadStatsModel import HeadToHeadStatsModel
from models.league_models.LeagueModel import LeagueModel
from models.team_stat_models.TeamStatsModel import TeamStatsModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.ScoresCalculator import ScoresCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator
from packages.StatCalculators.SslCalculator import SslCalculator
from packages.Verifiers.StatVerifier import StatVerifier


class StatCalculatorService:

    def __init__(self):
        self.__statVerifier = StatVerifier()

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

    def getHeadToHeadStats(self, leagueModel: LeagueModel, team1Id: int, team2Id: int):
        """
        Returns 2 HeadToHeadStatsModels for the teams with the given IDs.
        """
        if self.__statVerifier.comparingSameHeadToHeadTeam(team1Id, team2Id):
            return Error("Cannot compare a team to itself.")

        teamIds = (team1Id, team2Id)
        statsModels = []
        leagueModelNavigator = LeagueModelNavigator()
        for teamId in teamIds:
            teamName = leagueModelNavigator.getTeamById(leagueModel, teamId).getTeamName()
            # stats calculated below this line are not correct yet
            recordCalculator = RecordCalculator(teamId, leagueModel)
            wins = recordCalculator.getWins()
            losses = recordCalculator.getLosses()
            ties = recordCalculator.getTies()
            winPercentage = recordCalculator.getWinPercentage()
            ppgCalculator = PpgCalculator(teamId, leagueModel)
            ppg = ppgCalculator.getPpg()
            scoresCalculator = ScoresCalculator(teamId, leagueModel)
            plusMinus = scoresCalculator.getPlusMinus()
            stddev = scoresCalculator.getStandardDeviation()
            maxScore = scoresCalculator.getMaxScore()
            minScore = scoresCalculator.getMinScore()
            awalCalculator = AwalCalculator(teamId, leagueModel, wins, ties)
            awal = awalCalculator.getAwal()
            headToHeadStatsModel = HeadToHeadStatsModel(teamId=teamId,
                                                        teamName=teamName,
                                                        wins=wins,
                                                        losses=losses,
                                                        ties=ties,
                                                        winPercentage=winPercentage,
                                                        ppg=ppg,
                                                        plusMinus=plusMinus,
                                                        stddev=stddev,
                                                        maxScore=maxScore,
                                                        minScore=minScore,
                                                        awal=awal)
            statsModels.append(headToHeadStatsModel)
        return statsModels

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None
