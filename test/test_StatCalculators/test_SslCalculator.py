import unittest

from packages.StatCalculators.SslCalculator import SslCalculator


class TestSslCalculator(unittest.TestCase):

    def test_getRawTeamScore(self):
        rawTeamScoreTeam1 = SslCalculator(0.0, 0.0, 100.0, 100.0, 100.0, 1, 600.0).getRawTeamScore()
        rawTeamScoreTeam2 = SslCalculator(4.5, 4.5, 550.0, 150.0, 100.0, 7, 3600.0).getRawTeamScore()
        rawTeamScoreTeam3 = SslCalculator(2.5, 4.5, 550.0, 150.0, 100.0, 7, 3600.0).getRawTeamScore()
        self.assertIsInstance(rawTeamScoreTeam1, float)
        self.assertEqual(23.3, rawTeamScoreTeam1)
        self.assertEqual(92.3, rawTeamScoreTeam2)
        self.assertEqual(63.8, rawTeamScoreTeam3)

    def test_getRawTeamSuccess(self):
        rawTeamSuccessTeam1 = SslCalculator(0.0, 0.0, 100.0, 100.0, 100.0, 1, 600.0).getRawTeamSuccess()
        rawTeamSuccessTeam2 = SslCalculator(4.5, 4.5, 550.0, 150.0, 100.0, 7, 3600.0).getRawTeamSuccess()
        rawTeamSuccessTeam3 = SslCalculator(4.5, 2.5, 550.0, 150.0, 100.0, 7, 3600.0).getRawTeamSuccess()
        self.assertIsInstance(rawTeamSuccessTeam1, float)
        self.assertEqual(23.3, rawTeamSuccessTeam1)
        self.assertEqual(92.3, rawTeamSuccessTeam2)
        self.assertEqual(63.8, rawTeamSuccessTeam3)

    def test_getRawTeamLuck(self):
        rawTeamLuckTeam1 = SslCalculator(1.0, 0.0, 100.0, 100.0, 100.0, 1, 600.0).getRawTeamLuck()
        rawTeamLuckTeam2 = SslCalculator(4.5, 4.5, 550.0, 150.0, 100.0, 7, 3600.0).getRawTeamLuck()
        rawTeamLuckTeam3 = SslCalculator(4.5, 2.5, 550.0, 150.0, 100.0, 7, 3600.0).getRawTeamLuck()
        self.assertIsInstance(rawTeamLuckTeam1, float)
        self.assertEqual(-100.0, rawTeamLuckTeam1)
        self.assertEqual(0.0, rawTeamLuckTeam2)
        self.assertEqual(-28.5, rawTeamLuckTeam3)


