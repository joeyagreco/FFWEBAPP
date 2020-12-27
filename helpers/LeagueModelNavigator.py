from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
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

    def gamesPlayedByTeam(self, leagueModel: LeagueModel, teamId: int):
        """
        Returns as an int the number of games played in the given league by the team with the given ID
        """
        gamesPlayed = 0
        for week in leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == teamId or matchup.getTeamB().getTeamId() == teamId:
                    gamesPlayed += 1
        return gamesPlayed

    def totalLeaguePoints(self, leagueModel: LeagueModel):
        """
        Returns a float that is the total amount of points scored in the given league.
        """
        rounder = Rounder()
        totalPoints = 0
        for week in leagueModel.getWeeks():
            for matchup in week.getMatchups():
                totalPoints += matchup.getTeamAScore()
                totalPoints += matchup.getTeamBScore()
        return rounder.normalRound(totalPoints, rounder.getDecimalPlacesRoundedToInScores(leagueModel))

    def totalPointsScoredByTeam(self, leagueModel: LeagueModel, teamId: int):
        """
        Returns a float that is the total amount of points scored by the team with the given ID in the given league.
        """
        rounder = Rounder()
        totalPoints = 0
        for week in leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == teamId:
                    totalPoints += matchup.getTeamAScore()
                elif matchup.getTeamB().getTeamId() == teamId:
                    totalPoints += matchup.getTeamBScore()
        return rounder.normalRound(totalPoints, rounder.getDecimalPlacesRoundedToInScores(leagueModel))

    def getGameOutcomeAsString(self, matchup: MatchupModel, teamId: int):
        """
        Returns a string representation [win/loss/tie] of the outcome of the given game for the team with the given ID.
        Returns None if a team with the given ID does not play in this matchup.
        """
        if teamId != matchup.getTeamA().getTeamId() and teamId != matchup.getTeamB().getTeamId():
            # the given team doesn't play in the given matchup
            return None
        if teamId == matchup.getTeamA().getTeamId():
            # given team is team A
            isTeamA = True
        else:
            # given team is team B
            isTeamA = False
        if matchup.getTeamAScore() > matchup.getTeamBScore():
            if isTeamA:
                return "win"
            return "loss"
        elif matchup.getTeamAScore() < matchup.getTeamBScore():
            if isTeamA:
                return "loss"
            return "win"
        else:
            return "tie"


