import unittest

from packages.StatCalculators.SslCalculator import SslCalculator


class TestSslCalculator(unittest.TestCase):

    def test_getRawTeamScore(self):
        rawTeamScoreTeam1 = SslCalculator(0.0, 0.0, 100.0, 100.0, 100.0).getRawTeamScore()
        rawTeamScoreTeam2 = SslCalculator(4.5, 4.5, 120.0, 150.0, 100.0).getRawTeamScore()
        rawTeamScoreTeam3 = SslCalculator(4.5, 10.0, 120.0, 150.0, 100.0).getRawTeamScore()
        self.assertIsInstance(rawTeamScoreTeam1, float)
        self.assertEqual(40.0, rawTeamScoreTeam1)
        self.assertEqual(71.5, rawTeamScoreTeam2)
        self.assertEqual(71.5, rawTeamScoreTeam3)

    def test_getRawTeamSuccess(self):
        rawTeamSuccessTeam1 = SslCalculator(5.0, 5.0, 120.0, 150.0, 100.0).getRawTeamSuccess()
        rawTeamSuccessTeam2 = SslCalculator(1.0, 5.0, 120.0, 150.0, 100.0).getRawTeamSuccess()
        self.assertIsInstance(rawTeamSuccessTeam1, float)
        self.assertEqual(74.0, rawTeamSuccessTeam1)
        self.assertEqual(74.0, rawTeamSuccessTeam2)

    def test_getRawTeamLuck(self):
        rawTeamLuckTeam1 = SslCalculator(5.0, 5.0, 120.0, 150.0, 100.0).getRawTeamLuck()
        rawTeamLuckTeam2 = SslCalculator(1.0, 5.0, 120.0, 150.0, 100.0).getRawTeamLuck()
        rawTeamLuckTeam3 = SslCalculator(3.2, 1.0, 120.0, 150.0, 100.0).getRawTeamLuck()
        self.assertIsInstance(rawTeamLuckTeam1, float)
        self.assertEqual(0.0, rawTeamLuckTeam1)
        self.assertEqual(20.0, rawTeamLuckTeam2)
        self.assertEqual(-11.0, rawTeamLuckTeam3)


