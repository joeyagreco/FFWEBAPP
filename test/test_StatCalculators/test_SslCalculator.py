import unittest

from packages.StatCalculators.SslCalculator import SslCalculator


class TestSslCalculator(unittest.TestCase):

    def test_getTeamScore(self):
        rawTeamScoreTeam1 = SslCalculator(0.0, 0.0, 100.0, 100.0, 100.0, 1, 600.0).getTeamScore()
        rawTeamScoreTeam2 = SslCalculator(4.5, 4.5, 550.0, 150.0, 100.0, 7, 3600.0).getTeamScore()
        rawTeamScoreTeam3 = SslCalculator(2.5, 4.5, 550.0, 150.0, 100.0, 7, 3600.0).getTeamScore()
        self.assertIsInstance(rawTeamScoreTeam1, float)
        self.assertEqual(23.33, rawTeamScoreTeam1)
        self.assertEqual(92.34, rawTeamScoreTeam2)
        self.assertEqual(63.77, rawTeamScoreTeam3)

    def test_getTeamSuccess(self):
        rawTeamSuccessTeam1 = SslCalculator(0.0, 0.0, 100.0, 100.0, 100.0, 1, 600.0).getTeamSuccess()
        rawTeamSuccessTeam2 = SslCalculator(4.5, 4.5, 550.0, 150.0, 100.0, 7, 3600.0).getTeamSuccess()
        rawTeamSuccessTeam3 = SslCalculator(4.5, 2.5, 550.0, 150.0, 100.0, 7, 3600.0).getTeamSuccess()
        self.assertIsInstance(rawTeamSuccessTeam1, float)
        self.assertEqual(23.33, rawTeamSuccessTeam1)
        self.assertEqual(92.34, rawTeamSuccessTeam2)
        self.assertEqual(63.77, rawTeamSuccessTeam3)

    def test_getTeamLuck(self):
        rawTeamLuckTeam1 = SslCalculator(1.0, 0.0, 100.0, 100.0, 100.0, 1, 600.0).getTeamLuck()
        rawTeamLuckTeam2 = SslCalculator(4.5, 4.5, 550.0, 150.0, 100.0, 7, 3600.0).getTeamLuck()
        rawTeamLuckTeam3 = SslCalculator(4.5, 2.5, 550.0, 150.0, 100.0, 7, 3600.0).getTeamLuck()
        self.assertIsInstance(rawTeamLuckTeam1, float)
        self.assertEqual(-100.0, rawTeamLuckTeam1)
        self.assertEqual(0.0, rawTeamLuckTeam2)
        self.assertEqual(-28.57, rawTeamLuckTeam3)


