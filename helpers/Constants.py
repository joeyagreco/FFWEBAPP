class Constants:
    """
    This class is used to hold constants.
    The variables declared within this class are NOT meant to be modified.
    """

    # used for League Model Navigator
    WIN = "Win"
    LOSS = "Loss"
    TIE = "Tie"

    # used for League Stats
    ALL_SCORES = "All Scores"
    MARGINS_OF_VICTORY = "Margins of Victory"
    STAT_OPTIONS = [ALL_SCORES, MARGINS_OF_VICTORY]

    # used for Graphs
    PPG_BY_WEEK = "PPG by Week"
    SCORING_SHARE = "Scoring Share"
    AWAL_OVER_PPG = "AWAL/PPG"
    FREQUENCY_OF_SCORES = "Frequency of Scores"
    POINTS_FOR_OVER_POINTS_AGAINST = "Points For/Points Against"
    AWAL_BY_WEEK = "AWAL by Week"
    GRAPH_OPTIONS = [SCORING_SHARE, FREQUENCY_OF_SCORES, AWAL_OVER_PPG, POINTS_FOR_OVER_POINTS_AGAINST, PPG_BY_WEEK, AWAL_BY_WEEK]