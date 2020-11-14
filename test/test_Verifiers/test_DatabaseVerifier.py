import unittest
from packages.Verifiers.DatabaseVerifier import DatabaseVerifier


class TestDatabaseVerifier(unittest.TestCase):

    def test_duplicateTeamNamesLowerCaseDuplicate(self):
        databaseVerifier = DatabaseVerifier()
        dummyTeams = [{"teamId": 1, "teamName": "a"}, {"teamId": 2, "teamName": "a"}]
        self.assertEqual(True, databaseVerifier.duplicateTeamNames(dummyTeams))

    def test_duplicateTeamNamesUpperCaseDuplicate(self):
        databaseVerifier = DatabaseVerifier()
        dummyTeams = [{"teamId": 1, "teamName": "A"}, {"teamId": 2, "teamName": "A"}]
        self.assertEqual(True, databaseVerifier.duplicateTeamNames(dummyTeams))

    def test_duplicateTeamNamesMixedCaseDuplicate(self):
        databaseVerifier = DatabaseVerifier()
        dummyTeams = [{"teamId": 1, "teamName": "Ab"}, {"teamId": 2, "teamName": "aB"}]
        self.assertEqual(True, databaseVerifier.duplicateTeamNames(dummyTeams))

    def test_duplicateTeamNamesWhiteSpace(self):
        databaseVerifier = DatabaseVerifier()
        dummyTeams1 = [{"teamId": 1, "teamName": "a "}, {"teamId": 2, "teamName": "a"}]
        dummyTeams2 = [{"teamId": 1, "teamName": " a"}, {"teamId": 2, "teamName": "a"}]
        dummyTeams3 = [{"teamId": 1, "teamName": " a "}, {"teamId": 2, "teamName": "a"}]
        self.assertEqual(True, databaseVerifier.duplicateTeamNames(dummyTeams1))
        self.assertEqual(True, databaseVerifier.duplicateTeamNames(dummyTeams2))
        self.assertEqual(True, databaseVerifier.duplicateTeamNames(dummyTeams3))
