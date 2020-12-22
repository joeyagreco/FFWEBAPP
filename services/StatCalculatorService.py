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
        leagueModelNavigator = LeagueModelNavigator()
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
            gamesPlayed = leagueModelNavigator.gamesPlayedByTeam(leagueModel, teamId)
            # NOTE: if a team has played 0 games, the SSL calculations will have a DivisionByZero Error
            # this SHOULD not happen, because currently, a team has to play every week
            totalTeamPoints = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, teamId)
            totalLeaguePoints = leagueModelNavigator.totalLeaguePoints(leagueModel)
            sslCalculator = SslCalculator(awal, wal, totalTeamPoints, maxScore, minScore, gamesPlayed, totalLeaguePoints)
            teamScore = sslCalculator.getTeamScore()
            teamSuccess = sslCalculator.getTeamSuccess()
            teamLuck = sslCalculator.getTeamLuck()

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
                                       teamScore=teamScore,
                                       teamSuccess=teamSuccess,
                                       teamLuck=teamLuck)
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
        for i, teamId in enumerate(teamIds):
            opponentTeamId = teamIds[i-1]
            teamName = leagueModelNavigator.getTeamById(leagueModel, teamId).getTeamName()
            recordCalculator = RecordCalculator(teamId, leagueModel)
            wins = recordCalculator.getWinsVsTeam(opponentTeamId)
            losses = recordCalculator.getLossesVsTeam(opponentTeamId)
            ties = recordCalculator.getTiesVsTeam(opponentTeamId)
            winPercentage = recordCalculator.getWinPercentageVsTeam(opponentTeamId)
            ppgCalculator = PpgCalculator(teamId, leagueModel)
            ppg = ppgCalculator.getPpgVsTeam(opponentTeamId)
            scoresCalculator = ScoresCalculator(teamId, leagueModel)
            plusMinus = scoresCalculator.getPlusMinusVsTeam(opponentTeamId)
            stddev = scoresCalculator.getStandardDeviationVsTeam(opponentTeamId)
            maxScore = scoresCalculator.getMaxScoreVsTeam(opponentTeamId)
            minScore = scoresCalculator.getMinScoreVsTeam(opponentTeamId)
            awalCalculator = AwalCalculator(teamId, leagueModel, wins, ties)
            awal = awalCalculator.getAwalVsTeam(opponentTeamId)
            wal = awalCalculator.getWal()
            gamesPlayed = leagueModelNavigator.gamesPlayedByTeam(leagueModel, teamId)
            # NOTE: if a team has played 0 games, the SSL calculations will have a DivisionByZero Error
            # this SHOULD not happen, because currently, a team has to play every week
            totalTeamPoints = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, teamId)
            totalLeaguePoints = leagueModelNavigator.totalLeaguePoints(leagueModel)
            sslCalculator = SslCalculator(awal, wal, totalTeamPoints, maxScore, minScore, gamesPlayed, totalLeaguePoints)
            teamScore = sslCalculator.getTeamScore()
            teamSuccess = sslCalculator.getTeamSuccess()
            teamLuck = sslCalculator.getTeamLuck()
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
                                                        awal=awal,
                                                        teamScore=teamScore,
                                                        teamSuccess=teamSuccess,
                                                        teamLuck=teamLuck)
            statsModels.append(headToHeadStatsModel)
        return statsModels

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None
