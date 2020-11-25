import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from packages.StatCalculators.MaxScore import MaxScore
from packages.StatCalculators.Ppg import Ppg


class TestMaxScore(unittest.TestCase):

    def test_getMaxScore(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10)
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
        maxScoreTeam1 = MaxScore(1, leagueModel)
        maxScoreTeam2 = MaxScore(2, leagueModel)
        maxScoreTeam3 = MaxScore(3, leagueModel)
        maxScoreTeam4 = MaxScore(4, leagueModel)
        self.assertEqual(100, maxScoreTeam1.getMaxScore())
        self.assertEqual(100.2, maxScoreTeam2.getMaxScore())
        self.assertEqual(0, maxScoreTeam3.getMaxScore())
        self.assertEqual(50.01, maxScoreTeam4.getMaxScore())


