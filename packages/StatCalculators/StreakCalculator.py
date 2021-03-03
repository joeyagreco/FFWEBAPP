from typing import List

from helpers.Constants import Constants
from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from models.league_stat_models.StreakModel import StreakModel


class StreakCalculator:

    def __init__(self, leagueModel: LeagueModel, teamId: int, years: list):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__years = years

    def getWinStreaks(self) -> List[StreakModel]:
        """
        This returns a list of StreakModels that contain all the win streaks for the team with self.__teamId in self.__leagueModel within self.__years.
        """
        streakModelList = []
        currentStreakModelDict = self.__getDefaultStreakDict()
        for year in self.__years:
            for week in self.__leagueModel.getYears()[year].getWeeks():
                weekNumber = week.getWeekNumber()
                for matchup in week.getMatchups():
                    # check if our target team won
                    if LeagueModelNavigator.getGameOutcomeAsString(matchup, self.__teamId) == Constants.WIN:
                        tmpTeam = LeagueModelNavigator.getTeamById(self.__leagueModel, year, self.__teamId)
                        # check if we are currently on a streak
                        if currentStreakModelDict["streakNumber"] is not None:
                            # currently on a streak, update streak number and "end" streak data
                            currentStreakModelDict["streakNumber"] += 1
                            currentStreakModelDict["endDate"] = f"Week {weekNumber} {year}"
                            currentStreakModelDict["endTeam"] = tmpTeam
                        else:
                            # no current streak, start one
                            # initialize tmp streak dict
                            currentStreakModelDict["streakNumber"] = 1
                            currentStreakModelDict["startDate"] = f"Week {weekNumber} {year}"
                            currentStreakModelDict["startTeam"] = tmpTeam
                            currentStreakModelDict["endDate"] = f"Week {weekNumber} {year}"
                            currentStreakModelDict["endTeam"] = tmpTeam
                    else:
                        # if there was a streak of 2+, it is now over
                        if currentStreakModelDict["streakNumber"] > 1:
                            # valid streak, get StreakModel and add to return list
                            streakModelList.append(self.__getStreakModelFromDict(currentStreakModelDict))
                            # reset tmp streak dict
                            currentStreakModelDict = self.__getDefaultStreakDict()
        return streakModelList

    def __getDefaultStreakDict(self):
        """
        This returns a default streak dict.
        """
        return {"ownerId": self.__teamId,
                "streakNumber": None,
                "startDate": None,
                "startTeam": None,
                "endDate": None,
                "endTeam": None}

    def __getStreakModelFromDict(self, streakDict: dict) -> StreakModel:
        """
        This takes in a dictionary and returns it as a valid StreakModel
        """
        return StreakModel(ownerId=streakDict["ownerId"],
                           streakNumber=streakDict["streakNumber"],
                           startDate=streakDict["startDate"],
                           startTeam=streakDict["startTeam"],
                           endDate=streakDict["endDate"],
                           endTeam=streakDict["endTeam"])
