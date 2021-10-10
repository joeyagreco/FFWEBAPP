from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator


class StrengthOfScheduleCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel, years: list):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__years = years

    def getStrengthOfSchedule(self) -> float:
        """
        Returns the Strength of Schedule that the team with the given id has had.
        SoS = totalOpponentAWAL / totalGamesPlayed
        """
        totalOpponentAwal = 0
        gameCount = 0
        for year in self.__years:
            for week in self.__leagueModel.years[str(year)].getWeeks():
                for matchup in week.getMatchups():
                    if matchup.teamA.teamId == self.__teamId:
                        recordCalculator = RecordCalculator(matchup.teamB.teamId, self.__leagueModel, [year])
                        awalCalculator = AwalCalculator(matchup.teamB.teamId, self.__leagueModel, [year],
                                                        recordCalculator.getWins(onlyWeeks=[week.getWeekNumber()]),
                                                        recordCalculator.getTies(onlyWeeks=[week.getWeekNumber()]))
                        totalOpponentAwal += awalCalculator.getAwal(onlyWeeks=[week.getWeekNumber()])
                        gameCount += 1
                    elif matchup.teamB.teamId == self.__teamId:
                        recordCalculator = RecordCalculator(matchup.teamA.teamId, self.__leagueModel, [year])
                        awalCalculator = AwalCalculator(matchup.teamA.teamId, self.__leagueModel, [year],
                                                        recordCalculator.getWins(onlyWeeks=[week.getWeekNumber()]),
                                                        recordCalculator.getTies(onlyWeeks=[week.getWeekNumber()]))
                        totalOpponentAwal += awalCalculator.getAwal(onlyWeeks=[week.getWeekNumber()])
                        gameCount += 1
        if gameCount == 0:
            return 0.0
        return Rounder.normalRound(totalOpponentAwal / gameCount, 3)
