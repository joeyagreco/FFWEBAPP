from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class RecordCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__rounder = Rounder()

    def getWins(self):
        """
        Returns as an int the number of wins the team with self.__teamId has in this league.
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

    def getWinsVsTeam(self, opponentTeamId: int):
        """
        Returns as an int the number of wins the team with self.__teamId has against the team with the given ID.
        """
        wins = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    # see if they won as team A
                    if matchup.getTeamAScore() > matchup.getTeamBScore():
                        wins += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    # see if they won as team B
                    if matchup.getTeamBScore() > matchup.getTeamAScore():
                        wins += 1
        return wins

    def getLosses(self):
        """
        Returns as an int the number of losses the team with self.__teamId has in this league.
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

    def getLossesVsTeam(self, opponentTeamId: int):
        """
        Returns as an int the number of losses the team with self.__teamId has against the team with the given ID.
        """
        losses = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    # see if they lost as team A
                    if matchup.getTeamAScore() < matchup.getTeamBScore():
                        losses += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    # see if they lost as team B
                    if matchup.getTeamBScore() < matchup.getTeamAScore():
                        losses += 1
        return losses

    def getTies(self):
        """
        Returns as an int the number of ties the team with self.__teamId has in this league.
        """
        ties = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    # see if they tied as team A
                    if matchup.getTeamAScore() == matchup.getTeamBScore():
                        ties += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    # see if they tied as team B
                    if matchup.getTeamBScore() == matchup.getTeamAScore():
                        ties += 1
        return ties

    def getTiesVsTeam(self, opponentTeamId: int):
        """
        Returns as an int the number of ties the team with self.__teamId has against the team with the given ID.
        """
        ties = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    # see if they tied as team A
                    if matchup.getTeamAScore() == matchup.getTeamBScore():
                        ties += 1
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    # see if they tied as team B
                    if matchup.getTeamBScore() == matchup.getTeamAScore():
                        ties += 1
        return ties

    def getWinPercentage(self):
        """
        Returns as a float the win percentage of the team with self.__teamId
        """
        wins = self.getWins()
        losses = self.getLosses()
        ties = self.getTies()
        totalGames = wins + losses + ties

        return self.__rounder.keepTrailingZeros(self.__rounder.normalRound((wins + (0.5 * ties)) / totalGames, 3),3)

    def getWinPercentageVsTeam(self, opponentTeamId):
        """
        Returns as a float the win percentage of the team with self.__teamId vs the team with the given ID
        """
        wins = self.getWinsVsTeam(opponentTeamId)
        losses = self.getLossesVsTeam(opponentTeamId)
        ties = self.getTiesVsTeam(opponentTeamId)
        totalGames = wins + losses + ties

        return self.__rounder.keepTrailingZeros(self.__rounder.normalRound((wins + (0.5 * ties)) / totalGames, 3),3)
