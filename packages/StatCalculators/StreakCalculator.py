from typing import List

from helpers.Constants import Constants
from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from models.league_stat_models.StreakModel import StreakModel


class StreakCalculator:

    def __init__(self, leagueModel: LeagueModel, years: list):
        self.__leagueModel = leagueModel
        self.__years = years

    def getAllWinStreaks(self) -> List[StreakModel]:
        """
        This returns a list of StreakModels that contain all the win streaks for all teams in self.__leagueModel within self.__years.
        """
        streakModelList = []
        allTeamIds = LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, self.__years[0])
        mostRecentYear = LeagueModelNavigator.getMostRecentYear(self.__leagueModel, asInt=True)
        for teamId in allTeamIds:
            currentStreakModelDict = self.__getDefaultStreakDict(teamId)
            for year in self.__years:
                for week in self.__leagueModel.getYears()[str(year)].getWeeks():
                    weekNumber = week.getWeekNumber()
                    for matchup in week.getMatchups():
                        # check if our target team plays in this matchup
                        if matchup.getTeamA().getTeamId() == teamId or matchup.getTeamB().getTeamId() == teamId:
                            # check if our target team won
                            if LeagueModelNavigator.getGameOutcomeAsString(matchup, teamId) == Constants.WIN:
                                tmpTeam = LeagueModelNavigator.getTeamById(self.__leagueModel, year, teamId)
                                # check if we are currently on a streak
                                if currentStreakModelDict["streakNumber"] is not None:
                                    # currently on a streak, update streak number and "end" streak data
                                    currentStreakModelDict["streakNumber"] += 1
                                    currentStreakModelDict["endDate"] = f"Week {weekNumber}, {year}"
                                    currentStreakModelDict["endTeam"] = tmpTeam
                                else:
                                    # no current streak, start one
                                    # initialize tmp streak dict
                                    currentStreakModelDict["streakNumber"] = 1
                                    currentStreakModelDict["startDate"] = f"Week {weekNumber}, {year}"
                                    currentStreakModelDict["startTeam"] = tmpTeam
                                    currentStreakModelDict["endDate"] = f"Week {weekNumber}, {year}"
                                    currentStreakModelDict["endTeam"] = tmpTeam
                                    currentStreakModelDict["ongoing"] = True
                            else:
                                # if there was a streak of 2+, it is now over
                                if currentStreakModelDict["streakNumber"] is not None and currentStreakModelDict[
                                    "streakNumber"] > 1:
                                    # valid streak
                                    # mark as not ongoing streak
                                    currentStreakModelDict["ongoing"] = False
                                    # get StreakModel and add to return list
                                    streakModelList.append(self.__getStreakModelFromDict(currentStreakModelDict))
                                # reset streak dict
                                currentStreakModelDict = self.__getDefaultStreakDict(teamId)
            # check if we are currently on a streak and if so, add to streak return list
            if currentStreakModelDict["streakNumber"] is not None and currentStreakModelDict["streakNumber"] > 1:
                # valid streak, check if this streak is ongoing
                # remove end date if ongoing
                if currentStreakModelDict["ongoing"] and int(year) == mostRecentYear:
                    currentStreakModelDict["ongoing"] = True
                    currentStreakModelDict["endDate"] = ""
                else:
                    currentStreakModelDict["ongoing"] = False
                # get StreakModel and add to return list
                streakModelList.append(self.__getStreakModelFromDict(currentStreakModelDict))
        return streakModelList

    def getAllLossStreaks(self) -> List[StreakModel]:
        """
        This returns a list of StreakModels that contain all the loss streaks for all teams in self.__leagueModel within self.__years.
        """
        streakModelList = []
        allTeamIds = LeagueModelNavigator.getAllTeamIdsInLeague(self.__leagueModel, self.__years[0])
        mostRecentYear = LeagueModelNavigator.getMostRecentYear(self.__leagueModel, asInt=True)
        for teamId in allTeamIds:
            currentStreakModelDict = self.__getDefaultStreakDict(teamId)
            for year in self.__years:
                for week in self.__leagueModel.getYears()[str(year)].getWeeks():
                    weekNumber = week.getWeekNumber()
                    for matchup in week.getMatchups():
                        # check if our target team plays in this matchup
                        if matchup.getTeamA().getTeamId() == teamId or matchup.getTeamB().getTeamId() == teamId:
                            # check if our target team won
                            if LeagueModelNavigator.getGameOutcomeAsString(matchup, teamId) == Constants.LOSS:
                                tmpTeam = LeagueModelNavigator.getTeamById(self.__leagueModel, year, teamId)
                                # check if we are currently on a streak
                                if currentStreakModelDict["streakNumber"] is not None:
                                    # currently on a streak, update streak number and "end" streak data
                                    currentStreakModelDict["streakNumber"] += 1
                                    currentStreakModelDict["endDate"] = f"Week {weekNumber}, {year}"
                                    currentStreakModelDict["endTeam"] = tmpTeam
                                else:
                                    # no current streak, start one
                                    # initialize tmp streak dict
                                    currentStreakModelDict["streakNumber"] = 1
                                    currentStreakModelDict["startDate"] = f"Week {weekNumber}, {year}"
                                    currentStreakModelDict["startTeam"] = tmpTeam
                                    currentStreakModelDict["endDate"] = f"Week {weekNumber}, {year}"
                                    currentStreakModelDict["endTeam"] = tmpTeam
                                    currentStreakModelDict["ongoing"] = True
                            else:
                                # if there was a streak of 2+, it is now over
                                if currentStreakModelDict["streakNumber"] is not None and currentStreakModelDict[
                                    "streakNumber"] > 1:
                                    # valid streak
                                    # mark as not ongoing streak
                                    currentStreakModelDict["ongoing"] = False
                                    # get StreakModel and add to return list
                                    streakModelList.append(self.__getStreakModelFromDict(currentStreakModelDict))
                                # reset streak dict
                                currentStreakModelDict = self.__getDefaultStreakDict(teamId)
            # check if we are currently on a streak and if so, add to streak return list
            if currentStreakModelDict["streakNumber"] is not None and currentStreakModelDict["streakNumber"] > 1:
                # valid streak, check if this streak is ongoing
                # remove end date if ongoing
                if currentStreakModelDict["ongoing"] and int(year) == mostRecentYear:
                    currentStreakModelDict["ongoing"] = True
                    currentStreakModelDict["endDate"] = ""
                else:
                    currentStreakModelDict["ongoing"] = False
                # get StreakModel and add to return list
                streakModelList.append(self.__getStreakModelFromDict(currentStreakModelDict))
        return streakModelList

    def __getDefaultStreakDict(self, teamId):
        """
        This returns a default streak dict.
        """
        return {"owner": LeagueModelNavigator.getTeamById(self.__leagueModel, "0", teamId),
                "streakNumber": None,
                "startDate": None,
                "startTeam": None,
                "endDate": None,
                "endTeam": None,
                "ongoing": None}

    def __getStreakModelFromDict(self, streakDict: dict) -> StreakModel:
        """
        This takes in a dictionary and returns it as a valid StreakModel
        """
        return StreakModel(owner=streakDict["owner"],
                           streakNumber=streakDict["streakNumber"],
                           startDate=streakDict["startDate"],
                           startTeam=streakDict["startTeam"],
                           endDate=streakDict["endDate"],
                           endTeam=streakDict["endTeam"],
                           ongoing=streakDict["ongoing"])
