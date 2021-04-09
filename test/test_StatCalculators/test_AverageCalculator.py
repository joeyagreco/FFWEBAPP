import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
from packages.StatCalculators.AverageCalculator import AverageCalculator


class TestAverageCalculator(unittest.TestCase):

    def test_getAverageScore(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
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
        averageScore_allYears = AverageCalculator(leagueModel, [2020, 2021]).getAverageScore()
        averageScore_2020 = AverageCalculator(leagueModel, [2020]).getAverageScore()
        averageScore_noYears = AverageCalculator(leagueModel, []).getAverageScore()
        self.assertIsInstance(averageScore_allYears, float)
        self.assertEqual(89.2, averageScore_allYears)
        self.assertIsInstance(averageScore_2020, float)
        self.assertEqual(85.1, averageScore_2020)
        self.assertIsInstance(averageScore_noYears, int)
        self.assertEqual(0, averageScore_noYears)

    def test_getAverageScoreInWins(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
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
        averageScore_allYears = AverageCalculator(leagueModel, [2020, 2021]).getAverageScoreInWins()
        averageScore_2020 = AverageCalculator(leagueModel, [2020]).getAverageScoreInWins()
        averageScore_noYears = AverageCalculator(leagueModel, []).getAverageScoreInWins()
        self.assertIsInstance(averageScore_allYears, float)
        self.assertEqual(102.0, averageScore_allYears)
        self.assertIsInstance(averageScore_2020, float)
        self.assertEqual(102.2, averageScore_2020)
        self.assertIsInstance(averageScore_noYears, int)
        self.assertEqual(0, averageScore_noYears)
