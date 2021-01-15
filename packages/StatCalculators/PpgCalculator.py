from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class PpgCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__rounder = Rounder()

    def getPpg(self, **params) -> float:
        """
        Returns a float that is the Points Per Game for the team with the given ID.
        THROUGHWEEK: [int] Gives PPG through that week.
        ONLYWEEKS: [list] Gives PPG for the given week numbers.
        VSTEAMIDS: [list] Gives PPG vs teams with the given IDs.
        """
        leagueModelNavigator = LeagueModelNavigator()
        throughWeek = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", leagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
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
            return 0.0
        decimalPlacesRoundedTo = self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        return self.__rounder.normalRound(points / gameCount, decimalPlacesRoundedTo)

    def getPpgAgainst(self, **params) -> float:
        """
        Returns a float that is the Points Per Game against the team with the given ID.
        THROUGHWEEK: [int] Gives PPG Against through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("throughWeek", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        scores = []
        for week in self.__leagueModel.getWeeks():
            if week.getWeekNumber() > weekNumber:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamBScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamAScore())
        totalPoints = 0
        for score in scores:
            totalPoints += score
        decimalPlacesRoundedTo = self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        return self.__rounder.normalRound(totalPoints / weekNumber, decimalPlacesRoundedTo)

