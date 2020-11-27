from models.league_models.LeagueModel import LeagueModel


class RecordCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel

    def getWins(self):
        """
        Returns as an int the number of wins the team with the given ID has in this league.
        """
        wins = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    # see if they won as team A
                    if matchup.getTeamAScore() > matchup.getTeamBScore():
                        wins += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    # see if they won as team B
                    if matchup.getTeamBScore() > matchup.getTeamAScore():
                        wins += 1
        return wins

    def getLosses(self):
        """
        Returns as an int the number of losses the team with the given ID has in this league.
        """
        losses = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    # see if they lost as team A
                    if matchup.getTeamAScore() < matchup.getTeamBScore():
                        losses += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    # see if they lost as team B
                    if matchup.getTeamBScore() < matchup.getTeamAScore():
                        losses += 1
        return losses

    def getTies(self):
        """
        Returns as an int the number of ties the team with the given ID has in this league.
        """
        ties = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    # see if they lost as team A
                    if matchup.getTeamAScore() == matchup.getTeamBScore():
                        ties += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    # see if they lost as team B
                    if matchup.getTeamBScore() == matchup.getTeamAScore():
                        ties += 1
        return ties

