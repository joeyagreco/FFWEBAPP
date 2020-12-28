import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from packages.StatCalculators.SmartCalculator import SmartCalculator


class TestSmartCalculator(unittest.TestCase):

    def test_getPercentileOfScore(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        smartCalculator = SmartCalculator(leagueModel)
        percentile1 = smartCalculator.getPercentileOfScore(100)
        percentile2 = smartCalculator.getPercentileOfScore(105)
        self.assertIsInstance(percentile1, float)
        self.assertEqual(30, percentile1)
        self.assertEqual(100, percentile2)
