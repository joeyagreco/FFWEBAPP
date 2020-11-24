from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel


class LeagueBuilder:

    def __init__(self, leagueDict: dict):
        self.__leagueDict = leagueDict

    def getLeagueObject(self):
        return self.__getLeagueModel()

    def __getLeagueModel(self):
        league = LeagueModel(self.__leagueDict["_id"],
                             self.__leagueDict["leagueName"],
                             self.__leagueDict["numberOfTeams"],
                             self.__getTeamModels(),
                             self.__getWeeks())
        return league

    def __getTeamModels(self):
        teams = []
        for team in self.__leagueDict["teams"]:
            teams.append(TeamModel(team["teamId"], team["teamName"]))
        return teams

    def __getTeamModelById(self, teamId: int):
        for team in self.__leagueDict["teams"]:
            if team["teamId"] == teamId:
                return TeamModel(team["teamId"], team["teamName"])

    def __getMatchupModelsByWeekNumber(self, weekNumber: int):
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

    def __getWeeks(self):
        weeks = []
        for i, week in enumerate(self.__leagueDict["weeks"]):
            weeks.append(WeekModel(i + 1,
                                   self.__getMatchupModelsByWeekNumber(i + 1)))
        return weeks
