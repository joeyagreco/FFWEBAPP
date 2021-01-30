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
        THROUGHWEEK: [int] Gives SoS through that week.
        ONLYWEEKS: [list] Gives SoS for the given week numbers.
        """
        throughWeek = params.pop("throughWeek", LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        totalOpponentAwal = 0
        gameCount = 0
        for week in self.__leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    recordCalculator = RecordCalculator(matchup.getTeamB().getTeamId(), self.__leagueModel)
                    awalCalculator = AwalCalculator(matchup.getTeamB().getTeamId(), self.__leagueModel, recordCalculator.getWins(throughWeek=throughWeek), recordCalculator.getTies(throughWeek=throughWeek))
                    totalOpponentAwal += awalCalculator.getAwal(throughWeek=throughWeek)
                    gameCount += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    recordCalculator = RecordCalculator(matchup.getTeamA().getTeamId(), self.__leagueModel)
                    awalCalculator = AwalCalculator(matchup.getTeamA().getTeamId(), self.__leagueModel, recordCalculator.getWins(throughWeek=throughWeek), recordCalculator.getTies(throughWeek=throughWeek))
                    totalOpponentAwal += awalCalculator.getAwal(throughWeek=throughWeek)
                    gameCount += 1
        if gameCount == 0:
            return 0.0
        print(f"{LeagueModelNavigator.getTeamById(self.__leagueModel, self.__teamId).getTeamName()} Opponent AWAL: {totalOpponentAwal}, Total Weeks: {gameCount}")
        return Rounder.normalRound(totalOpponentAwal / gameCount**2, 3)
