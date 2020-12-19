from models.league_models.LeagueModel import LeagueModel
from models.league_models.WeekModel import WeekModel


class LeagueModelNavigator:

    def getTeamById(self, leagueModel: LeagueModel, teamId: int):
        """
        Returns a Team object for the team with the given ID in the given league.
        Throws Exception if a team with the given ID is not in the given league.
        """
        for team in leagueModel.getTeams():
            if team.getTeamId() == teamId:
                return team
        raise Exception("Given TeamID is not in the given LeagueModel")

    def teamsPlayInWeek(self, week: WeekModel, team1Id: int, team2Id: int):
        """
        Returns a boolean on whether teams with the given IDs play in the given week.
        """
        for matchup in week.getMatchups():
            if matchup.getTeamA().getTeamId() == team1Id and matchup.getTeamB().getTeamId() == team2Id or matchup.getTeamB().getTeamId() == team1Id and matchup.getTeamA().getTeamId() == team2Id:
                return True
        return False

    def teamsPlayEachOther(self, leagueModel: LeagueModel, team1Id: int, team2Id: int):
        """
        Returns a boolean on whether the teams with the given IDs play at all in the given league.
        """
        for week in leagueModel.getWeeks():
            if self.teamsPlayInWeek(week, team1Id, team2Id):
                return True
        return False
