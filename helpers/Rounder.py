import math


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
