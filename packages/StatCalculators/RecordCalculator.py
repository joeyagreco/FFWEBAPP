from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class RecordCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel, years: list):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__years = years

    def getWins(self, **params) -> int:
        """
        Returns as an int the number of wins the team with self.__teamId has in this league.
        THROUGHWEEK: [int] Gives wins through that week.
        ONLYWEEKS: [list] Gives wins for the given week numbers.
        VSTEAMIDS: [list] Gives wins vs teams with the given IDs.
        """
        wins = 0
        for year in self.__years:
            throughWeek = params.pop("throughWeek",
                                     LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in self.__leagueModel.years[str(year)].getWeeks():
                if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                    continue
                elif week.getWeekNumber() > throughWeek:
                    break
                for matchup in week.getMatchups():
                    if matchup.teamA.getTeamId() == self.__teamId and matchup.teamB.getTeamId() in vsTeamIds:
                        # see if they won as team A
                        if matchup.teamAScore > matchup.teamBScore:
                            wins += 1
                    elif matchup.teamB.getTeamId() == self.__teamId and matchup.teamA.getTeamId() in vsTeamIds:
                        # see if they won as team B
                        if matchup.teamBScore > matchup.teamAScore:
                            wins += 1
        return wins

    def getLosses(self, **params) -> int:
        """
        Returns as an int the number of losses the team with self.__teamId has in this league.
        THROUGHWEEK: [int] Gives losses through that week.
        ONLYWEEKS: [list] Gives losses for the given week numbers.
        VSTEAMIDS: [list] Gives losses vs teams with the given IDs.
        """
        losses = 0
        for year in self.__years:
            throughWeek = params.pop("throughWeek",
                                     LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in self.__leagueModel.years[str(year)].getWeeks():
                if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                    continue
                elif week.getWeekNumber() > throughWeek:
                    break
                for matchup in week.getMatchups():
                    if matchup.teamA.getTeamId() == self.__teamId and matchup.teamB.getTeamId() in vsTeamIds:
                        # see if they lost as team A
                        if matchup.teamAScore < matchup.teamBScore:
                            losses += 1
                    elif matchup.teamB.getTeamId() == self.__teamId and matchup.teamA.getTeamId() in vsTeamIds:
                        # see if they lost as team B
                        if matchup.teamBScore < matchup.teamAScore:
                            losses += 1
        return losses

    def getTies(self, **params) -> int:
        """
        Returns as an int the number of ties the team with self.__teamId has in this league.
        THROUGHWEEK: [int] Gives ties through that week.
        ONLYWEEKS: [list] Gives ties for the given week numbers.
        VSTEAMIDS: [list] Gives ties vs teams with the given IDs.
        """
        ties = 0
        for year in self.__years:
            throughWeek = params.pop("throughWeek",
                                     LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year,
                                                                                           excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in self.__leagueModel.years[str(year)].getWeeks():
                if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                    continue
                elif week.getWeekNumber() > throughWeek:
                    break
                for matchup in week.getMatchups():
                    if matchup.teamA.getTeamId() == self.__teamId and matchup.teamB.getTeamId() in vsTeamIds:
                        # see if they tied as team A
                        if matchup.teamAScore == matchup.teamBScore:
                            ties += 1
                    elif matchup.teamB.getTeamId() == self.__teamId and matchup.teamA.getTeamId() in vsTeamIds:
                        # see if they tied as team B
                        if matchup.teamBScore == matchup.teamAScore:
                            ties += 1
        return ties

    def getWinPercentage(self, **params) -> float:
        """
        Returns as a float the win percentage of the team with self.__teamId.
        THROUGHWEEK: [int] Gives win percentage through that week.
        ONLYWEEKS: [list] Gives win percentage for the given week numbers.
        VSTEAMIDS: [list] Gives win percentage vs teams with the given IDs.
        """
        wins = 0
        losses = 0
        ties = 0
        wins += self.getWins(**params)
        losses += self.getLosses(**params)
        ties += self.getTies(**params)
        totalGames = wins + losses + ties
        # if there are no games played, return 0.0 for win percentage
        if totalGames == 0:
            return 0.0
        return Rounder.normalRound((wins + (0.5 * ties)) / totalGames, 3)
