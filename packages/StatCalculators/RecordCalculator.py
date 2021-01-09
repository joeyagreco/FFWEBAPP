from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class RecordCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__rounder = Rounder()

    def getWins(self, **params):
        """
        Returns as an int the number of wins the team with self.__teamId has in this league.
        WEEK: [int] Gives wins through that week.
        VSTEAMIDS: [list] Gives wins vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        wins = 0
        for week in self.__leagueModel.getWeeks():
            if week.getWeekNumber() > weekNumber:
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

    def getLosses(self, **params):
        """
        Returns as an int the number of losses the team with self.__teamId has in this league.
        WEEK: [int] Gives losses through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        losses = 0
        for week in self.__leagueModel.getWeeks():
            if week.getWeekNumber() > weekNumber:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    # see if they lost as team A
                    if matchup.getTeamAScore() < matchup.getTeamBScore():
                        losses += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    # see if they lost as team B
                    if matchup.getTeamBScore() < matchup.getTeamAScore():
                        losses += 1
        return losses

    def getLossesVsTeam(self, opponentTeamId: int):
        """
        Returns as an int the number of losses the team with self.__teamId has against the team with the given ID.
        """
        losses = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    # see if they lost as team A
                    if matchup.getTeamAScore() < matchup.getTeamBScore():
                        losses += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    # see if they lost as team B
                    if matchup.getTeamBScore() < matchup.getTeamAScore():
                        losses += 1
        return losses

    def getTies(self, **params):
        """
        Returns as an int the number of ties the team with self.__teamId has in this league.
        WEEK: [int] Gives ties through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        ties = 0
        for week in self.__leagueModel.getWeeks():
            if week.getWeekNumber() > weekNumber:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    # see if they tied as team A
                    if matchup.getTeamAScore() == matchup.getTeamBScore():
                        ties += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    # see if they tied as team B
                    if matchup.getTeamBScore() == matchup.getTeamAScore():
                        ties += 1
        return ties

    def getTiesVsTeam(self, opponentTeamId: int):
        """
        Returns as an int the number of ties the team with self.__teamId has against the team with the given ID.
        """
        ties = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    # see if they tied as team A
                    if matchup.getTeamAScore() == matchup.getTeamBScore():
                        ties += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    # see if they tied as team B
                    if matchup.getTeamBScore() == matchup.getTeamAScore():
                        ties += 1
        return ties

    def getWinPercentage(self, **params):
        """
        Returns as a float the win percentage of the team with self.__teamId.
        WEEK: [int] Gives win percentage through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        wins = self.getWins(week=weekNumber)
        losses = self.getLosses(week=weekNumber)
        ties = self.getTies(week=weekNumber)
        totalGames = wins + losses + ties

        return self.__rounder.normalRound((wins + (0.5 * ties)) / totalGames, 3)

    def getWinPercentageVsTeam(self, opponentTeamId):
        """
        Returns as a float the win percentage of the team with self.__teamId vs the team with the given ID
        """
        wins = self.getWinsVsTeam(opponentTeamId)
        losses = self.getLossesVsTeam(opponentTeamId)
        ties = self.getTiesVsTeam(opponentTeamId)
        totalGames = wins + losses + ties

        return self.__rounder.normalRound((wins + (0.5 * ties)) / totalGames, 3)
