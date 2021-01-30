import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from packages.StatCalculators.RecordCalculator import RecordCalculator
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
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        sosTeam1_1 = StrengthOfScheduleCalculator(1, leagueModel).getStrengthOfSchedule(throughWeek=1)
        sosTeam1_2 = StrengthOfScheduleCalculator(1, leagueModel).getStrengthOfSchedule(throughWeek=2)
        sosTeam1_only2 = StrengthOfScheduleCalculator(1, leagueModel).getStrengthOfSchedule(onlyWeeks=[2])
        sosTeam1_only1and2 = StrengthOfScheduleCalculator(1, leagueModel).getStrengthOfSchedule(onlyWeeks=[1, 2])
        sosTeam1_allParams = StrengthOfScheduleCalculator(1, leagueModel).getStrengthOfSchedule(throughWeek=2)
        sosTeam1_default = StrengthOfScheduleCalculator(1, leagueModel).getStrengthOfSchedule()
        self.assertIsInstance(sosTeam1_1, float)
        self.assertEqual(0.6, sosTeam1_1)
        self.assertEqual(0.5, sosTeam1_2)
        self.assertEqual(1, sosTeam1_only2)
        self.assertEqual(0.5, sosTeam1_only1and2)
        self.assertEqual(0.5, sosTeam1_allParams)
        self.assertEqual(0.5, sosTeam1_default)

