from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from packages.Exceptions.InvalidTeamForStatError import InvalidTeamForStatError


class PpgCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel

    def getPpg(self, **params) -> float:
        """
        Returns a float that is the Points Per Game for the team with the given ID.
        THROUGHWEEK: [int] Gives PPG through that week.
        ONLYWEEKS: [list] Gives PPG for the given week numbers.
        VSTEAMIDS: [list] Gives PPG vs teams with the given IDs.
        """
        throughWeek = params.pop("throughWeek", LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        points = 0
        gameCount = 0
        for week in self.__leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    points += matchup.getTeamAScore()
                    gameCount += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    points += matchup.getTeamBScore()
                    gameCount += 1
        if gameCount == 0:
            raise InvalidTeamForStatError(f"PPG Not Found for Team with ID: {self.__teamId}")
        decimalPlacesRoundedTo = Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        return Rounder.normalRound(points / gameCount, decimalPlacesRoundedTo)

    def getPpgAgainst(self, **params) -> float:
        """
        Returns a float that is the Points Per Game against the team with the given ID.
        THROUGHWEEK: [int] Gives PPG Against through that week.
        ONLYWEEKS: [list] Gives PPG Against for the given week numbers.
        """
        throughWeek = params.pop("throughWeek", LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        points = 0
        gameCount = 0
        for week in self.__leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    points += matchup.getTeamBScore()
                    gameCount += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    points += matchup.getTeamAScore()
                    gameCount += 1
        if gameCount == 0:
            raise InvalidTeamForStatError(f"PPG Against Not Found for Team with ID: {self.__teamId}")
        decimalPlacesRoundedTo = Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        return Rounder.normalRound(points / gameCount, decimalPlacesRoundedTo)

