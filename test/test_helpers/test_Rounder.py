import unittest

from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel


class TestRounder(unittest.TestCase):

    def test_normalRound(self):

        self.assertIsInstance(Rounder.normalRound(100, 1), float)
        self.assertEqual(100.1, Rounder.normalRound(100.11, 1))
        self.assertEqual(100.2, Rounder.normalRound(100.15, 1))
        self.assertEqual(100.11, Rounder.normalRound(100.114, 2))
        self.assertEqual(100.12, Rounder.normalRound(100.115, 2))

    def test_getDecimalPlacesRoundedToInScores(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        self.assertEqual(1, Rounder.getDecimalPlacesRoundedToInScores(leagueModel))
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.51)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        self.assertEqual(2, Rounder.getDecimalPlacesRoundedToInScores(leagueModel))

    def test_keepTrailingZeros(self):
        score1 = 100
        score2 = 100.1
        score3 = 100.12
        score1_0places = Rounder.keepTrailingZeros(score1, 0)
        score1_1place = Rounder.keepTrailingZeros(score1, 1)
        score1_2places = Rounder.keepTrailingZeros(score1, 2)
        score2_0places = Rounder.keepTrailingZeros(score2, 0)
        score2_1place = Rounder.keepTrailingZeros(score2, 1)
        score2_2places = Rounder.keepTrailingZeros(score2, 2)
        score3_0places = Rounder.keepTrailingZeros(score3, 0)
        score3_1place = Rounder.keepTrailingZeros(score3, 1)
        score3_2places = Rounder.keepTrailingZeros(score3, 2)
        self.assertEqual("100.0", score1_0places)
        self.assertEqual("100.0", score1_1place)
        self.assertEqual("100.00", score1_2places)
        self.assertEqual("100.1", score2_0places)
        self.assertEqual("100.1", score2_1place)
        self.assertEqual("100.10", score2_2places)
        self.assertEqual("100.1", score3_0places)
        self.assertEqual("100.1", score3_1place)
        self.assertEqual("100.12", score3_2places)


