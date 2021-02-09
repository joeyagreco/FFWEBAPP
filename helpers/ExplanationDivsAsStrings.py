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
        {Constants.MAX_SCORE_STAT_TITLE} = max(A)<br>
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
        {Constants.MIN_SCORE_STAT_TITLE} = min(A)<br>
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
        {Constants.PPG_STAT_TITLE} = (ΣA) / B<br>
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
        {Constants.PPG_AGAINST_STAT_TITLE} = (ΣA) / B<br>
        WHERE:<br>
        A = All scores against a team<br>
        B = Number of games played by a team
        """

    PPG_AGAINST_FORMULA_EXPLAINED = f"""
        NA
        """

    PPG_AGAINST_STATS_EXPLAINED = (PPG_AGAINST_PURPOSE, PPG_AGAINST_FORMULA, PPG_AGAINST_FORMULA_EXPLAINED)

    PLUS_MINUS_PURPOSE = f"""
        {Constants.PLUS_MINUS_STAT_TITLE} (+/-) is used to show the net score differential for a team in a season.
        """

    PLUS_MINUS_FORMULA = f"""
        {Constants.PLUS_MINUS_STAT_TITLE} = ΣA - ΣB<br>
        WHERE:<br>
        A = All scores by a team<br>
        B = All scores against a team
        """

    PLUS_MINUS_FORMULA_EXPLAINED = f"""
        {Constants.PLUS_MINUS_STAT_TITLE} can be a misleading stat, as a team with a high {Constants.PLUS_MINUS_STAT_TITLE} isn't necessarily a better team than one with a low {Constants.PLUS_MINUS_STAT_TITLE}.<br>
        However, it is typically a good indication of how <i>successful</i> a team was, as a positive net score differential typically translates to more wins.
        """

    PLUS_MINUS_STATS_EXPLAINED = (PLUS_MINUS_PURPOSE, PLUS_MINUS_FORMULA, PLUS_MINUS_FORMULA_EXPLAINED)

    STDEV_PURPOSE = f"""
        {Constants.STDEV_STAT_TITLE} (Standard Deviation) is used to show how volatile a team's scoring was.<br>
        This stat measures a team's scores relative to the mean (or %0%{Constants.PPG_STAT_TITLE}%1%{Constants.PPG_STAT_TITLE}%2%) of all of their scores. 
        """

    STDEV_FORMULA = f"""
        {Constants.STDEV_STAT_TITLE} = sqrt((Σ|x-u|²)/N)<br>
        WHERE:<br>
        x = A score<br>
        u = %0%{Constants.PPG_STAT_TITLE}%1%{Constants.PPG_STAT_TITLE}%2%<br>
        N = Number of scores (typically weeks played)
        """

    STDEV_FORMULA_EXPLAINED = f"""
        A team with low {Constants.STDEV_STAT_TITLE} has been consistent in their scoring patterns.<br>
        A team with high {Constants.STDEV_STAT_TITLE} has been volatile in their scoring patterns.<br>
        It should be noted that if a team has lower {Constants.STDEV_STAT_TITLE} than another team, it is <i>not</i> an indication that the team with lower {Constants.STDEV_STAT_TITLE} has performed better.<br>
        <strong>Ex:</strong> Team A has scores: <strong>[100, 120, 150, 160]</strong> and a {Constants.STDEV_STAT_TITLE} of <strong>23.8</strong><br>
        Team B has scores: <strong>[70, 72, 71, 69]</strong> and a {Constants.STDEV_STAT_TITLE} of <strong>1.12</strong><br>
        Team B has a lower {Constants.STDEV_STAT_TITLE} than Team A, but has definitely performed worse.
        """

    STDEV_STATS_EXPLAINED = (STDEV_PURPOSE, STDEV_FORMULA, STDEV_FORMULA_EXPLAINED)

    SCORING_SHARE_PURPOSE = f"""
        {Constants.SCORING_SHARE_STAT_TITLE} is used to show what percentage of league scoring a team was responsible for.
        """

    SCORING_SHARE_FORMULA = f"""
        {Constants.SCORING_SHARE_STAT_TITLE} = (ΣA) / (ΣB)<br>
        WHERE:<br>
        A = All scores by a team<br>
        B = All scores by all teams
        """

    SCORING_SHARE_FORMULA_EXPLAINED = f"""
        {Constants.SCORING_SHARE_STAT_TITLE} is a good way to compare how a team performed in a league one year vs another year.<br>
        While scoring 100  %0%{Constants.PPG_STAT_TITLE}%1%{Constants.PPG_STAT_TITLE}%2% one year may not be equivalent to scoring 100  %0%{Constants.PPG_STAT_TITLE}%1%{Constants.PPG_STAT_TITLE}%2% another year,<br>
        scoring 10% of the league's points <i>will</i> be equivalent to scoring 10% of the league's points another year.
        """

    SCORING_SHARE_STATS_EXPLAINED = (SCORING_SHARE_PURPOSE, SCORING_SHARE_FORMULA, SCORING_SHARE_FORMULA_EXPLAINED)





    __ALL_STATS_EXPLAINED_DICT = {Constants.AWAL_STAT_TITLE: AWAL_STATS_EXPLAINED,
                                  Constants.MARGINS_OF_VICTORY_STAT_TITLE: MARGINS_OF_VICTORY_STATS_EXPLAINED,
                                  Constants.MAX_SCORE_STAT_TITLE: MAX_SCORE_STATS_EXPLAINED,
                                  Constants.MIN_SCORE_STAT_TITLE: MIN_SCORE_STATS_EXPLAINED,
                                  Constants.PPG_STAT_TITLE: PPG_STATS_EXPLAINED,
                                  Constants.PPG_AGAINST_STAT_TITLE: PPG_AGAINST_STATS_EXPLAINED,
                                  Constants.PLUS_MINUS_STAT_TITLE: PLUS_MINUS_STATS_EXPLAINED,
                                  Constants.STDEV_STAT_TITLE: STDEV_STATS_EXPLAINED,
                                  Constants.SCORING_SHARE: SCORING_SHARE_STATS_EXPLAINED}
