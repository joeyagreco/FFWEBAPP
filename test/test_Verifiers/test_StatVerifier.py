import unittest

from packages.Verifiers.StatVerifier import StatVerifier


class TestStatVerifier(unittest.TestCase):

    def test_comparingSameHeadToHeadTeam(self):
        statVerifier = StatVerifier()
        self.assertTrue(statVerifier.comparingSameHeadToHeadTeam(1, 1))
        self.assertFalse(statVerifier.comparingSameHeadToHeadTeam(1, 2))
