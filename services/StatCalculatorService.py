from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
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
            rounder = Rounder()
            decimalPlacesRoundedToScores = rounder.getDecimalPlacesRoundedToInScores(leagueModel)
            scoresCalculator = ScoresCalculator(team.getTeamId(), leagueModel)
            teamId = team.getTeamId()
            teamName = team.getTeamName()
            maxScore = scoresCalculator.getMaxScore()
            maxScoreStr = rounder.keepTrailingZeros(maxScore, decimalPlacesRoundedToScores)
            minScore = scoresCalculator.getMinScore()
            minScoreStr = rounder.keepTrailingZeros(minScore, decimalPlacesRoundedToScores)
            ppgCalculator = PpgCalculator(teamId, leagueModel)
            ppg = ppgCalculator.getPpg()
            ppgAgainst = ppgCalculator.getPpgAgainst()
            ppgStr = rounder.keepTrailingZeros(ppg, decimalPlacesRoundedToScores)
            ppgAgainstStr = rounder.keepTrailingZeros(ppgAgainst, decimalPlacesRoundedToScores)
            plusMinus = scoresCalculator.getPlusMinus()
            plusMinusStr = rounder.keepTrailingZeros(plusMinus, decimalPlacesRoundedToScores)
            stddev = scoresCalculator.getStandardDeviation()
            stddevStr = rounder.keepTrailingZeros(stddev, 2)
            recordCalculator = RecordCalculator(teamId, leagueModel)
            wins = recordCalculator.getWins()
            losses = recordCalculator.getLosses()
            ties = recordCalculator.getTies()
            winPercentage = recordCalculator.getWinPercentage()
            winPercentageStr = rounder.keepTrailingZeros(winPercentage, 3)
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
                                       winPercentage=winPercentageStr,
                                       ppg=ppgStr,
                                       ppgAgainst=ppgAgainstStr,
                                       plusMinus=plusMinusStr,
                                       stddev=stddevStr,
                                       maxScore=maxScoreStr,
                                       minScore=minScoreStr,
                                       awal=awal,
                                       teamScore=teamScore,
                                       teamSuccess=teamSuccess,
                                       teamLuck=teamLuck)
            teamStatsModels.append(teamModel)
        return teamStatsModels

    def getHeadToHeadStats(self, leagueModel: LeagueModel, team1Id: int, team2Id: int):
        """
        Returns 2 HeadToHeadStatsModels in a list for the teams with the given IDs.
        """
        teamIds = (team1Id, team2Id)
        statsModels = []
        leagueModelNavigator = LeagueModelNavigator()
        for i, teamId in enumerate(teamIds):
            opponentTeamId = teamIds[i - 1]
            rounder = Rounder()
            decimalPlacesRoundedToScores = rounder.getDecimalPlacesRoundedToInScores(leagueModel)
            teamName = leagueModelNavigator.getTeamById(leagueModel, teamId).getTeamName()
            recordCalculator = RecordCalculator(teamId, leagueModel)
            wins = recordCalculator.getWinsVsTeam(opponentTeamId)
            losses = recordCalculator.getLossesVsTeam(opponentTeamId)
            ties = recordCalculator.getTiesVsTeam(opponentTeamId)
            winPercentage = recordCalculator.getWinPercentageVsTeam(opponentTeamId)
            winPercentageStr = rounder.keepTrailingZeros(winPercentage, 3)
            ppgCalculator = PpgCalculator(teamId, leagueModel)
            ppg = ppgCalculator.getPpgVsTeam(opponentTeamId)
            ppgStr = rounder.keepTrailingZeros(ppg, decimalPlacesRoundedToScores)
            scoresCalculator = ScoresCalculator(teamId, leagueModel)
            plusMinus = scoresCalculator.getPlusMinusVsTeam(opponentTeamId)
            plusMinusStr = rounder.keepTrailingZeros(plusMinus, decimalPlacesRoundedToScores)
            stddev = scoresCalculator.getStandardDeviationVsTeam(opponentTeamId)
            stddevStr = rounder.keepTrailingZeros(stddev, 2)
            maxScore = scoresCalculator.getMaxScoreVsTeam(opponentTeamId)
            maxScoreStr = rounder.keepTrailingZeros(maxScore, decimalPlacesRoundedToScores)
            minScore = scoresCalculator.getMinScoreVsTeam(opponentTeamId)
            minScoreStr = rounder.keepTrailingZeros(minScore, decimalPlacesRoundedToScores)
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
                                                        winPercentage=winPercentageStr,
                                                        ppg=ppgStr,
                                                        plusMinus=plusMinusStr,
                                                        stddev=stddevStr,
                                                        maxScore=maxScoreStr,
                                                        minScore=minScoreStr,
                                                        awal=awal,
                                                        teamScore=teamScore,
                                                        teamSuccess=teamSuccess,
                                                        teamLuck=teamLuck)
            statsModels.append(headToHeadStatsModel)
        return statsModels

    def getLeagueStats(self, leagueModel: LeagueModel, statSelection: str):
        """
        Returns a model for the given stat for self.__leagueModel.
        """
        return None
