import math

from models.league_models.LeagueModel import LeagueModel


class Ppg:

    def __init__(self, teamId: int, leagueModel: LeagueModel):
        self.__teamId = teamId
        self.__leagueModel = leagueModel

    def getPpg(self):
        """
        Returns a float that is the Points Per Game for the team with the given ID.
        """
        scores = []
        numberOfWeeks = 0
        for week in self.__leagueModel.getWeeks():
            numberOfWeeks += 1
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamAScore())
                elif matchup.getTeamB().getTeamId() == self.__teamId:
                    scores.append(matchup.getTeamBScore())
        totalPoints = 0
        for score in scores:
            totalPoints += score
        return self.__normalRound(totalPoints / numberOfWeeks)

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
