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

    @classmethod
    def getLeagueObject(cls, leagueDict: dict) -> LeagueModel:
        return cls.__getLeagueModel(leagueDict)

    @classmethod
    def __getLeagueModel(cls, leagueDict: dict) -> LeagueModel:
        league = LeagueModel(leagueId=leagueDict["_id"],
                             leagueName=leagueDict["leagueName"],
                             numberOfTeams=leagueDict["numberOfTeams"],
                             years=cls.__getYearModels(leagueDict))
        return league

    @classmethod
    def __getYearModels(cls, leagueDict: dict) -> dict:
        years = dict()
        for year in leagueDict["years"]:
            currentYearDict = leagueDict["years"][year]
            years[year] = (YearModel(year=year,
                                     teams=cls.__getTeamModels(currentYearDict),
                                     weeks=cls.__getWeeks(leagueDict, currentYearDict)))
        return years

    @classmethod
    def __getTeamModels(cls, year) -> List[TeamModel]:
        teams = []
        for team in year["teams"]:
            teams.append(TeamModel(teamId=team["teamId"], teamName=team["teamName"]))
        return teams

    @classmethod
    def __getTeamModelById(cls, leagueDict: dict, teamId: int, yearNumber: int) -> TeamModel:
        for team in leagueDict["years"][str(yearNumber)]["teams"]:
            if team["teamId"] == teamId:
                return TeamModel(teamId=team["teamId"], teamName=team["teamName"])

    @classmethod
    def __getMatchupModelsByWeekNumber(cls, leagueDict: dict, weekNumber: int, yearNumber: int) -> List[MatchupModel]:
        matchups = []
        matchupId = 1
        for matchup in leagueDict["years"][str(yearNumber)]["weeks"][weekNumber - 1]["matchups"]:
            matchups.append(MatchupModel(matchupId=matchupId,
                                         teamA=cls.__getTeamModelById(leagueDict, matchup["teamA"]["teamId"],
                                                                      yearNumber),
                                         teamB=cls.__getTeamModelById(leagueDict, matchup["teamB"]["teamId"],
                                                                      yearNumber),
                                         teamAScore=matchup["teamAScore"],
                                         teamBScore=matchup["teamBScore"]))
            matchupId += 1
        return matchups

    @classmethod
    def __getWeeks(cls, leagueDict: dict, year) -> List[WeekModel]:
        # return empty list if this is year 0
        if year["year"] == 0:
            return []
        weeks = []
        for i, week in enumerate(year["weeks"]):
            weeks.append(WeekModel(weekNumber=i + 1,
                                   matchups=cls.__getMatchupModelsByWeekNumber(leagueDict, i + 1, year["year"])))
        return weeks
