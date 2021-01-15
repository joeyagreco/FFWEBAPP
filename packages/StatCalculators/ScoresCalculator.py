import statistics

from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class ScoresCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__rounder = Rounder()

    def getMaxScore(self, **params) -> float:
        """
        Returns the maximum score the team with the given ID has in the given league.
        THROUGHWEEK: [int] Gives Max Score through that week.
        ONLYWEEKS: [list] Gives Max Score for the given week numbers.
        VSTEAMIDS: [list] Gives Max Score vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        throughWeek = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        scores = []
        for week in self.__leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    scores.append(matchup.getTeamBScore())
        if not scores:
            return 0.0
        return self.__rounder.normalRound(max(scores),
                                          self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

    def getMinScore(self, **params) -> float:
        """
        Returns the minimum score the team with the given ID has in the given league through the given week.
        THROUGHWEEK: [int] Gives Min Score through that week.
        ONLYWEEKS: [list] Gives Min Score for the given week numbers.
        VSTEAMIDS: [list] Gives Min Score vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        throughWeek = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        scores = []
        for week in self.__leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    scores.append(matchup.getTeamBScore())
        if not scores:
            return 0.0
        return self.__rounder.normalRound(min(scores),
                                          self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

    def getPlusMinus(self, **params) -> float:
        """
        Returns the +/- for the team with the given ID has in the given league.
        Example: Team abc has scored 100 points and has had 75 points scored against him.
                 Team abc has a +/- of +25.
        THROUGHWEEK: [int] Gives Plus/Minus through that week.
        ONLYWEEKS: [list] Gives Plus/Minus for the given week numbers.
        VSTEAMIDS: [list] Gives Plus/Minus vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        throughWeek = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        totalTeamScore = 0
        totalOpponentScore = 0
        for week in self.__leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    totalTeamScore += matchup.getTeamAScore()
                    totalOpponentScore += matchup.getTeamBScore()
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    totalTeamScore += matchup.getTeamBScore()
                    totalOpponentScore += matchup.getTeamAScore()
        return float(self.__rounder.normalRound(totalTeamScore - totalOpponentScore,
                                                self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)))

    def getStandardDeviation(self, **params) -> float:
        """
        Returns the standard deviation of the scores for the team with the given ID has in the given league.
        THROUGHWEEK: [int] Gives Standard Deviation through that week.
        ONLYWEEKS: [list] Gives Standard Deviation for the given week numbers.
        VSTEAMIDS: [list] Gives Standard Deviation vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        throughWeek = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        scores = []
        for week in self.__leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    scores.append(matchup.getTeamBScore())
        if not scores:
            return 0.0
        standardDeviation = statistics.pstdev(scores)
        return float(self.__rounder.normalRound(standardDeviation, 2))

    def getPercentageOfLeagueScoring(self, **params) -> float:
        """
        Returns as a percentage the amount of total league scoring the team with self.__teamID was responsible for.
        THROUGHWEEK: [int] Gives percentage of league scoring through that week.
        VSTEAMIDS: [list] Gives STDEV vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        allWeeksTeamsPlay = leagueModelNavigator.getAllWeeksTeamsPlayEachOther(self.__leagueModel, self.__teamId, vsTeamIds)
        totalLeagueScore = leagueModelNavigator.totalLeaguePoints(self.__leagueModel, throughWeek=weekNumber, onlyIncludeWeeks=allWeeksTeamsPlay)
        totalTeamScore = 0
        for week in self.__leagueModel.getWeeks():
            if week.getWeekNumber() > weekNumber:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    totalTeamScore += matchup.getTeamAScore()
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    totalTeamScore += matchup.getTeamBScore()
        rounder = Rounder()
        percentageOfScoring = rounder.normalRound((totalTeamScore / totalLeagueScore) * 100, 2)
        return percentageOfScoring
