from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class PpgCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel, years: list):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__years = years

    def getPpg(self, **params) -> float:
        """
        Returns a float that is the Points Per Game for the team with the given ID.
        THROUGHWEEK: [int] Gives PPG through that week.
        ONLYWEEKS: [list] Gives PPG for the given week numbers.
        VSTEAMIDS: [list] Gives PPG vs teams with the given IDs.
        """
        points = 0
        gameCount = 0
        for year in self.__years:
            throughWeek = params.pop("throughWeek", LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, year, excludeIds=[self.__teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in self.__leagueModel.getYears()[year].getWeeks():
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
            return 0.0
        decimalPlacesRoundedTo = Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        return Rounder.normalRound(points / gameCount, decimalPlacesRoundedTo)

    def getPpgAgainst(self, **params) -> float:
        """
        Returns a float that is the Points Per Game against the team with the given ID.
        THROUGHWEEK: [int] Gives PPG Against through that week.
        ONLYWEEKS: [list] Gives PPG Against for the given week numbers.
        """
        points = 0
        gameCount = 0
        for year in self.__years:
            throughWeek = params.pop("throughWeek", LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            for week in self.__leagueModel.getYears()[year].getWeeks():
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
            return 0.0
        decimalPlacesRoundedTo = Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        return Rounder.normalRound(points / gameCount, decimalPlacesRoundedTo)

