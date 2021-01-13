from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.headToHead_stat_models.HeadToHeadStatsModel import HeadToHeadStatsModel
from models.league_models.LeagueModel import LeagueModel
from models.league_stat_models.MarginOfVictoryModel import MarginOfVictoryModel
from models.league_stat_models.ScoreModel import ScoreModel
from models.team_stat_models.TeamStatsModel import TeamStatsModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.EveryGameCalculator import EveryGameCalculator
from packages.StatCalculators.ScoresCalculator import ScoresCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator
from packages.StatCalculators.SmartCalculator import SmartCalculator
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
            # everything above this has had the "week" kwarg changed to "throughWeek"
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
            # this SHOULD not happen, because currently, a team HAS to play every week
            totalTeamPoints = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, teamId)
            totalLeaguePoints = leagueModelNavigator.totalLeaguePoints(leagueModel)
            sslCalculator = SslCalculator(awal, wal, totalTeamPoints, maxScore, minScore, gamesPlayed, totalLeaguePoints)
            teamScore = sslCalculator.getTeamScore()
            teamSuccess = sslCalculator.getTeamSuccess()
            teamLuck = sslCalculator.getTeamLuck()
            allScores = leagueModelNavigator.getAllScoresOfTeam(leagueModel, teamId)
            smartCalculator = SmartCalculator(leagueModel)
            smartWins = smartCalculator.getSmartWinsOfScoresList(allScores)
            smartWinsStr = rounder.keepTrailingZeros(smartWins, 2)
            smartWinsAdjustment = smartCalculator.getSmartWinsAdjustmentOfScores(allScores, wal)
            smartWinsAdjustmentStr = rounder.keepTrailingZeros(smartWinsAdjustment, 2)
            percentageOfLeagueScoring = scoresCalculator.getPercentageOfLeagueScoring()
            percentageOfLeagueScoringStr = rounder.keepTrailingZeros(percentageOfLeagueScoring, 2)

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
            wins = recordCalculator.getWins(vsTeamIds=[opponentTeamId])
            losses = recordCalculator.getLosses(vsTeamIds=[opponentTeamId])
            ties = recordCalculator.getTies(vsTeamIds=[opponentTeamId])
            winPercentage = recordCalculator.getWinPercentage(vsTeamIds=[opponentTeamId])
            winPercentageStr = rounder.keepTrailingZeros(winPercentage, 3)
            ppgCalculator = PpgCalculator(teamId, leagueModel)
            ppg = ppgCalculator.getPpg(vsTeamIds=[opponentTeamId])
            ppgStr = rounder.keepTrailingZeros(ppg, decimalPlacesRoundedToScores)
            scoresCalculator = ScoresCalculator(teamId, leagueModel)
            plusMinus = scoresCalculator.getPlusMinus(vsTeamIds=[opponentTeamId])
            plusMinusStr = rounder.keepTrailingZeros(plusMinus, decimalPlacesRoundedToScores)
            stddev = scoresCalculator.getStandardDeviation(vsTeamIds=[opponentTeamId])
            stddevStr = rounder.keepTrailingZeros(stddev, 2)
            maxScore = scoresCalculator.getMaxScore(vsTeamIds=[opponentTeamId])
            maxScoreStr = rounder.keepTrailingZeros(maxScore, decimalPlacesRoundedToScores)
            minScore = scoresCalculator.getMinScore(vsTeamIds=[opponentTeamId])
            minScoreStr = rounder.keepTrailingZeros(minScore, decimalPlacesRoundedToScores)
            awalCalculator = AwalCalculator(teamId, leagueModel, wins, ties)
            awal = awalCalculator.getAwal(vsTeamIds=[opponentTeamId])
            wal = awalCalculator.getWal()
            gamesPlayed = leagueModelNavigator.gamesPlayedByTeam(leagueModel, teamId, vsTeamIds=[opponentTeamId])
            # NOTE: if a team has played 0 games, the SSL calculations will have a DivisionByZero Error
            # this SHOULD not happen, because currently, a team has to play every week
            totalTeamPoints = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, teamId, vsTeamIds=[opponentTeamId])
            allWeeksTeamsPlay = leagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, team1Id, [team2Id])
            totalLeaguePoints = leagueModelNavigator.totalLeaguePoints(leagueModel, onlyIncludeWeeks=allWeeksTeamsPlay)
            sslCalculator = SslCalculator(awal, wal, totalTeamPoints, maxScore, minScore, gamesPlayed, totalLeaguePoints)
            teamScore = sslCalculator.getTeamScore()
            teamSuccess = sslCalculator.getTeamSuccess()
            teamLuck = sslCalculator.getTeamLuck()
            allScores = leagueModelNavigator.getAllScoresOfTeam(leagueModel, teamId, vsTeamIds=[opponentTeamId])
            smartCalculator = SmartCalculator(leagueModel)
            smartWins = smartCalculator.getSmartWinsOfScoresList(allScores)
            smartWinsStr = rounder.keepTrailingZeros(smartWins, 2)
            smartWinsAdjustment = smartCalculator.getSmartWinsAdjustmentOfScores(allScores, wal)
            smartWinsAdjustmentStr = rounder.keepTrailingZeros(smartWinsAdjustment, 2)
            percentageOfLeagueScoring = scoresCalculator.getPercentageOfLeagueScoring(vsTeamIds=[opponentTeamId])
            percentageOfLeagueScoringStr = rounder.keepTrailingZeros(percentageOfLeagueScoring, 2)
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

    def getLeagueStats(self, leagueModel: LeagueModel, statSelection: str):
        """
        Returns a model/models for the given stat for self.__leagueModel.
        """
        statOptions = ["All Scores", "Margins of Victory"]
        rounder = Rounder()
        decimalPlacesForScores = rounder.getDecimalPlacesRoundedToInScores(leagueModel)
        everyGameCalculator = EveryGameCalculator(leagueModel)
        if statSelection not in statOptions:
            return None
        elif statSelection == "All Scores":
            allScores = everyGameCalculator.getAllScores()
            # sort from score high -> low
            allScores.sort(key=lambda x: x.getScore(), reverse=True)
            allScoresStr = []
            for scoreModel in allScores:
                score = scoreModel.getScore()
                score = rounder.keepTrailingZeros(score, decimalPlacesForScores)
                teamFor = scoreModel.getTeamFor()
                teamAgainst = scoreModel.getTeamAgainst()
                outcome = scoreModel.getOutcome()
                weekNumber = scoreModel.getWeek()
                newModel = ScoreModel(score, teamFor, teamAgainst, outcome, weekNumber)
                allScoresStr.append(newModel)
            return allScoresStr
        elif statSelection == "Margins of Victory":
            allMovs = everyGameCalculator.getAllMarginOfVictories()
            # sort from MOV high -> low
            allMovs.sort(key=lambda x: x.getMarginOfVictory(), reverse=True)
            allMovsStr = []
            for movModel in allMovs:
                mov = movModel.getMarginOfVictory()
                mov = rounder.keepTrailingZeros(mov, decimalPlacesForScores)
                teamFor = movModel.getWinningTeam()
                teamForPoints = movModel.getWinningTeamPoints()
                teamForPoints = rounder.keepTrailingZeros(teamForPoints, decimalPlacesForScores)
                teamAgainst = movModel.getLosingTeam()
                teamAgainstPoints = movModel.getLosingTeamPoints()
                teamAgainstPoints = rounder.keepTrailingZeros(teamAgainstPoints, decimalPlacesForScores)
                weekNumber = movModel.getWeek()
                newModel = MarginOfVictoryModel(mov, teamFor, teamForPoints, teamAgainst, teamAgainstPoints, weekNumber)
                allMovsStr.append(newModel)
            return allMovsStr

