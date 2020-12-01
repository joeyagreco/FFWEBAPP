import math

from models.league_models.LeagueModel import LeagueModel
from models.league_models.WeekModel import WeekModel


class AwalCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel

    def getAwal(self):
        """
        Returns a float that is the AWAL for the team with the given ID.
        A = W * (1/L) + T * (0.5/L) - WAL
        Where:
        WAL = Game outcome (1=win, 0=loss, 0.5=tie)
        W = Teams outscored
        T = Teams tied
        L = Opponents in league (league size - 1)
        """
        totalAdjustment = 0
        totalWal = 0
        L = self.__leagueModel.getNumberOfTeams() - 1
        for week in self.__leagueModel.getWeeks():
            WAL = self.__getTeamOutcomeOfWeek(week)
            W = self.__getTeamsOutscoredOfWeek(week)
            T = self.__getTeamsTiedOfWeek(week)
            A = W * (1/L) + T * (0.5/L) - WAL
            totalAdjustment += A
            totalWal += WAL
        return self.__normalRound(totalAdjustment + totalWal)

    def __getTeamOutcomeOfWeek(self, week: WeekModel):
        """
        Returns the outcome in the given week for the team with self.__teamId
        (1=win, 0=loss, 0.5=tie)
        """
        for matchup in week.getMatchups():
            if matchup.getTeamA().getTeamId() == self.__teamId:
                # our target team is TeamA
                if matchup.getTeamAScore() > matchup.getTeamBScore():
                    # our target team won
                    return 1
                elif matchup.getTeamAScore() < matchup.getTeamBScore():
                    # our target team lost
                    return 0
                else:
                    # our target team tied
                    return 0.5
            elif matchup.getTeamB().getTeamId() == self.__teamId:
                # our target team is TeamB
                if matchup.getTeamBScore() > matchup.getTeamAScore():
                    # our target team won
                    return 1
                elif matchup.getTeamBScore() < matchup.getTeamAScore():
                    # our target team lost
                    return 0
                else:
                    # our target team tied
                    return 0.5

    def __getTeamsOutscoredOfWeek(self, week: WeekModel):
        """
        Returns the number of teams outscored in the given week for the team with self.__teamId
        """
        allScores = {}
        for matchup in week.getMatchups():
            allScores[matchup.getTeamA().getTeamId()] = matchup.getTeamAScore()
            allScores[matchup.getTeamB().getTeamId()] = matchup.getTeamBScore()
        allScoresList = []
        for teamId in allScores:
            allScoresList.append(allScores[teamId])
        targetTeamScore = allScores[self.__teamId]
        teamsOutscored = 0
        for score in allScoresList:
            if targetTeamScore > score:
                teamsOutscored += 1
        return teamsOutscored

    def __getTeamsTiedOfWeek(self, week: WeekModel):
        """
        Returns the number of teams tied in the given week for the team with self.__teamId
        """
        allScores = {}
        for matchup in week.getMatchups():
            allScores[matchup.getTeamA().getTeamId()] = matchup.getTeamAScore()
            allScores[matchup.getTeamB().getTeamId()] = matchup.getTeamBScore()
        allScoresList = []
        for teamId in allScores:
            if teamId != self.__teamId:
                allScoresList.append(allScores[teamId])
        targetTeamScore = allScores[self.__teamId]
        teamsTied = 0
        for score in allScoresList:
            if targetTeamScore == score:
                teamsTied += 1
        return teamsTied

    def __normalRound(self, number):
        """
        Rounds a float rounded to 2 decimal places.
        """
        part = number * 100
        delta = part - int(part)
        # always round "away from 0"
        if delta >= 0.5 or -0.5 < delta <= 0:
            part = math.ceil(part)
        else:
            part = math.floor(part)
        return part / 100