import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from packages.StatCalculators.ScoresCalculator import ScoresCalculator


class TestScoresCalculator(unittest.TestCase):

    def test_getMaxScore(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 98, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.1)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        maxScoreTeam1_1 = ScoresCalculator(1, leagueModel).getMaxScore(week=1)
        maxScoreTeam1_2 = ScoresCalculator(1, leagueModel).getMaxScore(week=2)
        maxScoreTeam1_3 = ScoresCalculator(1, leagueModel).getMaxScore(week=3)
        maxScoreTeam1_vs2 = ScoresCalculator(1, leagueModel).getMaxScore(vsTeamIds=[2])
        maxScoreTeam1_vs3 = ScoresCalculator(1, leagueModel).getMaxScore(vsTeamIds=[3])
        maxScoreTeam1_allParams = ScoresCalculator(1, leagueModel).getMaxScore(week=2, vsTeamIds=[2])
        maxScoreTeam1_default = ScoresCalculator(1, leagueModel).getMaxScore()
        self.assertEqual(98, maxScoreTeam1_1)
        self.assertEqual(99, maxScoreTeam1_2)
        self.assertEqual(100, maxScoreTeam1_3)
        self.assertEqual(100, maxScoreTeam1_vs2)
        self.assertEqual(0, maxScoreTeam1_vs3)
        self.assertEqual(99, maxScoreTeam1_allParams)
        self.assertEqual(100, maxScoreTeam1_default)

    def test_getMinScore(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.1)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 98, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        minScoreTeam1_1 = ScoresCalculator(1, leagueModel).getMinScore(week=1)
        minScoreTeam1_2 = ScoresCalculator(1, leagueModel).getMinScore(week=2)
        minScoreTeam1_3 = ScoresCalculator(1, leagueModel).getMinScore(week=3)
        minScoreTeam1_vs2 = ScoresCalculator(1, leagueModel).getMinScore(vsTeamIds=[2])
        minScoreTeam1_vs3 = ScoresCalculator(1, leagueModel).getMinScore(vsTeamIds=[3])
        minScoreTeam1_allParams = ScoresCalculator(1, leagueModel).getMinScore(week=1, vsTeamIds=[2])
        minScoreTeam1_default = ScoresCalculator(1, leagueModel).getMinScore()
        self.assertEqual(100, minScoreTeam1_1)
        self.assertEqual(99, minScoreTeam1_2)
        self.assertEqual(98, minScoreTeam1_3)
        self.assertEqual(98, minScoreTeam1_vs2)
        self.assertEqual(0, minScoreTeam1_vs3)
        self.assertEqual(100, minScoreTeam1_allParams)
        self.assertEqual(98, minScoreTeam1_default)

    def test_getPlusMinus(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.1)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        plusMinusTeam1_1 = ScoresCalculator(1, leagueModel).getPlusMinus(week=1)
        plusMinusTeam1_2 = ScoresCalculator(1, leagueModel).getPlusMinus(week=2)
        plusMinusTeam1_3 = ScoresCalculator(1, leagueModel).getPlusMinus(week=3)
        plusMinusTeam1_vs2 = ScoresCalculator(1, leagueModel).getPlusMinus(vsTeamIds=[2])
        plusMinusTeam1_vs3 = ScoresCalculator(1, leagueModel).getPlusMinus(vsTeamIds=[3])
        plusMinusTeam1_allParams = ScoresCalculator(1, leagueModel).getPlusMinus(week=2, vsTeamIds=[2])
        plusMinusTeam1_default = ScoresCalculator(1, leagueModel).getPlusMinus()
        self.assertIsInstance(plusMinusTeam1_1, float)
        self.assertEqual(0, plusMinusTeam1_1)
        self.assertEqual(-1.1, plusMinusTeam1_2)
        self.assertEqual(-2.3, plusMinusTeam1_3)
        self.assertEqual(-2.3, plusMinusTeam1_vs2)
        self.assertEqual(0, plusMinusTeam1_vs3)
        self.assertEqual(-1.1, plusMinusTeam1_allParams)
        self.assertEqual(-2.3, plusMinusTeam1_default)

    def test_getStandardDeviation(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.1)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        standardDeviationTeam1_1 = ScoresCalculator(1, leagueModel).getStandardDeviation(week=1)
        standardDeviationTeam1_2 = ScoresCalculator(1, leagueModel).getStandardDeviation(week=2)
        standardDeviationTeam1_3 = ScoresCalculator(1, leagueModel).getStandardDeviation(week=3)
        standardDeviationTeam1_vs2 = ScoresCalculator(1, leagueModel).getStandardDeviation(vsTeamIds=[2])
        standardDeviationTeam1_vs3 = ScoresCalculator(1, leagueModel).getStandardDeviation(vsTeamIds=[3])
        standardDeviationTeam1_allParams = ScoresCalculator(1, leagueModel).getStandardDeviation(week=1, vsTeamIds=[2])
        standardDeviationTeam1_default = ScoresCalculator(1, leagueModel).getStandardDeviation()
        self.assertIsInstance(standardDeviationTeam1_1, float)
        self.assertEqual(0, standardDeviationTeam1_1)
        self.assertEqual(0.5, standardDeviationTeam1_2)
        self.assertEqual(0.47, standardDeviationTeam1_3)
        self.assertEqual(0.47, standardDeviationTeam1_vs2)
        self.assertEqual(0, standardDeviationTeam1_vs3)
        self.assertEqual(0, standardDeviationTeam1_allParams)
        self.assertEqual(0.47, standardDeviationTeam1_default)

    def test_getPercentageOfLeagueScoring(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 101, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        percentageTeam1_1 = ScoresCalculator(1, leagueModel).getPercentageOfLeagueScoring(week=1)
        percentageTeam1_2 = ScoresCalculator(1, leagueModel).getPercentageOfLeagueScoring(week=2)
        percentageTeam1_default = ScoresCalculator(1, leagueModel).getPercentageOfLeagueScoring()
        self.assertIsInstance(percentageTeam1_1, float)
        self.assertEqual(23.87, percentageTeam1_1)
        self.assertEqual(23.96, percentageTeam1_2)
        self.assertEqual(23.96, percentageTeam1_default)
