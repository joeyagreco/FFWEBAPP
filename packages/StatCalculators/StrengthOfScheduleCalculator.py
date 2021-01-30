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
        VSTEAMIDS: [list] Gives SoS vs teams with the given IDs.
        """
        throughWeek = params.pop("throughWeek", LeagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, excludeId=self.__teamId))
        totalOpponentAwal = 0
        gameCount = 0
        for week in self.__leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    recordCalculator = RecordCalculator(matchup.getTeamB().getTeamId(), self.__leagueModel)
                    awalCalculator = AwalCalculator(matchup.getTeamB().getTeamId(), self.__leagueModel, recordCalculator.getWins(throughWeek=throughWeek), recordCalculator.getTies(throughWeek=throughWeek))
                    totalOpponentAwal += awalCalculator.getAwal(throughWeek=throughWeek)
                    gameCount += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    recordCalculator = RecordCalculator(matchup.getTeamA().getTeamId(), self.__leagueModel)
                    awalCalculator = AwalCalculator(matchup.getTeamB().getTeamId(), self.__leagueModel, recordCalculator.getWins(throughWeek=throughWeek), recordCalculator.getTies(throughWeek=throughWeek))
                    totalOpponentAwal += awalCalculator.getAwal(throughWeek=throughWeek)
                    gameCount += 1
        if gameCount == 0:
            return 0.0
        return Rounder.normalRound(totalOpponentAwal / gameCount, 3)
