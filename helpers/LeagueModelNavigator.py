from models.league_models.LeagueModel import LeagueModel


class LeagueModelNavigator:

    def getTeamById(self, leagueModel: LeagueModel, teamId: int):
        for team in leagueModel.getTeams():
            if team.getTeamId() == teamId:
                return team
        raise Exception("Given TeamID is not in the given LeagueModel")
