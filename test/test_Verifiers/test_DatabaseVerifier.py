import unittest
from packages.Verifiers.DatabaseVerifier import DatabaseVerifier


class TestDatabaseVerifier(unittest.TestCase):

    def test_duplicateTeamNamesLowerCaseDuplicate(self):
        dummyTeams = [{"teamId": 1, "teamName": "a"}, {"teamId": 2, "teamName": "a"}]
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyTeams))
        dummyTeams = [{"teamId": 1, "teamName": "a"}, {"teamId": 2, "teamName": "b"}]
        self.assertEqual(False, DatabaseVerifier.duplicateTeamNames(dummyTeams))

    def test_duplicateTeamNamesUpperCaseDuplicate(self):
        dummyTeams = [{"teamId": 1, "teamName": "A"}, {"teamId": 2, "teamName": "A"}]
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyTeams))
        dummyTeams = [{"teamId": 1, "teamName": "A"}, {"teamId": 2, "teamName": "B"}]
        self.assertEqual(False, DatabaseVerifier.duplicateTeamNames(dummyTeams))

    def test_duplicateTeamNamesMixedCaseDuplicate(self):
        dummyTeams = [{"teamId": 1, "teamName": "Ab"}, {"teamId": 2, "teamName": "aB"}]
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyTeams))
        dummyTeams = [{"teamId": 1, "teamName": "Ab"}, {"teamId": 2, "teamName": "bC"}]
        self.assertEqual(False, DatabaseVerifier.duplicateTeamNames(dummyTeams))

    def test_duplicateTeamNamesWhiteSpace(self):
        dummyTeams1 = [{"teamId": 1, "teamName": "a "}, {"teamId": 2, "teamName": "a"}]
        dummyTeams2 = [{"teamId": 1, "teamName": " a"}, {"teamId": 2, "teamName": "a"}]
        dummyTeams3 = [{"teamId": 1, "teamName": " a "}, {"teamId": 2, "teamName": "a"}]
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyTeams1))
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyTeams2))
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyTeams3))
        dummyTeams1 = [{"teamId": 1, "teamName": " a "}, {"teamId": 2, "teamName": "b"}]
        self.assertEqual(False, DatabaseVerifier.duplicateTeamNames(dummyTeams1))
