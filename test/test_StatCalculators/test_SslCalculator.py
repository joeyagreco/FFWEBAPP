import unittest

from packages.StatCalculators.SslCalculator import SslCalculator


class TestSslCalculator(unittest.TestCase):

    def test_getTeamScore(self):
        rawTeamScoreTeam1 = SslCalculator(0.0, 0.0, 16.67, 100.0, 100.0, 1).getTeamScore()
        rawTeamScoreTeam2 = SslCalculator(4.5, 4.5, 15.28, 150.0, 100.0, 7).getTeamScore()
        rawTeamScoreTeam3 = SslCalculator(2.5, 4.5, 15.28, 150.0, 100.0, 7).getTeamScore()
        self.assertIsInstance(rawTeamScoreTeam1, float)
        self.assertEqual(43.34, rawTeamScoreTeam1)
        self.assertEqual(107.35, rawTeamScoreTeam2)
        self.assertEqual(78.77, rawTeamScoreTeam3)

    def test_getTeamSuccess(self):
        rawTeamSuccessTeam1 = SslCalculator(0.0, 0.0, 16.67, 100.0, 100.0, 1).getTeamSuccess()
        rawTeamSuccessTeam2 = SslCalculator(4.5, 4.5, 15.28, 150.0, 100.0, 7).getTeamSuccess()
        rawTeamSuccessTeam3 = SslCalculator(2.5, 4.5, 15.28, 150.0, 100.0, 7).getTeamSuccess()
        self.assertIsInstance(rawTeamSuccessTeam1, float)
        self.assertEqual(43.34, rawTeamSuccessTeam1)
        self.assertEqual(107.35, rawTeamSuccessTeam2)
        self.assertEqual(107.35, rawTeamSuccessTeam3)

    def test_getTeamLuck(self):
        rawTeamLuckTeam1 = SslCalculator(0.0, 0.0, 16.67, 100.0, 100.0, 1).getTeamLuck()
        rawTeamLuckTeam2 = SslCalculator(4.5, 4.5, 15.28, 150.0, 100.0, 7).getTeamLuck()
        rawTeamLuckTeam3 = SslCalculator(2.5, 4.5, 15.28, 150.0, 100.0, 7).getTeamLuck()
        self.assertIsInstance(rawTeamLuckTeam1, float)
        self.assertEqual(0, rawTeamLuckTeam1)
        self.assertEqual(0, rawTeamLuckTeam2)
        self.assertEqual(28.57, rawTeamLuckTeam3)


