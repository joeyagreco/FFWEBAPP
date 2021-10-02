import unittest

from packages.Verifiers.LeagueDictVerifier import LeagueDictVerifier


class TestLeagueDictVerifier(unittest.TestCase):

    def test_teamPlaysItself(self):
        dummyTeamA = {"teamId": 1, "teamName": "dummyTeamA"}
        dummyTeamB = {"teamId": 2, "teamName": "dummyTeamB"}
        dummyWeeks = [{"weekNumber": 1, "matchups": [
            {"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamA, "teamAScore": 100, "teamBScore": 100}]}]
        dummyYears = {"1234": {"year": 1234, "teams": [], "weeks": dummyWeeks}}
        self.assertEqual(True, LeagueDictVerifier.teamPlaysItself(dummyYears))
        dummyWeeks = [{"weekNumber": 1, "matchups": [
            {"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamB, "teamAScore": 100, "teamBScore": 101}]}]
        dummyYears = {"1234": {"year": 1234, "teams": [], "weeks": dummyWeeks}}
        self.assertEqual(False, LeagueDictVerifier.teamPlaysItself(dummyYears))

    def test_teamPlaysTwice(self):
        dummyTeamA = {"teamId": 1, "teamName": "dummyTeamA"}
        dummyTeamB = {"teamId": 2, "teamName": "dummyTeamB"}
        dummyTeamC = {"teamId": 3, "teamName": "dummyTeamC"}
        dummyTeamD = {"teamId": 4, "teamName": "dummyTeamD"}
        dummyWeeks = [{"weekNumber": 1, "matchups": [
            {"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamB, "teamAScore": 100, "teamBScore": 101},
            {"matchupId": 2, "teamA": dummyTeamA, "teamB": dummyTeamC, "teamAScore": 100, "teamBScore": 102}]}]
        dummyYears = {"1234": {"year": 1234, "teams": [], "weeks": dummyWeeks}}
        self.assertEqual(True, LeagueDictVerifier.teamPlaysTwice(dummyYears))
        dummyWeeks = [{"weekNumber": 1, "matchups": [
            {"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamB, "teamAScore": 100, "teamBScore": 101},
            {"matchupId": 2, "teamA": dummyTeamC, "teamB": dummyTeamD, "teamAScore": 102, "teamBScore": 103}]}]
        dummyYears = {"1234": {"year": 1234, "teams": [], "weeks": dummyWeeks}}
        self.assertEqual(False, LeagueDictVerifier.teamPlaysTwice(dummyYears))

    def test_duplicateTeamNamesLowerCaseDuplicate(self):
        dummyTeams = [{"teamId": 1, "teamName": "a"}, {"teamId": 2, "teamName": "a"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(True, LeagueDictVerifier.duplicateTeamNames(dummyYears))
        dummyTeams = [{"teamId": 1, "teamName": "a"}, {"teamId": 2, "teamName": "b"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(False, LeagueDictVerifier.duplicateTeamNames(dummyYears))

    def test_duplicateTeamNamesUpperCaseDuplicate(self):
        dummyTeams = [{"teamId": 1, "teamName": "A"}, {"teamId": 2, "teamName": "A"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(True, LeagueDictVerifier.duplicateTeamNames(dummyYears))
        dummyTeams = [{"teamId": 1, "teamName": "A"}, {"teamId": 2, "teamName": "B"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(False, LeagueDictVerifier.duplicateTeamNames(dummyYears))

    def test_duplicateTeamNamesMixedCaseDuplicate(self):
        dummyTeams = [{"teamId": 1, "teamName": "Ab"}, {"teamId": 2, "teamName": "aB"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(True, LeagueDictVerifier.duplicateTeamNames(dummyYears))
        dummyTeams = [{"teamId": 1, "teamName": "Ab"}, {"teamId": 2, "teamName": "bC"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(False, LeagueDictVerifier.duplicateTeamNames(dummyYears))

    def test_duplicateTeamNamesWhiteSpace(self):
        dummyTeams1 = [{"teamId": 1, "teamName": "a "}, {"teamId": 2, "teamName": "a"}]
        dummyYears1 = {"1234": {"year": 1234, "teams": dummyTeams1, "weeks": []}}
        dummyTeams2 = [{"teamId": 1, "teamName": " a"}, {"teamId": 2, "teamName": "a"}]
        dummyYears2 = {"1234": {"year": 1234, "teams": dummyTeams2, "weeks": []}}
        dummyTeams3 = [{"teamId": 1, "teamName": " a "}, {"teamId": 2, "teamName": "a"}]
        dummyYears3 = {"1234": {"year": 1234, "teams": dummyTeams3, "weeks": []}}
        self.assertEqual(True, LeagueDictVerifier.duplicateTeamNames(dummyYears1))
        self.assertEqual(True, LeagueDictVerifier.duplicateTeamNames(dummyYears2))
        self.assertEqual(True, LeagueDictVerifier.duplicateTeamNames(dummyYears3))
        dummyTeams = [{"teamId": 1, "teamName": " a "}, {"teamId": 2, "teamName": "b"}]
        dummyYears = {"1234": {"year": 1234, "teams": dummyTeams, "weeks": []}}
        self.assertEqual(False, LeagueDictVerifier.duplicateTeamNames(dummyYears))
