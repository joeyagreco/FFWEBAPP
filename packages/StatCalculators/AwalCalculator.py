from typing import List

from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from models.league_models.WeekModel import WeekModel


class AwalCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel, years: List[int], wins: int, ties: int):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__years = years
        self.__wins = wins
        self.__ties = ties

    def getAwal(self, **params) -> float:
        """
        Returns the AWAL for the team with self.__teamId.
        AWAL = W * (1/L) + T * (0.5/L)
        Where:
        W = Teams outscored
        T = Teams tied
        L = Opponents that week (usually league size - 1)

        THROUGHWEEK: [int] Gives AWAL through that week.
        ONLYWEEKS: [list] Gives AWAL for the given week numbers.
        VSTEAMIDS: [list] Gives AWAL vs teams with the given IDs.
        """
        totalAdjustment = self.getAdjustment(**params)
        return Rounder.normalRound(totalAdjustment + self.getWal(), 2)

    def getAdjustment(self, **params) -> float:
        """
        Returns the adjustment [A] for the team with self.__teamId.
        A = W * (1/L) + T * (0.5/L) - WAL
        Where:
        WAL = Game outcome (1=win, 0=loss, 0.5=tie)
        W = Teams outscored
        T = Teams tied
        L = Opponents in league (league size - 1)

        THROUGHWEEK: [int] Gives Adjustment through that week.
        ONLYWEEKS: [list] Gives Adjustment for the given week numbers.
        VSTEAMIDS: [list] Gives Adjustment vs teams with the given IDs.
        """
        totalAdjustment = 0
        for year in self.__years:
            throughWeek = params.pop("throughWeek",
                                     LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            L = self.__leagueModel.numberOfTeams - 1
            for week in self.__leagueModel.years[str(year)].getWeeks():
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                if LeagueModelNavigator.teamsPlayInWeek(week, self.__teamId, vsTeamIds):
                    WAL = self.__getTeamOutcomeOfWeek(week)
                    W = self.__getTeamsOutscoredOfWeek(week)
                    T = self.__getTeamsTiedOfWeek(week)
                    A = W * (1 / L) + T * (0.5 / L) - WAL
                    totalAdjustment += A
        return Rounder.normalRound(totalAdjustment, 2)

    def getWal(self) -> float:
        """
        Returns the total wins against the league for the team with self.__teamId [from class instance variables].
        """
        wal = self.__wins + (0.5 * self.__ties)
        return Rounder.normalRound(wal, 2)

    def getAwalPerGame(self, **params) -> float:
        """
        Returns the AWAL per game

        THROUGHWEEK: [int] Gives AWAL Per Game through that week.
        ONLYWEEKS: [list] Gives AWAL Per Game for the given week numbers.
        VSTEAMIDS: [list] Gives AWAL Per Game vs teams with the given IDs.
        """
        numberOfGames = LeagueModelNavigator.gamesPlayedByTeam(self.__leagueModel, self.__years,
                                                               self.__teamId, **params)
        return Rounder.normalRound(self.getAwal(**params) / numberOfGames, 2) if numberOfGames != 0 else 0

    def __getTeamOutcomeOfWeek(self, week: WeekModel) -> float:
        """
        Returns the outcome in the given week for the team with self.__teamId.
        (1=win, 0=loss, 0.5=tie)
        """
        for matchup in week.matchups:
            if matchup.teamA.teamId == self.__teamId:
                # our target team is TeamA
                if matchup.teamAScore > matchup.teamBScore:
                    # our target team won
                    return 1
                elif matchup.teamAScore < matchup.teamBScore:
                    # our target team lost
                    return 0
                else:
                    # our target team tied
                    return 0.5
            elif matchup.teamB.teamId == self.__teamId:
                # our target team is TeamB
                if matchup.teamBScore > matchup.teamAScore:
                    # our target team won
                    return 1
                elif matchup.teamBScore < matchup.teamAScore:
                    # our target team lost
                    return 0
                else:
                    # our target team tied
                    return 0.5

    def __getTeamsOutscoredOfWeek(self, week: WeekModel) -> int:
        """
        Returns the number of teams outscored in the given week for the team with self.__teamId.
        """
        allScores = {}
        for matchup in week.matchups:
            allScores[matchup.teamA.teamId] = matchup.teamAScore
            allScores[matchup.teamB.teamId] = matchup.teamBScore
        allScoresList = []
        for teamId in allScores:
            allScoresList.append(allScores[teamId])
        targetTeamScore = allScores[self.__teamId]
        teamsOutscored = 0
        for score in allScoresList:
            if targetTeamScore > score:
                teamsOutscored += 1
        return teamsOutscored

    def __getTeamsTiedOfWeek(self, week: WeekModel) -> int:
        """
        Returns the number of teams tied in the given week for the team with self.__teamId.
        """
        allScores = {}
        for matchup in week.matchups:
            allScores[matchup.teamA.teamId] = matchup.teamAScore
            allScores[matchup.teamB.teamId] = matchup.teamBScore
        allScoresList = []
        for teamId in allScores:
            if teamId != self.__teamId:
                allScoresList.append(allScores[teamId])
        targetTeamScore = allScores[self.__teamId]
        teamsTied = 0
        for score in allScoresList:
            if targetTeamScore == score:
                teamsTied += 1
        return teamsTied
