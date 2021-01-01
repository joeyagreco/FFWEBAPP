import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from packages.StatCalculators.SmartCalculator import SmartCalculator


class TestSmartCalculator(unittest.TestCase):

    def test_getSmartWinsOfScore(self):
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
        smartWins1 = smartCalculator.getSmartWinsOfScore(100)
        smartWins2 = smartCalculator.getSmartWinsOfScore(105)
        smartWins3 = smartCalculator.getSmartWinsOfScore(0)
        self.assertIsInstance(smartWins1, float)
        self.assertEqual(0.3, smartWins1)
        self.assertEqual(1.0, smartWins2)
        self.assertEqual(0.0, smartWins3)

    def test_getSmartWinsOfScores(self):
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
        smartWins1 = smartCalculator.getSmartWinsOfScores([100])
        self.assertIsInstance(smartWins1, float)
        self.assertEqual(0.3, smartWins1)

    def test_getSmartLuckOfScores(self):
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
        smartLuck1 = smartCalculator.getSmartLuckOfScores([100], 0)
        self.assertIsInstance(smartLuck1, float)
        self.assertEqual(-0.3, smartLuck1)

