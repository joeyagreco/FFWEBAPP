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

    AWAL_PURPOSE = f"""
        AWAL stands for Adjusted Wins Against the League. It is exactly that, an adjustment added to the Wins Against the League (or %0%{Constants.WAL_STAT_TITLE}%1%WAL%2%) of a team.<br>
        In simple terms, this stat more accurately represents how many %0%{Constants.WAL_STAT_TITLE}%1%WAL%2% any given team should have.<br>
        Ex: A team with 6.3 AWAL "deserves" 6.3 %0%{Constants.WAL_STAT_TITLE}%1%WAL%2%.
        """
    AWAL_FORMULA = f"""
        AWAL = W * (1/L) + T * (0.5/L)<br>
        Where:<br>
        W = Teams outscored<br>
        T = Teams tied<br>
        L = Opponents in league (league size - 1)<br>
        """
    AWAL_FORMULA_EXPLAINED = f"""
        To properly calculate AWAL, the AWAL must be calculated once for each team every week.<br>
        Each week's AWAL can then be added together to create an aggregate AWAL for each team.<br>
        A team's AWAL for any given week will ALWAYS be between 0 and 1 (inclusive).
        """

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
