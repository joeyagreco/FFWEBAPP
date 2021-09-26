import statistics

from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class AverageCalculator:

    def __init__(self, leagueModel: LeagueModel, years: list):
        self.__leagueModel = leagueModel
        self.__years = years

    def getAverageScore(self):
        """
        This returns the average score in every game in self.__leagueModel in every year in self.__years
        """
        allScores = []
        for year in self.__years:
            for week in self.__leagueModel.getYears()[str(year)].getWeeks():
                for matchup in week.getMatchups():
                    allScores.append(matchup.getTeamAScore())
                    allScores.append(matchup.getTeamBScore())
        if len(allScores) > 0:
            return Rounder.normalRound(statistics.mean(allScores),
                                       Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))
        return 0

    def getAverageScoreInWins(self):
        """
        This returns the average score in wins in every game in self.__leagueModel in every year in self.__years
        """
        allScores = []
        for year in self.__years:
            for week in self.__leagueModel.getYears()[str(year)].getWeeks():
                for matchup in week.getMatchups():
                    if matchup.getTeamAScore() > matchup.getTeamBScore():
                        allScores.append(matchup.getTeamAScore())
                    elif matchup.getTeamBScore() > matchup.getTeamAScore():
                        allScores.append(matchup.getTeamBScore())
        if len(allScores) > 0:
            return Rounder.normalRound(statistics.mean(allScores),
                                       Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))
        return 0

    def getAverageScoreInLosses(self):
        """
        This returns the average score in losses in every game in self.__leagueModel in every year in self.__years
        """
        allScores = []
        for year in self.__years:
            for week in self.__leagueModel.getYears()[str(year)].getWeeks():
                for matchup in week.getMatchups():
                    if matchup.getTeamAScore() < matchup.getTeamBScore():
                        allScores.append(matchup.getTeamAScore())
                    elif matchup.getTeamBScore() < matchup.getTeamAScore():
                        allScores.append(matchup.getTeamBScore())
        if len(allScores) > 0:
            return Rounder.normalRound(statistics.mean(allScores),
                                       Rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))
        return 0
