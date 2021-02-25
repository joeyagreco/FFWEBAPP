import unittest

from packages.Verifiers.LeagueDictVerifier import LeagueDictVerifier


class TestLeagueDictVerifier(unittest.TestCase):

    def test_teamPlaysItself(self):
        dummyTeamA = {"teamId": 1, "teamName": "dummyTeamA"}
        dummyTeamB = {"teamId": 2, "teamName": "dummyTeamB"}
        dummyWeeks = [{"weekNumber": 1, "matchups": [{"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamA, "teamAScore": 100, "teamBScore": 100}]}]
        dummyYears = {"1234": {"year": 1234, "teams": [], "weeks": dummyWeeks}}
        self.assertEqual(True, LeagueDictVerifier.teamPlaysItself(dummyYears))
        dummyWeeks = [{"weekNumber": 1, "matchups": [{"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamB, "teamAScore": 100, "teamBScore": 101}]}]
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
