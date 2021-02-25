import math

from models.league_models.LeagueModel import LeagueModel


class Rounder:
    """
    This class is used to round numbers.
    """

    @staticmethod
    def normalRound(number, decimalPlaces: int) -> float:
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

    @staticmethod
    def getDecimalPlacesRoundedToInScores(league: LeagueModel) -> int:
        """
        Returns an int that represents how many decimal places the scores in this league are rounded to.
        Ex: score of 132.55 -> 2, score of 130.10 -> 1
        Default return value is 1.
        """
        maxDecimalPlaces = 1
        for year in league.getYears():
            for week in league.getYears()[year].getWeeks():
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

    @staticmethod
    def keepTrailingZeros(number, zeros: int) -> str:
        """
        This takes in a number and returns a string of that number that has the amount of trailing zeros that is passed in.
        Note: If zeros is less than 1, it is set to 1 by default.
        Note2: This method DOES NOT round, any extra decimals can and will be cut off to meet zeros length.
        """
        if zeros < 1:
            zeros = 1
        strNumber = str(float(number))
        # add zeros to end of number
        for x in range(zeros):
            strNumber += "0"
        # remove unnecessary zeros from the end
        splitNumber = strNumber.split(".")
        splitNumber[1] = splitNumber[1][:zeros]
        return f"{splitNumber[0]}.{splitNumber[1]}"
