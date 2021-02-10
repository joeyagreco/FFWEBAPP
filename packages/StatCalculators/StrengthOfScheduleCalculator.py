from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator


class StrengthOfScheduleCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel

    def getStrengthOfSchedule(self, **params) -> float:
        """
        Returns the Strength of Schedule that the team with the given id has had.
        SoS = totalOpponentAWAL / totalGamesPlayed
        """
        totalOpponentAwal = 0
        gameCount = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    recordCalculator = RecordCalculator(matchup.getTeamB().getTeamId(), self.__leagueModel)
                    awalCalculator = AwalCalculator(matchup.getTeamB().getTeamId(), self.__leagueModel, recordCalculator.getWins(onlyWeeks=[week.getWeekNumber()]), recordCalculator.getTies(onlyWeeks=[week.getWeekNumber()]))
                    totalOpponentAwal += awalCalculator.getAwal(onlyWeeks=[week.getWeekNumber()])
                    gameCount += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    recordCalculator = RecordCalculator(matchup.getTeamA().getTeamId(), self.__leagueModel)
                    awalCalculator = AwalCalculator(matchup.getTeamA().getTeamId(), self.__leagueModel, recordCalculator.getWins(onlyWeeks=[week.getWeekNumber()]), recordCalculator.getTies(onlyWeeks=[week.getWeekNumber()]))
                    totalOpponentAwal += awalCalculator.getAwal(onlyWeeks=[week.getWeekNumber()])
                    gameCount += 1
        if gameCount == 0:
            return 0.0
        return Rounder.normalRound(totalOpponentAwal / gameCount, 3)
