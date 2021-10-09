import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
from packages.StatCalculators.StreakCalculator import StreakCalculator


class TestStreakCalculator(unittest.TestCase):

    def test_getWinStreaks(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 90.5, 100)
        matchup2 = MatchupModel(2, team3, team4, 120.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 92)
        matchup2 = MatchupModel(2, team3, team4, 60, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 110.2, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 102, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 110.5, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2021 = YearModel(2021, teamList, weekList)
        year0 = YearModel(0, teamList, None)
        yearDict = {"0": year0, "2020": year2020, "2021": year2021}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        winStreaks_2020 = StreakCalculator(leagueModel, [2020]).getAllWinStreaks()
        winStreaks_2021 = StreakCalculator(leagueModel, [2021]).getAllWinStreaks()
        winStreaks_bothYears = StreakCalculator(leagueModel, [2020, 2021]).getAllWinStreaks()
        self.assertIsInstance(winStreaks_2020, list)
        self.assertEqual(3, len(winStreaks_2020))
        self.assertEqual(1, winStreaks_2020[0].owner.getTeamId())
        self.assertEqual(2, winStreaks_2020[0].streakNumber)
        self.assertEqual("Week 2, 2020", winStreaks_2020[0].firstDate)
        self.assertEqual("team1", winStreaks_2020[0].firstTeam.getTeamName())
        self.assertEqual("Week 3, 2020", winStreaks_2020[0].lastDate)
        self.assertEqual("team1", winStreaks_2020[0].lastTeam.getTeamName())
        self.assertIsInstance(winStreaks_2021, list)
        self.assertEqual(2, len(winStreaks_2021))
        self.assertIsInstance(winStreaks_bothYears, list)
        self.assertEqual(4, len(winStreaks_bothYears))
        self.assertEqual(1, winStreaks_bothYears[0].owner.getTeamId())
        self.assertEqual(3, winStreaks_bothYears[0].streakNumber)
        self.assertEqual("Week 2, 2020", winStreaks_bothYears[0].firstDate)
        self.assertEqual("team1", winStreaks_bothYears[0].firstTeam.getTeamName())
        self.assertEqual("Week 1, 2021", winStreaks_bothYears[0].lastDate)
        self.assertEqual("team1", winStreaks_bothYears[0].lastTeam.getTeamName())
        self.assertTrue(winStreaks_2021[-1].ongoing)
        self.assertFalse(winStreaks_bothYears[0].ongoing)

    def test_getWinStreaks_nonCurrentYearCantBeOngoing(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 90.5, 200)
        matchup2 = MatchupModel(2, team3, team4, 120.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 200)
        matchup2 = MatchupModel(2, team3, team4, 60, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 110.2, 200)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 102, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 110.5, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2021 = YearModel(2021, teamList, weekList)
        year0 = YearModel(0, teamList, None)
        yearDict = {"0": year0, "2020": year2020, "2021": year2021}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        winStreaks_bothYears = StreakCalculator(leagueModel, [2020, 2021]).getAllWinStreaks()
        self.assertFalse(winStreaks_bothYears[0].ongoing)

    def test_getLossStreaks(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 90.5, 100)
        matchup2 = MatchupModel(2, team3, team4, 120.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 92)
        matchup2 = MatchupModel(2, team3, team4, 60, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 110.2, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 102, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 110.5, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2021 = YearModel(2021, teamList, weekList)
        year0 = YearModel(0, teamList, None)
        yearDict = {"0": year0, "2020": year2020, "2021": year2021}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        lossStreaks_2020 = StreakCalculator(leagueModel, [2020]).getAllLossStreaks()
        lossStreaks_2021 = StreakCalculator(leagueModel, [2021]).getAllLossStreaks()
        lossStreaks_bothYears = StreakCalculator(leagueModel, [2020, 2021]).getAllLossStreaks()
        self.assertIsInstance(lossStreaks_2020, list)
        self.assertEqual(3, len(lossStreaks_2020))
        self.assertEqual(2, lossStreaks_2020[0].owner.getTeamId())
        self.assertEqual(2, lossStreaks_2020[0].streakNumber)
        self.assertEqual("Week 2, 2020", lossStreaks_2020[0].firstDate)
        self.assertEqual("team2", lossStreaks_2020[0].firstTeam.getTeamName())
        self.assertEqual("Week 3, 2020", lossStreaks_2020[0].lastDate)
        self.assertEqual("team2", lossStreaks_2020[0].lastTeam.getTeamName())
        self.assertIsInstance(lossStreaks_2021, list)
        self.assertEqual(2, len(lossStreaks_2021))
        self.assertIsInstance(lossStreaks_bothYears, list)
        self.assertEqual(4, len(lossStreaks_bothYears))
        self.assertEqual(2, lossStreaks_bothYears[0].owner.getTeamId())
        self.assertEqual(3, lossStreaks_bothYears[0].streakNumber)
        self.assertEqual("Week 2, 2020", lossStreaks_bothYears[0].firstDate)
        self.assertEqual("team2", lossStreaks_bothYears[0].firstTeam.getTeamName())
        self.assertEqual("Week 1, 2021", lossStreaks_bothYears[0].lastDate)
        self.assertEqual("team2", lossStreaks_bothYears[0].lastTeam.getTeamName())
        self.assertTrue(lossStreaks_2021[-1].ongoing)
        self.assertFalse(lossStreaks_2020[1].ongoing)

    def test_getLossStreaks_nonCurrentYearCantBeOngoing(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 90.5, 0)
        matchup2 = MatchupModel(2, team3, team4, 120.1, 0)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 0)
        matchup2 = MatchupModel(2, team3, team4, 60, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 110.2, 0)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 102, 200)
        matchup2 = MatchupModel(2, team3, team4, 110.5, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2021 = YearModel(2021, teamList, weekList)
        year0 = YearModel(0, teamList, None)
        yearDict = {"0": year0, "2020": year2020, "2021": year2021}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        winStreaks_bothYears = StreakCalculator(leagueModel, [2020, 2021]).getAllLossStreaks()
        self.assertFalse(winStreaks_bothYears[0].ongoing)
