import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
from packages.StatCalculators.StrengthOfScheduleCalculator import StrengthOfScheduleCalculator


class TestStrengthOfScheduleCalculator(unittest.TestCase):

    def test_getStrengthOfSchedule(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100.6, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        sosTeam1 = StrengthOfScheduleCalculator(1, leagueModel, [2020]).getStrengthOfSchedule()
        sosTeam2 = StrengthOfScheduleCalculator(2, leagueModel, [2020]).getStrengthOfSchedule()
        sosTeam3 = StrengthOfScheduleCalculator(3, leagueModel, [2020]).getStrengthOfSchedule()
        sosTeam4 = StrengthOfScheduleCalculator(4, leagueModel, [2020]).getStrengthOfSchedule()
        sosTeam5 = StrengthOfScheduleCalculator(5, leagueModel, [2020]).getStrengthOfSchedule()
        sosTeam6 = StrengthOfScheduleCalculator(6, leagueModel, [2020]).getStrengthOfSchedule()
        self.assertIsInstance(sosTeam1, float)
        self.assertEqual(0.5, sosTeam1)
        self.assertEqual(0.45, sosTeam2)
        self.assertEqual(0.15, sosTeam3)
        self.assertEqual(0.1, sosTeam4)
        self.assertEqual(1.0, sosTeam5)
        self.assertEqual(0.8, sosTeam6)
