from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class PpgCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__rounder = Rounder()

    def getPpg(self):
        """
        Returns a float that is the Points Per Game for the team with the given ID.
        """
        scores = []
        numberOfWeeks = 0
        for week in self.__leagueModel.getWeeks():
            numberOfWeeks += 1
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamBScore())
        totalPoints = 0
        for score in scores:
            totalPoints += score
        return self.__rounder.normalRound(totalPoints / numberOfWeeks, self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

    def getPpgAgainst(self):
        """
        Returns a float that is the Points Per Game against the team with the given ID.
        """
        scores = []
        numberOfWeeks = 0
        for week in self.__leagueModel.getWeeks():
            numberOfWeeks += 1
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamBScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamAScore())
        totalPoints = 0
        for score in scores:
            totalPoints += score
        return self.__rounder.normalRound(totalPoints / numberOfWeeks, self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

