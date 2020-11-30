import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator


class TestAwalCalculator(unittest.TestCase):

    def test_getAwalNormal(self):
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
        awalTeam1 = AwalCalculator(1, leagueModel).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.20, awalTeam1)
        self.assertEqual(0.40, awalTeam2)
        self.assertEqual(0.00, awalTeam3)
        self.assertEqual(0.60, awalTeam4)
        self.assertEqual(0.80, awalTeam5)
        self.assertEqual(1.00, awalTeam6)

    def test_getAwalOneTiedMatchup(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        awalTeam1 = AwalCalculator(1, leagueModel).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.30, awalTeam1)
        self.assertEqual(0.30, awalTeam2)
        self.assertEqual(0.00, awalTeam3)
        self.assertEqual(0.60, awalTeam4)
        self.assertEqual(0.80, awalTeam5)
        self.assertEqual(1.00, awalTeam6)

    def test_getAwalOneTieNotMatchup(self):
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
        awalTeam1 = AwalCalculator(1, leagueModel).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.30, awalTeam1)
        self.assertEqual(0.60, awalTeam2)
        self.assertEqual(0.00, awalTeam3)
        self.assertEqual(0.30, awalTeam4)
        self.assertEqual(0.80, awalTeam5)
        self.assertEqual(1.00, awalTeam6)

    def test_getAwalOneTiedMatchupOneTieNotMatchup(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        awalTeam1 = AwalCalculator(1, leagueModel).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.40, awalTeam1)
        self.assertEqual(0.40, awalTeam2)
        self.assertEqual(0.00, awalTeam3)
        self.assertEqual(0.40, awalTeam4)
        self.assertEqual(0.80, awalTeam5)
        self.assertEqual(1.00, awalTeam6)

    def test_getAwalAllTies(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 100, 100)
        matchup3 = MatchupModel(3, team5, team6, 100, 100)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        awalTeam1 = AwalCalculator(1, leagueModel).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.50, awalTeam1)
        self.assertEqual(0.50, awalTeam2)
        self.assertEqual(0.50, awalTeam3)
        self.assertEqual(0.50, awalTeam4)
        self.assertEqual(0.50, awalTeam5)
        self.assertEqual(0.50, awalTeam6)

    def test_getAwalNormalSixteenTeams(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        team7 = TeamModel(6, "team7")
        team8 = TeamModel(6, "team8")
        team9 = TeamModel(6, "team9")
        team10 = TeamModel(6, "team10")
        team11 = TeamModel(6, "team11")
        team12 = TeamModel(6, "team12")
        team13 = TeamModel(6, "team13")
        team14 = TeamModel(6, "team14")
        team15 = TeamModel(6, "team15")
        team16 = TeamModel(6, "team16")
        teamList = [team1, team2, team3, team4, team5, team6, team7, team8,
                    team9, team10, team11, team12, team13, team14, team15, team16]
        matchup1 = MatchupModel(1, team1, team2, 100, 101)
        matchup2 = MatchupModel(2, team3, team4, 102, 103)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchup4 = MatchupModel(4, team7, team8, 106, 107)
        matchup5 = MatchupModel(5, team9, team10, 108, 109)
        matchup6 = MatchupModel(6, team11, team12, 110, 111)
        matchup7 = MatchupModel(7, team13, team14, 112, 113)
        matchup8 = MatchupModel(8, team15, team16, 114, 115)
        matchupList = [matchup1, matchup2, matchup3, matchup4, matchup5, matchup6, matchup7, matchup8]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 16, teamList, weekList)
        awalTeam1 = AwalCalculator(1, leagueModel).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel).getAwal()
        awalTeam7 = AwalCalculator(7, leagueModel).getAwal()
        awalTeam8 = AwalCalculator(8, leagueModel).getAwal()
        awalTeam9 = AwalCalculator(9, leagueModel).getAwal()
        awalTeam10 = AwalCalculator(10, leagueModel).getAwal()
        awalTeam11 = AwalCalculator(11, leagueModel).getAwal()
        awalTeam12 = AwalCalculator(12, leagueModel).getAwal()
        awalTeam13 = AwalCalculator(13, leagueModel).getAwal()
        awalTeam14 = AwalCalculator(14, leagueModel).getAwal()
        awalTeam15 = AwalCalculator(15, leagueModel).getAwal()
        awalTeam616 = AwalCalculator(16, leagueModel).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.20, awalTeam1)
        self.assertEqual(0.40, awalTeam2)
        self.assertEqual(0.00, awalTeam3)
        self.assertEqual(0.60, awalTeam4)
        self.assertEqual(0.80, awalTeam5)
        self.assertEqual(1.00, awalTeam6)
