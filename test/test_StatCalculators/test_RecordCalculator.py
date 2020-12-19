import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from packages.StatCalculators.RecordCalculator import RecordCalculator


class TestRecordCalculator(unittest.TestCase):

    def test_getWins(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        winsTeam1 = RecordCalculator(1, leagueModel).getWins()
        winsTeam2 = RecordCalculator(2, leagueModel).getWins()
        winsTeam3 = RecordCalculator(3, leagueModel).getWins()
        winsTeam4 = RecordCalculator(4, leagueModel).getWins()
        winsTeam5 = RecordCalculator(5, leagueModel).getWins()
        winsTeam6 = RecordCalculator(6, leagueModel).getWins()
        self.assertIsInstance(winsTeam1, int)
        self.assertEqual(0, winsTeam1)
        self.assertEqual(1, winsTeam2)
        self.assertEqual(2, winsTeam6)

    def test_getWinsVsTeam(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        winsTeam1 = RecordCalculator(1, leagueModel).getWinsVsTeam(2)
        winsTeam2 = RecordCalculator(2, leagueModel).getWinsVsTeam(1)
        self.assertIsInstance(winsTeam1, int)
        self.assertEqual(0, winsTeam1)
        self.assertEqual(1, winsTeam2)

    def test_getLosses(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        lossesTeam1 = RecordCalculator(1, leagueModel).getLosses()
        lossesTeam2 = RecordCalculator(2, leagueModel).getLosses()
        lossesTeam3 = RecordCalculator(3, leagueModel).getLosses()
        lossesTeam4 = RecordCalculator(4, leagueModel).getLosses()
        lossesTeam5 = RecordCalculator(5, leagueModel).getLosses()
        lossesTeam6 = RecordCalculator(6, leagueModel).getLosses()
        self.assertIsInstance(lossesTeam1, int)
        self.assertEqual(1, lossesTeam1)
        self.assertEqual(0, lossesTeam2)
        self.assertEqual(2, lossesTeam5)

    def test_getLossesVsTeam(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        lossesTeam1 = RecordCalculator(1, leagueModel).getLossesVsTeam(2)
        lossesTeam2 = RecordCalculator(2, leagueModel).getLossesVsTeam(1)
        self.assertIsInstance(lossesTeam1, int)
        self.assertEqual(1, lossesTeam1)
        self.assertEqual(0, lossesTeam2)

    def test_getTies(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.00)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.6)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        tiesTeam1 = RecordCalculator(1, leagueModel).getTies()
        tiesTeam2 = RecordCalculator(2, leagueModel).getTies()
        tiesTeam3 = RecordCalculator(3, leagueModel).getTies()
        tiesTeam4 = RecordCalculator(4, leagueModel).getTies()
        tiesTeam5 = RecordCalculator(5, leagueModel).getTies()
        tiesTeam6 = RecordCalculator(6, leagueModel).getTies()
        self.assertIsInstance(tiesTeam1, int)
        self.assertEqual(1, tiesTeam1)
        self.assertEqual(0, tiesTeam3)
        self.assertEqual(2, tiesTeam5)

    def test_getTiesVsTeam(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.00)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.6)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        tiesTeam1 = RecordCalculator(1, leagueModel).getTiesVsTeam(2)
        tiesTeam2 = RecordCalculator(2, leagueModel).getTiesVsTeam(1)
        tiesTeam3 = RecordCalculator(3, leagueModel).getTiesVsTeam(4)
        self.assertIsInstance(tiesTeam1, int)
        self.assertEqual(1, tiesTeam1)
        self.assertEqual(1, tiesTeam2)
        self.assertEqual(0, tiesTeam3)

    def test_getWinPercentage(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.00)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.6)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.6)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        winPercentageTeam1 = RecordCalculator(1, leagueModel).getWinPercentage()
        winPercentageTeam2 = RecordCalculator(2, leagueModel).getWinPercentage()
        winPercentageTeam3 = RecordCalculator(3, leagueModel).getWinPercentage()
        winPercentageTeam4 = RecordCalculator(4, leagueModel).getWinPercentage()
        winPercentageTeam5 = RecordCalculator(5, leagueModel).getWinPercentage()
        winPercentageTeam6 = RecordCalculator(6, leagueModel).getWinPercentage()
        self.assertIsInstance(winPercentageTeam1, float)
        self.assertEqual(0.167, winPercentageTeam1)
        self.assertEqual(0.833, winPercentageTeam2)
        self.assertEqual(0.333, winPercentageTeam3)
        self.assertEqual(0.667, winPercentageTeam4)
        self.assertEqual(0.500, winPercentageTeam5)
        self.assertEqual(0.500, winPercentageTeam6)

    def test_getWinPercentageVsTeam(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.00)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.6)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.6)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        winPercentageTeam1 = RecordCalculator(1, leagueModel).getWinPercentageVsTeam(2)
        winPercentageTeam2 = RecordCalculator(2, leagueModel).getWinPercentageVsTeam(1)
        winPercentageTeam3 = RecordCalculator(3, leagueModel).getWinPercentageVsTeam(4)
        winPercentageTeam4 = RecordCalculator(4, leagueModel).getWinPercentageVsTeam(3)
        winPercentageTeam5 = RecordCalculator(5, leagueModel).getWinPercentageVsTeam(6)
        winPercentageTeam6 = RecordCalculator(6, leagueModel).getWinPercentageVsTeam(5)
        self.assertIsInstance(winPercentageTeam1, float)
        self.assertEqual(0.167, winPercentageTeam1)
        self.assertEqual(0.833, winPercentageTeam2)
        self.assertEqual(0.333, winPercentageTeam3)
        self.assertEqual(0.667, winPercentageTeam4)
        self.assertEqual(0.500, winPercentageTeam5)
        self.assertEqual(0.500, winPercentageTeam6)
