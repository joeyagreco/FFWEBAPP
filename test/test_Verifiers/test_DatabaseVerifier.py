import unittest
from packages.Verifiers.DatabaseVerifier import DatabaseVerifier


class TestDatabaseVerifier(unittest.TestCase):

    def test_duplicateTeamNamesLowerCaseDuplicate(self):
        dummyTeams = [{"teamId": 1, "teamName": "a"}, {"teamId": 2, "teamName": "a"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyYears))
        dummyTeams = [{"teamId": 1, "teamName": "a"}, {"teamId": 2, "teamName": "b"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(False, DatabaseVerifier.duplicateTeamNames(dummyYears))

    def test_duplicateTeamNamesUpperCaseDuplicate(self):
        dummyTeams = [{"teamId": 1, "teamName": "A"}, {"teamId": 2, "teamName": "A"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyYears))
        dummyTeams = [{"teamId": 1, "teamName": "A"}, {"teamId": 2, "teamName": "B"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(False, DatabaseVerifier.duplicateTeamNames(dummyYears))

    def test_duplicateTeamNamesMixedCaseDuplicate(self):
        dummyTeams = [{"teamId": 1, "teamName": "Ab"}, {"teamId": 2, "teamName": "aB"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyYears))
        dummyTeams = [{"teamId": 1, "teamName": "Ab"}, {"teamId": 2, "teamName": "bC"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(False, DatabaseVerifier.duplicateTeamNames(dummyYears))

    def test_duplicateTeamNamesWhiteSpace(self):
        dummyTeams1 = [{"teamId": 1, "teamName": "a "}, {"teamId": 2, "teamName": "a"}]
        dummyYears1 = {"1234": {"year": 1234, "teams": dummyTeams1, "weeks": []}}
        dummyTeams2 = [{"teamId": 1, "teamName": " a"}, {"teamId": 2, "teamName": "a"}]
        dummyYears2 = {"1234": {"year": 1234, "teams": dummyTeams2, "weeks": []}}
        dummyTeams3 = [{"teamId": 1, "teamName": " a "}, {"teamId": 2, "teamName": "a"}]
        dummyYears3 = {"1234": {"year": 1234, "teams": dummyTeams3, "weeks": []}}
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyYears1))
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyYears2))
        self.assertEqual(True, DatabaseVerifier.duplicateTeamNames(dummyYears3))
        dummyTeams = [{"teamId": 1, "teamName": " a "}, {"teamId": 2, "teamName": "b"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(False, DatabaseVerifier.duplicateTeamNames(dummyYears))
