import math


class Rounder:

    def normalRound(self, number):
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
