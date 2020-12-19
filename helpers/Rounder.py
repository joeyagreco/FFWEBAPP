import math

from models.league_models.LeagueModel import LeagueModel


class Rounder:

    def normalRound(self, number, decimalPlaces: int):
        """
        Rounds a float rounded decimalPlaces places.
        """
        part = number * (10 ** decimalPlaces)
        delta = part - int(part)
        # always round "away from 0"
        if delta >= 0.5 or -0.5 < delta <= 0:
            part = math.ceil(part)
        else:
            part = math.floor(part)
        return part / (10 ** decimalPlaces)

    def getDecimalPlacesRoundedToInScores(self, league: LeagueModel):
        """
        Returns an int that represents how many decimal places the scores in this league are rounded to.
        Ex: score of 132.55 -> 2, score of 130.10 -> 1
        Default return value is 1.
        """

        maxDecimalPlaces = 1
        for week in league.getWeeks():
            for matchup in week.getMatchups():
                aScore = matchup.getTeamAScore()
                bScore = matchup.getTeamBScore()
                if isinstance(aScore, float):
                    aScoreStr = str(aScore)
                    aScoreDecimalLength = len(aScoreStr.split(".")[1])
                    if aScoreDecimalLength > maxDecimalPlaces:
                        maxDecimalPlaces = aScoreDecimalLength
                if isinstance(bScore, float):
                    bScoreStr = str(bScore)
                    bScoreDecimalLength = len(bScoreStr.split(".")[1])
                    if bScoreDecimalLength > maxDecimalPlaces:
                        maxDecimalPlaces = bScoreDecimalLength
        return maxDecimalPlaces

