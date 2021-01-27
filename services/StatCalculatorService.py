from builders.GraphBuilder import GraphBuilder
from helpers.Constants import Constants
from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.headToHead_stat_models.HeadToHeadStatsModel import HeadToHeadStatsModel
from models.league_models.LeagueModel import LeagueModel
from models.league_stat_models.MarginOfVictoryModel import MarginOfVictoryModel
from models.league_stat_models.ScoreModel import ScoreModel
from models.team_stat_models.TeamStatsModel import TeamStatsModel
from packages.Exceptions.InvalidStatSelectionError import InvalidStatSelectionError
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.EveryGameCalculator import EveryGameCalculator
from packages.StatCalculators.ScoresCalculator import ScoresCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator
from packages.StatCalculators.SmartCalculator import SmartCalculator
from packages.StatCalculators.SslCalculator import SslCalculator


class StatCalculatorService:
    """
    This class connects stat calculators to the main Controller.
    It contains logic where the controller can/should not.
    """

    @staticmethod
    def getTeamStats(leagueModel: LeagueModel):
        """
        Returns a list of TeamStatsModels, one for each team in the given league.
        """
        teamStatsModels = []
        for team in leagueModel.getTeams():
            decimalPlacesRoundedToScores = Rounder.getDecimalPlacesRoundedToInScores(leagueModel)
            scoresCalculator = ScoresCalculator(team.getTeamId(), leagueModel)
            teamId = team.getTeamId()
            teamName = team.getTeamName()
            maxScore = scoresCalculator.getMaxScore()
            maxScoreStr = Rounder.keepTrailingZeros(maxScore, decimalPlacesRoundedToScores)
            minScore = scoresCalculator.getMinScore()
            minScoreStr = Rounder.keepTrailingZeros(minScore, decimalPlacesRoundedToScores)
            ppgCalculator = PpgCalculator(teamId, leagueModel)
            ppg = ppgCalculator.getPpg()
            ppgAgainst = ppgCalculator.getPpgAgainst()
            ppgStr = Rounder.keepTrailingZeros(ppg, decimalPlacesRoundedToScores)
            ppgAgainstStr = Rounder.keepTrailingZeros(ppgAgainst, decimalPlacesRoundedToScores)
            plusMinus = scoresCalculator.getPlusMinus()
            plusMinusStr = Rounder.keepTrailingZeros(plusMinus, decimalPlacesRoundedToScores)
            stddev = scoresCalculator.getStandardDeviation()
            stddevStr = Rounder.keepTrailingZeros(stddev, 2)
            recordCalculator = RecordCalculator(teamId, leagueModel)
            wins = recordCalculator.getWins()
            losses = recordCalculator.getLosses()
            ties = recordCalculator.getTies()
            winPercentage = recordCalculator.getWinPercentage()
            winPercentageStr = Rounder.keepTrailingZeros(winPercentage, 3)
            awalCalculator = AwalCalculator(teamId, leagueModel, wins, ties)
            awal = awalCalculator.getAwal()
            wal = awalCalculator.getWal()
            gamesPlayed = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, teamId)
            # NOTE: if a team has played 0 games, the SSL calculations will have a DivisionByZero Error
            # this SHOULD not happen, because currently, a team HAS to play every week
            totalTeamPoints = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, teamId)
            totalLeaguePoints = LeagueModelNavigator.totalLeaguePoints(leagueModel)
            sslCalculator = SslCalculator(awal, wal, totalTeamPoints, maxScore, minScore, gamesPlayed, totalLeaguePoints)
            teamScore = sslCalculator.getTeamScore()
            teamSuccess = sslCalculator.getTeamSuccess()
            teamLuck = sslCalculator.getTeamLuck()
            allScores = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, teamId)
            smartCalculator = SmartCalculator(leagueModel)
            smartWins = smartCalculator.getSmartWinsOfScoresList(allScores)
            smartWinsStr = Rounder.keepTrailingZeros(smartWins, 2)
            smartWinsAdjustment = smartCalculator.getSmartWinsAdjustmentOfScores(allScores, wal)
            smartWinsAdjustmentStr = Rounder.keepTrailingZeros(smartWinsAdjustment, 2)
            percentageOfLeagueScoring = scoresCalculator.getPercentageOfLeagueScoring()
            percentageOfLeagueScoringStr = Rounder.keepTrailingZeros(percentageOfLeagueScoring, 2)

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
                                       teamLuck=teamLuck,
                                       smartWins=smartWinsStr,
                                       smartWinsAdjustment=smartWinsAdjustmentStr,
                                       percentageOfLeagueScoring=percentageOfLeagueScoringStr)
            teamStatsModels.append(teamModel)
        # sort from win percentage high -> low
        teamStatsModels.sort(key=lambda x: x.getWinPercentage(), reverse=True)
        return teamStatsModels

    @staticmethod
    def getHeadToHeadStats(leagueModel: LeagueModel, team1Id: int, team2Id: int):
        """
        Returns 2 HeadToHeadStatsModels in a list for the teams with the given IDs.
        """
        teamIds = (team1Id, team2Id)
        statsModels = []
        for i, teamId in enumerate(teamIds):
            opponentTeamId = teamIds[i - 1]
            decimalPlacesRoundedToScores = Rounder.getDecimalPlacesRoundedToInScores(leagueModel)
            teamName = LeagueModelNavigator.getTeamById(leagueModel, teamId).getTeamName()
            recordCalculator = RecordCalculator(teamId, leagueModel)
            wins = recordCalculator.getWins(vsTeamIds=[opponentTeamId])
            losses = recordCalculator.getLosses(vsTeamIds=[opponentTeamId])
            ties = recordCalculator.getTies(vsTeamIds=[opponentTeamId])
            winPercentage = recordCalculator.getWinPercentage(vsTeamIds=[opponentTeamId])
            winPercentageStr = Rounder.keepTrailingZeros(winPercentage, 3)
            ppgCalculator = PpgCalculator(teamId, leagueModel)
            ppg = ppgCalculator.getPpg(vsTeamIds=[opponentTeamId])
            ppgStr = Rounder.keepTrailingZeros(ppg, decimalPlacesRoundedToScores)
            scoresCalculator = ScoresCalculator(teamId, leagueModel)
            plusMinus = scoresCalculator.getPlusMinus(vsTeamIds=[opponentTeamId])
            plusMinusStr = Rounder.keepTrailingZeros(plusMinus, decimalPlacesRoundedToScores)
            stddev = scoresCalculator.getStandardDeviation(vsTeamIds=[opponentTeamId])
            stddevStr = Rounder.keepTrailingZeros(stddev, 2)
            maxScore = scoresCalculator.getMaxScore(vsTeamIds=[opponentTeamId])
            maxScoreStr = Rounder.keepTrailingZeros(maxScore, decimalPlacesRoundedToScores)
            minScore = scoresCalculator.getMinScore(vsTeamIds=[opponentTeamId])
            minScoreStr = Rounder.keepTrailingZeros(minScore, decimalPlacesRoundedToScores)
            awalCalculator = AwalCalculator(teamId, leagueModel, wins, ties)
            awal = awalCalculator.getAwal(vsTeamIds=[opponentTeamId])
            wal = awalCalculator.getWal()
            gamesPlayed = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, teamId, vsTeamIds=[opponentTeamId])
            # NOTE: if a team has played 0 games, the SSL calculations will have a DivisionByZero Error
            # this SHOULD not happen, because currently, a team has to play every week
            totalTeamPoints = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, teamId, vsTeamIds=[opponentTeamId])
            allWeeksTeamsPlay = LeagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, team1Id, [team2Id])
            totalLeaguePoints = LeagueModelNavigator.totalLeaguePoints(leagueModel, onlyIncludeWeeks=allWeeksTeamsPlay)
            sslCalculator = SslCalculator(awal, wal, totalTeamPoints, maxScore, minScore, gamesPlayed, totalLeaguePoints)
            teamScore = sslCalculator.getTeamScore()
            teamSuccess = sslCalculator.getTeamSuccess()
            teamLuck = sslCalculator.getTeamLuck()
            allScores = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, teamId, vsTeamIds=[opponentTeamId])
            smartCalculator = SmartCalculator(leagueModel)
            smartWins = smartCalculator.getSmartWinsOfScoresList(allScores)
            smartWinsStr = Rounder.keepTrailingZeros(smartWins, 2)
            smartWinsAdjustment = smartCalculator.getSmartWinsAdjustmentOfScores(allScores, wal)
            smartWinsAdjustmentStr = Rounder.keepTrailingZeros(smartWinsAdjustment, 2)
            percentageOfLeagueScoring = scoresCalculator.getPercentageOfLeagueScoring(vsTeamIds=[opponentTeamId])
            percentageOfLeagueScoringStr = Rounder.keepTrailingZeros(percentageOfLeagueScoring, 2)
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
                                                        teamLuck=teamLuck,
                                                        smartWins=smartWinsStr,
                                                        smartWinsAdjustment=smartWinsAdjustmentStr,
                                                        percentageOfLeagueScoring=percentageOfLeagueScoringStr)
            statsModels.append(headToHeadStatsModel)
        return statsModels

    @staticmethod
    def getLeagueStats(leagueModel: LeagueModel, statSelection: str):
        """
        Returns a model/models for the given stat for self.__leagueModel.
        """
        statOptions = Constants.STAT_OPTIONS
        decimalPlacesForScores = Rounder.getDecimalPlacesRoundedToInScores(leagueModel)
        everyGameCalculator = EveryGameCalculator(leagueModel)
        if statSelection not in statOptions:
            raise InvalidStatSelectionError(f"Unknown League Stat: {statSelection}.")
        elif statSelection == Constants.ALL_SCORES:
            allScores = everyGameCalculator.getAllScores()
            # sort from score high -> low
            allScores.sort(key=lambda x: x.getScore(), reverse=True)
            allScoresStr = []
            for scoreModel in allScores:
                score = scoreModel.getScore()
                score = Rounder.keepTrailingZeros(score, decimalPlacesForScores)
                teamFor = scoreModel.getTeamFor()
                teamAgainst = scoreModel.getTeamAgainst()
                outcome = scoreModel.getOutcome()
                weekNumber = scoreModel.getWeek()
                newModel = ScoreModel(score=score,
                                      teamFor=teamFor,
                                      teamAgainst=teamAgainst,
                                      outcome=outcome,
                                      week=weekNumber)
                allScoresStr.append(newModel)
            return allScoresStr
        elif statSelection == Constants.MARGINS_OF_VICTORY:
            allMovs = everyGameCalculator.getAllMarginOfVictories()
            # sort from MOV high -> low
            allMovs.sort(key=lambda x: x.getMarginOfVictory(), reverse=True)
            allMovsStr = []
            for movModel in allMovs:
                mov = movModel.getMarginOfVictory()
                mov = Rounder.keepTrailingZeros(mov, decimalPlacesForScores)
                teamFor = movModel.getWinningTeam()
                teamForPoints = movModel.getWinningTeamPoints()
                teamForPoints = Rounder.keepTrailingZeros(teamForPoints, decimalPlacesForScores)
                teamAgainst = movModel.getLosingTeam()
                teamAgainstPoints = movModel.getLosingTeamPoints()
                teamAgainstPoints = Rounder.keepTrailingZeros(teamAgainstPoints, decimalPlacesForScores)
                weekNumber = movModel.getWeek()
                newModel = MarginOfVictoryModel(marginOfVictory=mov,
                                                winningTeam=teamFor,
                                                winningTeamPoints=teamForPoints,
                                                losingTeam=teamAgainst,
                                                losingTeamPoints=teamAgainstPoints,
                                                week=weekNumber)
                allMovsStr.append(newModel)
            return allMovsStr

    @staticmethod
    def getGraphDiv(leagueModel: LeagueModel, screenWidth: float, graphSelection: str):
        if graphSelection == Constants.PPG_BY_WEEK:
            return GraphBuilder.getHtmlForPpg(leagueModel, screenWidth)
        elif graphSelection == Constants.SCORING_SHARE:
            return GraphBuilder.getHtmlForScoringShare(leagueModel, screenWidth)
        elif graphSelection == Constants.AWAL_OVER_PPG:
            return GraphBuilder.getHtmlForAwalOverPpg(leagueModel, screenWidth)
        elif graphSelection == Constants.FREQUENCY_OF_SCORES:
            return GraphBuilder.getHtmlForFrequencyOfScores(leagueModel, screenWidth)
        elif graphSelection == Constants.POINTS_FOR_OVER_POINTS_AGAINST:
            return GraphBuilder.getHtmlForPointsOverPointsAgainst(leagueModel, screenWidth)
        else:
            # TODO decide what to return here
            return "..."


