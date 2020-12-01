import math


class Rounder:

    def normalRound2(self, number):
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

    def normalRound3(self, number):
        """
        Rounds a float rounded to 3 decimal places.
        """
        part = number * 1000
        delta = part - int(part)
        # always round "away from 0"
        if delta >= 0.5 or -0.5 < delta <= 0:
            part = math.ceil(part)
        else:
            part = math.floor(part)
        return part / 1000
