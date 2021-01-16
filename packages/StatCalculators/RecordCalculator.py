from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class RecordCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__rounder = Rounder()

    def getWins(self, **params) -> int:
        """
        Returns as an int the number of wins the team with self.__teamId has in this league.
        THROUGHWEEK: [int] Gives wins through that week.
        ONLYWEEKS: [list] Gives wins for the given week numbers.
        VSTEAMIDS: [list] Gives wins vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        throughWeek = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        wins = 0
        for week in self.__leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    # see if they won as team A
                    if matchup.getTeamAScore() > matchup.getTeamBScore():
                        wins += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    # see if they won as team B
                    if matchup.getTeamBScore() > matchup.getTeamAScore():
                        wins += 1
        return wins

    def getLosses(self, **params) -> int:
        """
        Returns as an int the number of losses the team with self.__teamId has in this league.
        THROUGHWEEK: [int] Gives losses through that week.
        VSTEAMIDS: [list] Gives losses vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        losses = 0
        for week in self.__leagueModel.getWeeks():
            if week.getWeekNumber() > weekNumber:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    # see if they lost as team A
                    if matchup.getTeamAScore() < matchup.getTeamBScore():
                        losses += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    # see if they lost as team B
                    if matchup.getTeamBScore() < matchup.getTeamAScore():
                        losses += 1
        return losses

    def getTies(self, **params) -> int:
        """
        Returns as an int the number of ties the team with self.__teamId has in this league.
        THROUGHWEEK: [int] Gives ties through that week.
        VSTEAMIDS: [list] Gives ties vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        ties = 0
        for week in self.__leagueModel.getWeeks():
            if week.getWeekNumber() > weekNumber:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    # see if they tied as team A
                    if matchup.getTeamAScore() == matchup.getTeamBScore():
                        ties += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    # see if they tied as team B
                    if matchup.getTeamBScore() == matchup.getTeamAScore():
                        ties += 1
        return ties

    def getWinPercentage(self, **params) -> float:
        """
        Returns as a float the win percentage of the team with self.__teamId.
        THROUGHWEEK: [int] Gives win percentage through that week.
        VSTEAMIDS: [list] Gives ties vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        wins = self.getWins(throughWeek=weekNumber, vsTeamIds=vsTeamIds)
        losses = self.getLosses(throughWeek=weekNumber, vsTeamIds=vsTeamIds)
        ties = self.getTies(throughWeek=weekNumber, vsTeamIds=vsTeamIds)
        totalGames = wins + losses + ties
        # if there are no games played, return 0.0 for win percentage
        if totalGames == 0:
            return 0.0
        return self.__rounder.normalRound((wins + (0.5 * ties)) / totalGames, 3)
