import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
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
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.6, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2021 = YearModel(2021, teamList, weekList)
        yearDict = {2020: year2020, 2021: year2021}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        smartCalculator2020 = SmartCalculator(leagueModel, [2020])
        smartCalculator2021 = SmartCalculator(leagueModel, [2021])
        smartCalculatorBothYears = SmartCalculator(leagueModel, [2020, 2021])
        smartWins1 = smartCalculator2020.getSmartWinsOfScore(100)
        smartWins2 = smartCalculator2020.getSmartWinsOfScore(100)
        smartWinsDefault = smartCalculator2020.getSmartWinsOfScore(100)
        smartWins_2021 = smartCalculator2021.getSmartWinsOfScore(100)
        smartWinsBothYears = smartCalculatorBothYears.getSmartWinsOfScore(100)
        self.assertIsInstance(smartWins1, float)
        self.assertEqual(0.32, smartWins1)
        self.assertEqual(0.32, smartWins2)
        self.assertEqual(0.32, smartWinsDefault)
        self.assertEqual(0.18, smartWins_2021)
        self.assertEqual(0.26, smartWinsBothYears)

    def test_getSmartWinsOfScoresList(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        smartCalculator = SmartCalculator(leagueModel, [2020])
        smartWins2 = smartCalculator.getSmartWinsOfScoresList([100, 100])
        smartWinsDefault = smartCalculator.getSmartWinsOfScoresList([100, 100])
        self.assertIsInstance(smartWins2, float)
        self.assertEqual(0.64, smartWins2)
        self.assertEqual(0.64, smartWinsDefault)

    def test_getSmartWinsAdjustmentOfScores(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100, 99)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        smartCalculator = SmartCalculator(leagueModel, [2020])
        swa2 = smartCalculator.getSmartWinsAdjustmentOfScores([100, 100], 1)
        swaDefault = smartCalculator.getSmartWinsAdjustmentOfScores([100, 100], 1)
        self.assertIsInstance(swa2, float)
        self.assertEqual(-0.18, swa2)
        self.assertEqual(-0.18, swaDefault)

