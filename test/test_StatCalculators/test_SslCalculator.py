import unittest

from packages.StatCalculators.SslCalculator import SslCalculator


class TestSslCalculator(unittest.TestCase):

    def test_getRawTeamScore(self):
        rawTeamScoreTeam1 = SslCalculator(0.0, 0.0, 100.0, 100.0, 100.0, 1).getRawTeamScore()
        rawTeamScoreTeam2 = SslCalculator(4.5, 4.5, 120.0, 150.0, 100.0, 7).getRawTeamScore()
        rawTeamScoreTeam3 = SslCalculator(4.5, 10.0, 120.0, 150.0, 100.0, 15).getRawTeamScore()
        self.assertIsInstance(rawTeamScoreTeam1, float)
        self.assertEqual(40.0, rawTeamScoreTeam1)
        self.assertEqual(113.3, rawTeamScoreTeam2)
        self.assertEqual(79.0, rawTeamScoreTeam3)

    def test_getRawTeamSuccess(self):
        rawTeamSuccessTeam1 = SslCalculator(5.0, 5.0, 120.0, 150.0, 100.0, 5).getRawTeamSuccess()
        rawTeamSuccessTeam2 = SslCalculator(1.0, 5.0, 120.0, 150.0, 100.0, 6).getRawTeamSuccess()
        self.assertIsInstance(rawTeamSuccessTeam1, float)
        self.assertEqual(149.0, rawTeamSuccessTeam1)
        self.assertEqual(132.3, rawTeamSuccessTeam2)

    def test_getRawTeamLuck(self):
        rawTeamLuckTeam1 = SslCalculator(5.0, 5.0, 120.0, 150.0, 100.0, 5).getRawTeamLuck()
        rawTeamLuckTeam2 = SslCalculator(1.0, 5.0, 120.0, 150.0, 100.0, 5).getRawTeamLuck()
        rawTeamLuckTeam3 = SslCalculator(3.2, 1.0, 120.0, 150.0, 100.0, 5).getRawTeamLuck()
        self.assertIsInstance(rawTeamLuckTeam1, float)
        self.assertEqual(0.0, rawTeamLuckTeam1)
        self.assertEqual(80.0, rawTeamLuckTeam2)
        self.assertEqual(-44.0, rawTeamLuckTeam3)


