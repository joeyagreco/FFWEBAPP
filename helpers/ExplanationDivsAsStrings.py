from helpers.Constants import Constants


class ExplanationDivsAsStrings:
    """
    This class is used to hold strings that will be converted into HTML divs later.
    The variables declared within this class are NOT meant to be modified.
    """

    # strings used by the applyLinkSpans() method
    __SPAN0 = """<span class="link" onclick="reroute('"""
    __SPAN1 = """')">"""
    __SPAN2 = """</span>"""

    @classmethod
    def applyLinkSpans(cls, string: str) -> str:
        """
        This finds and replaces the text %0% , %2% , and %2% with valid HTML that is a span with a clickable reroute function call.
        EXAMPLE:
        __________________________________________________________________________
        THIS ->             %0%{Constants.PPG_STAT_TITLE}%1%PPG%2%
        BECOMES THIS ->     <span class="link" onclick="reroute('PPG')">PPG</span>
        """
        newStr = string.replace("%0%", cls.__SPAN0)
        newStr = newStr.replace("%1%", cls.__SPAN1)
        newStr = newStr.replace("%2%", cls.__SPAN2)
        return newStr

    @classmethod
    def retrieveStatList(cls, statTitle: str) -> list:
        """
        This is used to retrieve the list of stat strings for the given statTitle.
        Returns a list of empty strings if the statTitle isn't found.
        """
        newList = ["", "", ""]
        if statTitle in cls.__ALL_STATS_EXPLAINED_DICT:
            # apply class methods to convert theses
            newList = []
            for string in cls.__ALL_STATS_EXPLAINED_DICT[statTitle]:
                newList.append(cls.applyLinkSpans(string))
        return newList

    AWAL_PURPOSE = f"""
        {Constants.AWAL_STAT_TITLE} stands for Adjusted Wins Against the League.<br>
        It is exactly that, an adjustment added to the Wins Against the League (or %0%{Constants.WAL_STAT_TITLE}%1%{Constants.WAL_STAT_TITLE}%2%) of a team.<br>
        In simple terms, this stat more accurately represents how many %0%{Constants.WAL_STAT_TITLE}%1%{Constants.WAL_STAT_TITLE}%2% any given team should have.<br>
        <strong>Ex:</strong> A team with 6.3 {Constants.AWAL_STAT_TITLE} "deserves" 6.3 %0%{Constants.WAL_STAT_TITLE}%1%{Constants.WAL_STAT_TITLE}%2%.
        """
    AWAL_FORMULA = f"""
        {Constants.AWAL_STAT_TITLE} = W * (1/L) + T * (0.5/L)<br>
        Where:<br>
        W = Teams outscored<br>
        T = Teams tied<br>
        L = Opponents that week (usually league size - 1)<br>
        """
    AWAL_FORMULA_EXPLAINED = f"""
        To properly calculate {Constants.AWAL_STAT_TITLE}, the {Constants.AWAL_STAT_TITLE} must be calculated once for each team every week.<br>
        Each week's {Constants.AWAL_STAT_TITLE} can then be added together to create an aggregate {Constants.AWAL_STAT_TITLE} for each team.<br>
        A team's {Constants.AWAL_STAT_TITLE} for any given week will <strong>always</strong> be between 0 and 1 (inclusive).
        """
    AWAL_STATS_EXPLAINED = (AWAL_PURPOSE, AWAL_FORMULA, AWAL_FORMULA_EXPLAINED)

    MARGINS_OF_VICTORY_PURPOSE = f"""
        {Constants.MARGINS_OF_VICTORY_STAT_TITLE} (or MOV) is used to measure the magnitude of any given win.
        """

    MARGINS_OF_VICTORY_FORMULA = f"""
        MOV = |Team A Score - Team B Score|<br>
        OR<br>
        MOV = Winning Team Score - Losing Team Score
        """

    MARGINS_OF_VICTORY_FORMULA_EXPLAINED = f"""
        <strong>Note:</strong> {Constants.MARGINS_OF_VICTORY_STAT_TITLE} must be greater than 0.
        """

    MARGINS_OF_VICTORY_STATS_EXPLAINED = (MARGINS_OF_VICTORY_PURPOSE, MARGINS_OF_VICTORY_FORMULA, MARGINS_OF_VICTORY_FORMULA_EXPLAINED)

    MAX_SCORE_PURPOSE = f"""
        {Constants.MAX_SCORE_STAT_TITLE} is used to retrieve the highest score for an individual team.<br>
        It is the inverse of %0%{Constants.MIN_SCORE_STAT_TITLE}%1%{Constants.MIN_SCORE_STAT_TITLE}%2%.
        """

    MAX_SCORE_FORMULA = f"""
        max(A)<br>
        WHERE:<br>
        A = List of every score by a single team
        """

    MAX_SCORE_FORMULA_EXPLAINED = f"""
        <strong>Note:</strong> If a team has multiple "max" scores, this does not change the outcome.<br>
        <strong>Ex:</strong> A team with scores: [100, 105, 104, 102] has a {Constants.MAX_SCORE_STAT_TITLE} of 105.<br>
        AND<br>
        A team with scores: [99, 105, 105, 101] has a {Constants.MAX_SCORE_STAT_TITLE} of 105.
        """

    MAX_SCORE_STATS_EXPLAINED = (MAX_SCORE_PURPOSE, MAX_SCORE_FORMULA, MAX_SCORE_FORMULA_EXPLAINED)

    MIN_SCORE_PURPOSE = f"""
        {Constants.MIN_SCORE_STAT_TITLE} is used to retrieve the lowest score for an individual team.<br>
        It is the inverse of %0%{Constants.MAX_SCORE_STAT_TITLE}%1%{Constants.MAX_SCORE_STAT_TITLE}%2%.
        """

    MIN_SCORE_FORMULA = f"""
        min(A)<br>
        WHERE:<br>
        A = List of every score by a single team
        """

    MIN_SCORE_FORMULA_EXPLAINED = f"""
        <strong>Note:</strong> If a team has multiple "min" scores, this does not change the outcome.<br>
        <strong>Ex:</strong> A team with scores: [100, 105, 104, 102] has a {Constants.MIN_SCORE_STAT_TITLE} of 100.<br>
        AND<br>
        A team with scores: [99, 100, 100, 101] has a {Constants.MIN_SCORE_STAT_TITLE} of 100.
        """

    MIN_SCORE_STATS_EXPLAINED = (MIN_SCORE_PURPOSE, MIN_SCORE_FORMULA, MIN_SCORE_FORMULA_EXPLAINED)

    PPG_PURPOSE = f"""
        {Constants.PPG_STAT_TITLE} (Points Per Game) is the average amount of points a team scores per week.
        """

    PPG_FORMULA = f"""
        (ΣA) / B<br>
        WHERE:<br>
        A = All scores by a team<br>
        B = Number of games played by a team
        """

    PPG_FORMULA_EXPLAINED = f"""
        NA
        """

    PPG_STATS_EXPLAINED = (PPG_PURPOSE, PPG_FORMULA, PPG_FORMULA_EXPLAINED)

    PPG_AGAINST_PURPOSE = f"""
        {Constants.PPG_AGAINST_STAT_TITLE} (Points Per Game Against) is the average amount of points a team has scored against them per week.
        """

    PPG_AGAINST_FORMULA = f"""
        (ΣA) / B<br>
        WHERE:<br>
        A = All scores against a team<br>
        B = Number of games played by a team
        """

    PPG_AGAINST_FORMULA_EXPLAINED = f"""
        NA
        """

    PPG_AGAINST_STATS_EXPLAINED = (PPG_AGAINST_PURPOSE, PPG_AGAINST_FORMULA, PPG_AGAINST_FORMULA_EXPLAINED)


    __ALL_STATS_EXPLAINED_DICT = {Constants.AWAL_STAT_TITLE: AWAL_STATS_EXPLAINED,
                                  Constants.MARGINS_OF_VICTORY_STAT_TITLE: MARGINS_OF_VICTORY_STATS_EXPLAINED,
                                  Constants.MAX_SCORE_STAT_TITLE: MAX_SCORE_STATS_EXPLAINED,
                                  Constants.MIN_SCORE_STAT_TITLE: MIN_SCORE_STATS_EXPLAINED,
                                  Constants.PPG_STAT_TITLE: PPG_STATS_EXPLAINED,
                                  Constants.PPG_AGAINST_STAT_TITLE: PPG_AGAINST_STATS_EXPLAINED}
