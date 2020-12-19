import statistics

from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel


class ScoresCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__rounder = Rounder()

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
        return self.__rounder.normalRound(max(scores), self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

    def getMaxScoreVsTeam(self, opponentTeamId: int):
        """
        Returns the maximum score the team with the given ID has against the team with opponentTeamId.
        """
        scores = []
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    scores.append(matchup.getTeamBScore())
        return self.__rounder.normalRound(max(scores), self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

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
        return self.__rounder.normalRound(min(scores), self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

    def getMinScoreVsTeam(self, opponentTeamId: int):
        """
        Returns the minimum score the team with the given ID has vs the team with opponentTeamId.
        """
        scores = []
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    scores.append(matchup.getTeamBScore())
        return self.__rounder.normalRound(min(scores), self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel))

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
        return float(self.__rounder.normalRound(totalTeamScore - totalOpponentScore, self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)))

    def getPlusMinusVsTeam(self, opponentTeamId: int):
        """
        Returns the +/- for the team with the given ID has against the team with opponentTeamId.
        Example: Team abc has scored 100 points vs team def and has had 75 points scored against him by team def.
                 Team abc has a +/- of +25 vs team def.
        """
        totalTeamScore = 0
        totalOpponentScore = 0
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    totalTeamScore += matchup.getTeamAScore()
                    totalOpponentScore += matchup.getTeamBScore()
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    totalTeamScore += matchup.getTeamBScore()
                    totalOpponentScore += matchup.getTeamAScore()
        return float(self.__rounder.normalRound(totalTeamScore - totalOpponentScore, self.__rounder.getDecimalPlacesRoundedToInScores(self.__leagueModel)))

    def getStandardDeviation(self):
        """
        Returns the standard deviation of the scores for the team with the given ID has in the given league.
        """
        scores = []
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamBScore())
        standardDeviation = statistics.pstdev(scores)
        return float(self.__rounder.normalRound(standardDeviation, 2))

    def getStandardDeviationVsTeam(self, opponentTeamId: int):
        """
        Returns the standard deviation of the scores for the team with the given ID has vs the team with opponentTeamId.
        """
        scores = []
        for week in self.__leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId and matchup.getTeamB().getTeamId() == opponentTeamId:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId and matchup.getTeamA().getTeamId() == opponentTeamId:
                    scores.append(matchup.getTeamBScore())
        standardDeviation = statistics.pstdev(scores)
        return float(self.__rounder.normalRound(standardDeviation, 2))
