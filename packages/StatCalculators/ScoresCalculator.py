import math

from models.league_models.LeagueModel import LeagueModel


class ScoresCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel

    def __normalRound(self, score):
        """
        Rounds a float rounded to 2 decimal places.
        """
        part = score * 100
        delta = part - int(part)
        # always round "away from 0"
        if delta >= 0.5 or -0.5 < delta <= 0:
            part = math.ceil(part)
        else:
            part = math.floor(part)
        return part / 100

    def getMaxScore(self):
        """
        Returns the maximum score the team with the given ID has in the given league.
        """
        scores = []
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamBScore())
        return float(max(scores))

    def getMinScore(self):
        """
        Returns the minimum score the team with the given ID has in the given league.
        """
        scores = []
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamBScore())
        return float(min(scores))

    def getPlusMinus(self):
        """
        Returns the +/- for the team with the given ID has in the given league.
        Example: Team abc has scored 100 points and has had 75 points scored against him.
                 Team abc has a +/- of +25.
        """
        totalTeamScore = 0
        totalOpponentScore = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    totalTeamScore += matchup.getTeamAScore()
                    totalOpponentScore += matchup.getTeamBScore()
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    totalTeamScore += matchup.getTeamBScore()
                    totalOpponentScore += matchup.getTeamAScore()
        return float(self.__normalRound(totalTeamScore - totalOpponentScore))
