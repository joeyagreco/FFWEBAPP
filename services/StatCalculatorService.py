from typing import List

from builders.GraphBuilder import GraphBuilder
from helpers.Constants import Constants
from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.headToHead_stat_models.HeadToHeadStatsModel import HeadToHeadStatsModel
from models.league_models.LeagueModel import LeagueModel
from models.league_stat_models.MarginOfVictoryModel import MarginOfVictoryModel
from models.league_stat_models.OwnerComparisonModel import OwnerComparisonModel
from models.league_stat_models.ScoreModel import ScoreModel
from models.team_stat_models.TeamStatsModel import TeamStatsModel
from packages.Exceptions.InvalidStatSelectionError import InvalidStatSelectionError
from packages.StatCalculators.AverageCalculator import AverageCalculator
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.EveryGameCalculator import EveryGameCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator
from packages.StatCalculators.ScoresCalculator import ScoresCalculator
from packages.StatCalculators.SmartCalculator import SmartCalculator
from packages.StatCalculators.SslCalculator import SslCalculator
from packages.StatCalculators.StreakCalculator import StreakCalculator
from packages.StatCalculators.StrengthOfScheduleCalculator import StrengthOfScheduleCalculator


class StatCalculatorService:
    """
    This class connects stat calculators to the main Controller.
    It contains logic where the controller can/should not.
    """

    @staticmethod
    def getTeamStats(leagueModel: LeagueModel, years: list) -> List[TeamStatsModel]:
        """
        Returns a list of TeamStatsModels, one for each team in the given league in the given year.
        """
        teamStatsModels = []
        for year in years:
            for team in leagueModel.getYears()[str(year)].getTeams():
                yearAsList = [year]
                decimalPlacesRoundedToScores = Rounder.getDecimalPlacesRoundedToInScores(leagueModel)
                teamId = team.getTeamId()
                teamName = team.getTeamName()
                scoresCalculator = ScoresCalculator(team.getTeamId(), leagueModel, yearAsList)
                maxScore = scoresCalculator.getMaxScore()
                maxScoreStr = Rounder.keepTrailingZeros(maxScore, decimalPlacesRoundedToScores)
                minScore = scoresCalculator.getMinScore()
                minScoreStr = Rounder.keepTrailingZeros(minScore, decimalPlacesRoundedToScores)
                ppgCalculator = PpgCalculator(teamId, leagueModel, yearAsList)
                ppg = ppgCalculator.getPpg()
                ppgAgainst = ppgCalculator.getPpgAgainst()
                ppgStr = Rounder.keepTrailingZeros(ppg, decimalPlacesRoundedToScores)
                ppgAgainstStr = Rounder.keepTrailingZeros(ppgAgainst, decimalPlacesRoundedToScores)
                plusMinus = scoresCalculator.getPlusMinus()
                plusMinusStr = Rounder.keepTrailingZeros(plusMinus, decimalPlacesRoundedToScores)
                stddev = scoresCalculator.getStandardDeviation()
                stddevStr = Rounder.keepTrailingZeros(stddev, 2)
                recordCalculator = RecordCalculator(teamId, leagueModel, yearAsList)
                wins = recordCalculator.getWins()
                losses = recordCalculator.getLosses()
                ties = recordCalculator.getTies()
                winPercentage = recordCalculator.getWinPercentage()
                winPercentageStr = Rounder.keepTrailingZeros(winPercentage, 3)
                awalCalculator = AwalCalculator(teamId, leagueModel, yearAsList, wins, ties)
                awal = awalCalculator.getAwal()
                awalStr = Rounder.keepTrailingZeros(awal, 2)
                wal = awalCalculator.getWal()
                walStr = Rounder.keepTrailingZeros(wal, 2)
                awalPerGame = awalCalculator.getAwalPerGame()
                awalPerGameStr = Rounder.keepTrailingZeros(awalPerGame, 2)
                gamesPlayed = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, yearAsList, teamId)
                # NOTE: if a team has played 0 games, the SSL calculations will have a DivisionByZero Error
                # this SHOULD not happen, because currently, a team HAS to play every week
                scoringShare = scoresCalculator.getScoringShare()
                scoringShareStr = Rounder.keepTrailingZeros(scoringShare, 2)
                scoringShareAgainst = scoresCalculator.getScoringShareAgainst()
                scoringShareAgainstStr = Rounder.keepTrailingZeros(scoringShareAgainst, 2)
                sslCalculator = SslCalculator(awal, wal, scoringShare, maxScore, minScore, gamesPlayed)
                teamScore = sslCalculator.getTeamScore()
                teamScoreStr = Rounder.keepTrailingZeros(teamScore, 2)
                teamSuccess = sslCalculator.getTeamSuccess()
                teamSuccessStr = Rounder.keepTrailingZeros(teamSuccess, 2)
                teamLuck = sslCalculator.getTeamLuck()
                teamLuckStr = Rounder.keepTrailingZeros(teamLuck, 2)
                allScores = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, yearAsList, teamId)
                smartCalculator = SmartCalculator(leagueModel, yearAsList)
                smartWins = smartCalculator.getSmartWinsOfScoresList(allScores)
                smartWinsStr = Rounder.keepTrailingZeros(smartWins, 2)
                strengthOfScheduleCalculator = StrengthOfScheduleCalculator(teamId, leagueModel, yearAsList)
                strengthOfSchedule = strengthOfScheduleCalculator.getStrengthOfSchedule()
                strengthOfScheduleStr = Rounder.keepTrailingZeros(strengthOfSchedule, 3)

                teamModel = TeamStatsModel(teamId=teamId,
                                           year=year,
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
                                           awal=awalStr,
                                           teamScore=teamScoreStr,
                                           teamSuccess=teamSuccessStr,
                                           teamLuck=teamLuckStr,
                                           smartWins=smartWinsStr,
                                           scoringShare=scoringShareStr,
                                           strengthOfSchedule=strengthOfScheduleStr,
                                           wal=walStr,
                                           scoringShareAgainst=scoringShareAgainstStr,
                                           awalPerGame=awalPerGameStr)
                teamStatsModels.append(teamModel)
        # sort from win percentage high -> low
        teamStatsModels.sort(key=lambda x: x.getWinPercentage(), reverse=True)
        return teamStatsModels

    @staticmethod
    def getHeadToHeadStats(leagueModel: LeagueModel, years: list, team1Id: int, team2Id: int) -> List[
        HeadToHeadStatsModel]:
        """
        Returns 2 HeadToHeadStatsModels in a list for the teams with the given IDs in the given league in the given year.
        """
        if len(years) > 1:
            year = "0"
        else:
            year = years[0]
        teamIds = (team1Id, team2Id)
        statsModels = []
        for i, teamId in enumerate(teamIds):
            opponentTeamId = teamIds[i - 1]
            decimalPlacesRoundedToScores = Rounder.getDecimalPlacesRoundedToInScores(leagueModel)
            teamName = LeagueModelNavigator.getTeamById(leagueModel, year, teamId).getTeamName()
            recordCalculator = RecordCalculator(teamId, leagueModel, years)
            wins = recordCalculator.getWins(vsTeamIds=[opponentTeamId])
            losses = recordCalculator.getLosses(vsTeamIds=[opponentTeamId])
            ties = recordCalculator.getTies(vsTeamIds=[opponentTeamId])
            winPercentage = recordCalculator.getWinPercentage(vsTeamIds=[opponentTeamId])
            winPercentageStr = Rounder.keepTrailingZeros(winPercentage, 3)
            ppgCalculator = PpgCalculator(teamId, leagueModel, years)
            ppg = ppgCalculator.getPpg(vsTeamIds=[opponentTeamId])
            ppgStr = Rounder.keepTrailingZeros(ppg, decimalPlacesRoundedToScores)
            scoresCalculator = ScoresCalculator(teamId, leagueModel, years)
            plusMinus = scoresCalculator.getPlusMinus(vsTeamIds=[opponentTeamId])
            plusMinusStr = Rounder.keepTrailingZeros(plusMinus, decimalPlacesRoundedToScores)
            stddev = scoresCalculator.getStandardDeviation(vsTeamIds=[opponentTeamId])
            stddevStr = Rounder.keepTrailingZeros(stddev, 2)
            maxScore = scoresCalculator.getMaxScore(vsTeamIds=[opponentTeamId])
            maxScoreStr = Rounder.keepTrailingZeros(maxScore, decimalPlacesRoundedToScores)
            minScore = scoresCalculator.getMinScore(vsTeamIds=[opponentTeamId])
            minScoreStr = Rounder.keepTrailingZeros(minScore, decimalPlacesRoundedToScores)
            awalCalculator = AwalCalculator(teamId, leagueModel, years, wins, ties)
            awal = awalCalculator.getAwal(vsTeamIds=[opponentTeamId])
            awalStr = Rounder.keepTrailingZeros(awal, 2)
            wal = awalCalculator.getWal()
            walStr = Rounder.keepTrailingZeros(wal, 2)
            awalPerGame = awalCalculator.getAwalPerGame(vsTeamIds=[opponentTeamId])
            awalPerGameStr = Rounder.keepTrailingZeros(awalPerGame, 2)
            gamesPlayed = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, years, teamId, vsTeamIds=[opponentTeamId])
            # NOTE: if a team has played 0 games, the SSL calculations will have a DivisionByZero Error
            # this SHOULD not happen, because currently, a team has to play every week
            scoringShare = scoresCalculator.getScoringShare(vsTeamIds=[opponentTeamId])
            scoringShareStr = Rounder.keepTrailingZeros(scoringShare, 2)
            sslCalculator = SslCalculator(awal, wal, scoringShare, maxScore, minScore, gamesPlayed)
            teamScore = sslCalculator.getTeamScore()
            teamScoreStr = Rounder.keepTrailingZeros(teamScore, 2)
            teamSuccess = sslCalculator.getTeamSuccess()
            teamSuccessStr = Rounder.keepTrailingZeros(teamSuccess, 2)
            teamLuck = sslCalculator.getTeamLuck()
            teamLuckStr = Rounder.keepTrailingZeros(teamLuck, 2)
            allScores = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, years, teamId, vsTeamIds=[opponentTeamId])
            smartCalculator = SmartCalculator(leagueModel, years)
            smartWins = smartCalculator.getSmartWinsOfScoresList(allScores)
            smartWinsStr = Rounder.keepTrailingZeros(smartWins, 2)
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
                                                        awal=awalStr,
                                                        teamScore=teamScoreStr,
                                                        teamSuccess=teamSuccessStr,
                                                        teamLuck=teamLuckStr,
                                                        smartWins=smartWinsStr,
                                                        scoringShare=scoringShareStr,
                                                        wal=walStr,
                                                        awalPerGame=awalPerGameStr)
            statsModels.append(headToHeadStatsModel)
        return statsModels

    @staticmethod
    def getLeagueStats(leagueModel: LeagueModel, years: list, statSelection: str):
        """
        Returns a model/models for the given stat for self.__leagueModel
        Raises InvalidStatSelectionError if stat is not known
        """
        statOptions = Constants.LEAGUE_STATS_STAT_TITLES
        decimalPlacesForScores = Rounder.getDecimalPlacesRoundedToInScores(leagueModel)
        everyGameCalculator = EveryGameCalculator(leagueModel, years)
        if statSelection not in statOptions:
            raise InvalidStatSelectionError(f"Unknown League Stat: {statSelection}.")
        elif statSelection == Constants.ALL_SCORES_STAT_TITLE:
            allScores = everyGameCalculator.getAllScores()
            allScoresStr = []
            for scoreModel in allScores:
                score = scoreModel.getScore()
                score = Rounder.keepTrailingZeros(score, decimalPlacesForScores)
                teamFor = scoreModel.getTeamFor()
                teamAgainst = scoreModel.getTeamAgainst()
                outcome = scoreModel.getOutcome()
                weekNumber = scoreModel.getWeek()
                year = scoreModel.getYear()
                newModel = ScoreModel(score=score,
                                      teamFor=teamFor,
                                      teamAgainst=teamAgainst,
                                      outcome=outcome,
                                      week=weekNumber,
                                      year=year)
                allScoresStr.append(newModel)
            return allScoresStr
        elif statSelection == Constants.MARGINS_OF_VICTORY_STAT_TITLE:
            allMovs = everyGameCalculator.getAllMarginOfVictories()
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
                year = movModel.getYear()
                newModel = MarginOfVictoryModel(marginOfVictory=mov,
                                                winningTeam=teamFor,
                                                winningTeamPoints=teamForPoints,
                                                losingTeam=teamAgainst,
                                                losingTeamPoints=teamAgainstPoints,
                                                week=weekNumber,
                                                year=year)
                allMovsStr.append(newModel)
            return allMovsStr
        elif statSelection == Constants.WINNING_STREAKS_STAT_TITLE:
            streakCalculator = StreakCalculator(leagueModel, years)
            allWinStreaks = streakCalculator.getAllWinStreaks()
            return allWinStreaks
        elif statSelection == Constants.LOSING_STREAKS_STAT_TITLE:
            streakCalculator = StreakCalculator(leagueModel, years)
            allLossStreaks = streakCalculator.getAllLossStreaks()
            return allLossStreaks
        elif statSelection == Constants.OWNER_COMPARISON_STAT_TITLE:
            allYears = LeagueModelNavigator.getAllYearsWithWeeks(leagueModel, asInts=True)
            allOwnerIds = LeagueModelNavigator.getAllTeamIdsInLeague(leagueModel, allYears[0])

            ownerComparisonModels = []
            for ownerId in allOwnerIds:
                decimalPlacesRoundedToScores = Rounder.getDecimalPlacesRoundedToInScores(leagueModel)
                ownerName = LeagueModelNavigator.getTeamById(leagueModel, "0", ownerId).getTeamName()
                scoresCalculator = ScoresCalculator(ownerId, leagueModel, allYears)
                maxScore = scoresCalculator.getMaxScore()
                maxScoreStr = Rounder.keepTrailingZeros(maxScore, decimalPlacesRoundedToScores)
                minScore = scoresCalculator.getMinScore()
                minScoreStr = Rounder.keepTrailingZeros(minScore, decimalPlacesRoundedToScores)
                ppgCalculator = PpgCalculator(ownerId, leagueModel, allYears)
                ppg = ppgCalculator.getPpg()
                ppgAgainst = ppgCalculator.getPpgAgainst()
                ppgStr = Rounder.keepTrailingZeros(ppg, decimalPlacesRoundedToScores)
                ppgAgainstStr = Rounder.keepTrailingZeros(ppgAgainst, decimalPlacesRoundedToScores)
                plusMinus = scoresCalculator.getPlusMinus()
                plusMinusStr = Rounder.keepTrailingZeros(plusMinus, decimalPlacesRoundedToScores)
                stddev = scoresCalculator.getStandardDeviation()
                stddevStr = Rounder.keepTrailingZeros(stddev, 2)
                recordCalculator = RecordCalculator(ownerId, leagueModel, allYears)
                wins = recordCalculator.getWins()
                losses = recordCalculator.getLosses()
                ties = recordCalculator.getTies()
                winPercentage = recordCalculator.getWinPercentage()
                winPercentageStr = Rounder.keepTrailingZeros(winPercentage, 3)
                awalCalculator = AwalCalculator(ownerId, leagueModel, allYears, wins, ties)
                awal = awalCalculator.getAwal()
                awalStr = Rounder.keepTrailingZeros(awal, 2)
                wal = awalCalculator.getWal()
                walStr = Rounder.keepTrailingZeros(wal, 2)
                gamesPlayed = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, allYears, ownerId)
                # NOTE: if a team has played 0 games, the SSL calculations will have a DivisionByZero Error
                # this SHOULD not happen, because currently, a team HAS to play every week
                scoringShare = scoresCalculator.getScoringShare()
                scoringShareStr = Rounder.keepTrailingZeros(scoringShare, 2)
                scoringShareAgainst = scoresCalculator.getScoringShareAgainst()
                scoringShareAgainstStr = Rounder.keepTrailingZeros(scoringShareAgainst, 2)
                sslCalculator = SslCalculator(awal, wal, scoringShare, maxScore, minScore, gamesPlayed)
                teamScore = sslCalculator.getTeamScore()
                teamScoreStr = Rounder.keepTrailingZeros(teamScore, 2)
                teamSuccess = sslCalculator.getTeamSuccess()
                teamSuccessStr = Rounder.keepTrailingZeros(teamSuccess, 2)
                teamLuck = sslCalculator.getTeamLuck()
                teamLuckStr = Rounder.keepTrailingZeros(teamLuck, 2)
                allScores = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, allYears, ownerId)
                smartCalculator = SmartCalculator(leagueModel, allYears)
                smartWins = smartCalculator.getSmartWinsOfScoresList(allScores)
                smartWinsStr = Rounder.keepTrailingZeros(smartWins, 2)
                strengthOfScheduleCalculator = StrengthOfScheduleCalculator(ownerId, leagueModel, allYears)
                strengthOfSchedule = strengthOfScheduleCalculator.getStrengthOfSchedule()
                strengthOfScheduleStr = Rounder.keepTrailingZeros(strengthOfSchedule, 3)

                ownerComparisonModel = OwnerComparisonModel(ownerId=ownerId,
                                                            ownerName=ownerName,
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
                                                            awal=awalStr,
                                                            teamScore=teamScoreStr,
                                                            teamSuccess=teamSuccessStr,
                                                            teamLuck=teamLuckStr,
                                                            smartWins=smartWinsStr,
                                                            scoringShare=scoringShareStr,
                                                            strengthOfSchedule=strengthOfScheduleStr,
                                                            wal=walStr,
                                                            scoringShareAgainst=scoringShareAgainstStr)
                ownerComparisonModels.append(ownerComparisonModel)
            # sort from win percentage high -> low
            ownerComparisonModels.sort(key=lambda x: x.getWinPercentage(), reverse=True)
            return ownerComparisonModels
        elif statSelection == Constants.LEAGUE_AVERAGES_STAT_TITLE:
            # return a dictionary with each average
            leagueAveragesDict = dict()
            averageCalculator = AverageCalculator(leagueModel, years)
            leagueAveragesDict[Constants.AVERAGE_SCORE_STAT_TITLE] = averageCalculator.getAverageScore()
            leagueAveragesDict[Constants.AVERAGE_SCORE_IN_WINS_STAT_TITLE] = averageCalculator.getAverageScoreInWins()
            leagueAveragesDict[
                Constants.AVERAGE_SCORE_IN_LOSSES_STAT_TITLE] = averageCalculator.getAverageScoreInLosses()
            return leagueAveragesDict

    @staticmethod
    def getGraphDiv(leagueModel: LeagueModel, years: list, screenWidth: float, graphSelection: str):
        """
        Raises InvalidStatSelectionError if graph is not known
        """
        if graphSelection == Constants.PPG_BY_WEEK:
            data = dict()
            numOfWeeksList = []
            for year in years:
                for team in leagueModel.getYears()[str(year)].getTeams():
                    data[team.getTeamName()] = LeagueModelNavigator.getListOfTeamScores(leagueModel, year,
                                                                                        team.getTeamId())
                    numOfWeeksList.append(LeagueModelNavigator.getNumberOfWeeksInLeague(leagueModel, year, asList=True))
            xAxisTicks = max(numOfWeeksList)
            return GraphBuilder.getHtmlForByWeekLineGraph(screenWidth, data, xAxisTicks, "Points Scored", 10,
                                                          Constants.PPG_BY_WEEK)

        elif graphSelection == Constants.AWAL_BY_WEEK:
            data = dict()
            numOfWeeksList = []
            for year in years:
                for team in leagueModel.getYears()[str(year)].getTeams():
                    numOfWeeksList.append(LeagueModelNavigator.getNumberOfWeeksInLeague(leagueModel, year, asList=True))
                    data[team.getTeamName()] = []
                    for week in leagueModel.getYears()[str(year)].getWeeks():
                        recordCalculator = RecordCalculator(team.getTeamId(), leagueModel, [year])
                        awalCalculator = AwalCalculator(team.getTeamId(), leagueModel, [year],
                                                        recordCalculator.getWins(throughWeek=week.getWeekNumber()),
                                                        recordCalculator.getTies(throughWeek=week.getWeekNumber()))
                        awal = awalCalculator.getAwal(throughWeek=week.getWeekNumber())
                        data[team.getTeamName()].append(awal)
            xAxisTicks = max(numOfWeeksList)
            return GraphBuilder.getHtmlForByWeekLineGraph(screenWidth, data, xAxisTicks, Constants.AWAL_STAT_TITLE, 1,
                                                          Constants.AWAL_BY_WEEK)

        elif graphSelection == Constants.SCORING_SHARE:
            teamNames = []
            teamPoints = []
            for year in years:
                for team in leagueModel.getYears()[str(year)].getTeams():
                    teamNames.append(team.getTeamName())
                    totalPoints = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, [year], team.getTeamId())
                    teamPoints.append(totalPoints)
            return GraphBuilder.getHtmlForPieGraph(screenWidth, teamNames, teamPoints, Constants.SCORING_SHARE)

        elif graphSelection == Constants.AWAL_PER_GAME_OVER_SCORING_SHARE:
            return GraphBuilder.getHtmlForAwalOverScoringShare(leagueModel, years, screenWidth)

        elif graphSelection == Constants.FREQUENCY_OF_SCORES:
            allScores = []
            for year in years:
                for team in leagueModel.getYears()[str(year)].getTeams():
                    allScores += LeagueModelNavigator.getListOfTeamScores(leagueModel, year, team.getTeamId())
            return GraphBuilder.getHtmlForHistogram(screenWidth, allScores, int(len(allScores) / 5), "Points Scored",
                                                    "Occurrences", Constants.FREQUENCY_OF_SCORES)

        elif graphSelection == Constants.POINTS_FOR_OVER_POINTS_AGAINST:
            return GraphBuilder.getHtmlForPointsOverPointsAgainst(leagueModel, years, screenWidth)

        elif graphSelection == Constants.STRENGTH_OF_SCHEDULE_OVER_SCORING_SHARE_AGAINST:
            return GraphBuilder.getHtmlForStrengthOfScheduleOverScoringShareAgainst(leagueModel, years, screenWidth)

        else:
            raise InvalidStatSelectionError("No Valid Graph Given to Generate.")
