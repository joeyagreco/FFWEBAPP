from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class PpgCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__rounder = Rounder()

    def getPpg(self, **params):
        """
        Returns a float that is the Points Per Game for the team with the given ID.
        WEEK: [int] Gives Max Score through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        scores = []
        for week in self.__leagueModel.getWeeks():
            if week.getWeekNumber() > weekNumber:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamBScore())
        totalPoints = 0
        for score in scores:
            totalPoints += score
        decimalPlacesRoundedTo = self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        return self.__rounder.normalRound(totalPoints / weekNumber, decimalPlacesRoundedTo)

    def getPpgVsTeam(self, opponentTeamId: int):
        """
        Returns a float that is the Points Per Game for the team with self.__teamId against the team with opponentTeamId
        """
        scores = []
        numberOfWeeks = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    scores.append(matchup.getTeamAScore())
                    numberOfWeeks += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    scores.append(matchup.getTeamBScore())
                    numberOfWeeks += 1
        totalPoints = 0
        for score in scores:
            totalPoints += score
        decimalPlacesRoundedTo = self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)
        return self.__rounder.normalRound(totalPoints / numberOfWeeks, decimalPlacesRoundedTo)

    def getPpgAgainst(self, **params):
        """
        Returns a float that is the Points Per Game against the team with the given ID.
        WEEK: [int] Gives Max Score through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
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

