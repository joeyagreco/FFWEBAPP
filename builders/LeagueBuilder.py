from typing import List

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel


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
                             self.__getTeamModels(),
                             self.__getWeeks())
        return league

    def __getTeamModels(self) -> List[TeamModel]:
        teams = []
        for team in self.__leagueDict["teams"]:
            teams.append(TeamModel(team["teamId"], team["teamName"]))
        return teams

    def __getTeamModelById(self, teamId: int) -> TeamModel:
        for team in self.__leagueDict["teams"]:
            if team["teamId"] == teamId:
                return TeamModel(team["teamId"], team["teamName"])

    def __getMatchupModelsByWeekNumber(self, weekNumber: int) -> List[MatchupModel]:
        matchups = []
        matchupId = 1
        for matchup in self.__leagueDict["weeks"][weekNumber - 1]["matchups"]:
            matchups.append(MatchupModel(matchupId,
                                         self.__getTeamModelById(matchup["teamA"]["teamId"]),
                                         self.__getTeamModelById(matchup["teamB"]["teamId"]),
                                         matchup["teamAScore"],
                                         matchup["teamBScore"]))
            matchupId += 1
        return matchups

    def __getWeeks(self) -> List[WeekModel]:
        weeks = []
        for i, week in enumerate(self.__leagueDict["weeks"]):
            weeks.append(WeekModel(i + 1,
                                   self.__getMatchupModelsByWeekNumber(i + 1)))
        return weeks
