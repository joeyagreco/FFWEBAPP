import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from packages.StatCalculators.SslCalculator import SslCalculator


class TestSslCalculator(unittest.TestCase):

    def test_getRawTeamScore(self):
        rawTeamScoreTeam1 = SslCalculator(0.0, 0.0, 100.0, 100.0, 100.0).getRawTeamScore()
        rawTeamScoreTeam2 = SslCalculator(4.5, 4.5, 120.0, 150.0, 100.0).getRawTeamScore()
        rawTeamScoreTeam3 = SslCalculator(5.5, 10.0, 120.0, 150.0, 10.0).getRawTeamScore()
        self.assertIsInstance(rawTeamScoreTeam1, float)
        self.assertEqual(40.0, rawTeamScoreTeam1)
        self.assertEqual(71.5, rawTeamScoreTeam2)
        self.assertEqual(67.5, rawTeamScoreTeam3)
