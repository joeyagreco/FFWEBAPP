from typing import List

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel


class LeagueBuilder:
    """
    This class takes a league in the form of a Dictionary and converts it into League Model objects.
    """

    def __init__(self, leagueDict: dict):
        self.__leagueDict = leagueDict

    def getLeagueObject(self) -> LeagueModel:
        return self.__getLeagueModel()

    def __getLeagueModel(self) -> LeagueModel:
        league = LeagueModel(self.__leagueDict["_id"],
                             self.__leagueDict["leagueName"],
                             self.__leagueDict["numberOfTeams"],
                             self.__getYearModels())
        return league

    def __getYearModels(self) -> dict:
        years = dict()
        for year in self.__leagueDict["years"]:
            currentYearDict = self.__leagueDict["years"][year]
            years[year] = (YearModel(year,
                                     self.__getTeamModels(currentYearDict),
                                     self.__getWeeks(currentYearDict)))
        return years

    def __getTeamModels(self, year) -> List[TeamModel]:
        teams = []
        for team in year["teams"]:
            teams.append(TeamModel(team["teamId"], team["teamName"]))
        return teams

    def __getTeamModelById(self, teamId: int, yearNumber: int) -> TeamModel:
        for team in self.__leagueDict["years"][str(yearNumber)]["teams"]:
            if team["teamId"] == teamId:
                return TeamModel(team["teamId"], team["teamName"])

    def __getMatchupModelsByWeekNumber(self, weekNumber: int, yearNumber: int) -> List[MatchupModel]:
        matchups = []
        matchupId = 1
        for matchup in self.__leagueDict["years"][str(yearNumber)]["weeks"][weekNumber - 1]["matchups"]:
            matchups.append(MatchupModel(matchupId,
                                         self.__getTeamModelById(matchup["teamA"]["teamId"], yearNumber),
                                         self.__getTeamModelById(matchup["teamB"]["teamId"], yearNumber),
                                         matchup["teamAScore"],
                                         matchup["teamBScore"]))
            matchupId += 1
        return matchups

    def __getWeeks(self, year) -> List[WeekModel]:
        # return None if this is year 0
        if year["year"] == 0:
            return None
        weeks = []
        for i, week in enumerate(year["weeks"]):
            weeks.append(WeekModel(i + 1, self.__getMatchupModelsByWeekNumber(i + 1, year["year"])))
        return weeks
