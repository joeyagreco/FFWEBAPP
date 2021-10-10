import statistics

from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class ScoresCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel, years: list):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__years = years

    def getMaxScore(self, **params) -> float:
        """
        Returns the maximum score the team with the given ID has in the given league in the given years.
        THROUGHWEEK: [int] Gives Max Score through that week.
        ONLYWEEKS: [list] Gives Max Score for the given week numbers.
        VSTEAMIDS: [list] Gives Max Score vs teams with the given IDs.
        """
        scores = []
        for year in self.__years:
            throughWeek = params.pop("throughWeek",
                                     LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in self.__leagueModel.years[str(year)].weeks:
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                for matchup in week.matchups:
                    if matchup.teamA.teamId == self.__teamId and matchup.teamB.teamId in vsTeamIds:
                        scores.append(matchup.teamAScore)
                    elif matchup.teamB.teamId == self.__teamId and matchup.teamA.teamId in vsTeamIds:
                        scores.append(matchup.teamBScore)
        if not scores:
            return 0.0
        return Rounder.normalRound(max(scores), Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

    def getMinScore(self, **params) -> float:
        """
        Returns the minimum score the team with the given ID has in the given league through the given week.
        THROUGHWEEK: [int] Gives Min Score through that week.
        ONLYWEEKS: [list] Gives Min Score for the given week numbers.
        VSTEAMIDS: [list] Gives Min Score vs teams with the given IDs.
        """
        scores = []
        for year in self.__years:
            throughWeek = params.pop("throughWeek",
                                     LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in self.__leagueModel.years[str(year)].weeks:
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                for matchup in week.matchups:
                    if matchup.teamA.teamId == self.__teamId and matchup.teamB.teamId in vsTeamIds:
                        scores.append(matchup.teamAScore)
                    elif matchup.teamB.teamId == self.__teamId and matchup.teamA.teamId in vsTeamIds:
                        scores.append(matchup.teamBScore)
        if not scores:
            return 0.0
        return Rounder.normalRound(min(scores), Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

    def getPlusMinus(self, **params) -> float:
        """
        Returns the +/- for the team with the given ID has in the given league.
        Example: Team abc has scored 100 points and has had 75 points scored against him.
                 Team abc has a +/- of +25.
        THROUGHWEEK: [int] Gives Plus/Minus through that week.
        ONLYWEEKS: [list] Gives Plus/Minus for the given week numbers.
        VSTEAMIDS: [list] Gives Plus/Minus vs teams with the given IDs.
        """
        totalTeamScore = 0
        totalOpponentScore = 0
        for year in self.__years:
            throughWeek = params.pop("throughWeek",
                                     LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in self.__leagueModel.years[str(year)].weeks:
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                for matchup in week.matchups:
                    if matchup.teamA.teamId == self.__teamId and matchup.teamB.teamId in vsTeamIds:
                        totalTeamScore += matchup.teamAScore
                        totalOpponentScore += matchup.teamBScore
                    elif matchup.teamB.teamId == self.__teamId and matchup.teamA.teamId in vsTeamIds:
                        totalTeamScore += matchup.teamBScore
                        totalOpponentScore += matchup.teamAScore
        return float(Rounder.normalRound(totalTeamScore - totalOpponentScore,
                                         Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)))

    def getStandardDeviation(self, **params) -> float:
        """
        Returns the standard deviation of the scores for the team with the given ID has in the given league.
        THROUGHWEEK: [int] Gives Standard Deviation through that week.
        ONLYWEEKS: [list] Gives Standard Deviation for the given week numbers.
        VSTEAMIDS: [list] Gives Standard Deviation vs teams with the given IDs.
        """
        scores = []
        for year in self.__years:
            throughWeek = params.pop("throughWeek",
                                     LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in self.__leagueModel.years[str(year)].weeks:
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                for matchup in week.matchups:
                    if matchup.teamA.teamId == self.__teamId and matchup.teamB.teamId in vsTeamIds:
                        scores.append(matchup.teamAScore)
                    elif matchup.teamB.teamId == self.__teamId and matchup.teamA.teamId in vsTeamIds:
                        scores.append(matchup.teamBScore)
        if not scores:
            return 0.0
        standardDeviation = statistics.pstdev(scores)
        return float(Rounder.normalRound(standardDeviation, 2))

    def getScoringShare(self, **params) -> float:
        """
        Returns as a percentage the amount of total league scoring the team with self.__teamID was responsible for.
        THROUGHWEEK: [int] Gives percentage of league scoring through that week.
        ONLYWEEKS: [list] Gives percentage of league scoring for the given week numbers.
        VSTEAMIDS: [list] Gives percentage of league scoring vs teams with the given IDs.
        """
        totalTeamScore = 0
        totalLeagueScore = 0
        for year in self.__years:
            weekNumber = params.pop("throughWeek",
                                    LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["weekNumber"] = weekNumber
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            allWeeksTeamsPlay = LeagueModelNavigator.getAllWeeksTeamsPlayEachOther(self.__leagueModel, year,
                                                                                   self.__teamId, vsTeamIds,
                                                                                   onlyWeeks=onlyWeeks)
            totalLeagueScore += LeagueModelNavigator.totalLeaguePoints(self.__leagueModel, [year],
                                                                       throughWeek=weekNumber,
                                                                       onlyWeeks=allWeeksTeamsPlay)
            for week in self.__leagueModel.years[str(year)].weeks:
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > weekNumber:
                    break
                for matchup in week.matchups:
                    if matchup.teamA.teamId == self.__teamId and matchup.teamB.teamId in vsTeamIds:
                        totalTeamScore += matchup.teamAScore
                    elif matchup.teamB.teamId == self.__teamId and matchup.teamA.teamId in vsTeamIds:
                        totalTeamScore += matchup.teamBScore
        percentageOfScoring = Rounder.normalRound((totalTeamScore / totalLeagueScore) * 100, 2)
        return percentageOfScoring

    def getScoringShareAgainst(self, **params) -> float:
        """
        Returns as a percentage the amount of total league scoring the team with self.__teamID had scored against them.
        THROUGHWEEK: [int] Gives percentage of league scoring through that week.
        ONLYWEEKS: [list] Gives percentage of league scoring for the given week numbers.
        VSTEAMIDS: [list] Gives percentage of league scoring vs teams with the given IDs.
        """
        totalTeamScore = 0
        totalLeagueScore = 0
        for year in self.__years:
            weekNumber = params.pop("throughWeek",
                                    LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["weekNumber"] = weekNumber
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            allWeeksTeamsPlay = LeagueModelNavigator.getAllWeeksTeamsPlayEachOther(self.__leagueModel, year,
                                                                                   self.__teamId, vsTeamIds,
                                                                                   onlyWeeks=onlyWeeks)
            totalLeagueScore += LeagueModelNavigator.totalLeaguePoints(self.__leagueModel, [year],
                                                                       throughWeek=weekNumber,
                                                                       onlyWeeks=allWeeksTeamsPlay)
            for week in self.__leagueModel.years[str(year)].weeks:
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > weekNumber:
                    break
                for matchup in week.matchups:
                    if matchup.teamA.teamId == self.__teamId and matchup.teamB.teamId in vsTeamIds:
                        totalTeamScore += matchup.teamBScore
                    elif matchup.teamB.teamId == self.__teamId and matchup.teamA.teamId in vsTeamIds:
                        totalTeamScore += matchup.teamAScore
        percentageOfScoring = Rounder.normalRound((totalTeamScore / totalLeagueScore) * 100, 2)
        return percentageOfScoring
