import unittest

from packages.Verifiers.LeagueDictVerifier import LeagueDictVerifier


class TestLeagueDictVerifier(unittest.TestCase):

    def test_teamPlaysItself(self):
        leagueDictVerifier = LeagueDictVerifier()
        dummyTeamA = {"teamId": 1, "teamName": "dummyTeamA"}
        dummyTeamB = {"teamId": 2, "teamName": "dummyTeamB"}
        dummyWeek = [{"weekNumber": 1, "matchups": [
            {"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamA, "teamAScore": 100, "teamBScore": 100}]}]
        self.assertEqual(True, leagueDictVerifier.teamPlaysItself(dummyWeek))
        dummyWeek = [{"weekNumber": 1, "matchups": [
            {"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamB, "teamAScore": 100, "teamBScore": 101}]}]
        self.assertEqual(False, leagueDictVerifier.teamPlaysItself(dummyWeek))

    def test_teamPlaysTwice(self):
        leagueDictVerifier = LeagueDictVerifier()
        dummyTeamA = {"teamId": 1, "teamName": "dummyTeamA"}
        dummyTeamB = {"teamId": 2, "teamName": "dummyTeamB"}
        dummyTeamC = {"teamId": 3, "teamName": "dummyTeamC"}
        dummyTeamD = {"teamId": 4, "teamName": "dummyTeamD"}
        dummyWeek = [{"weekNumber": 1, "matchups": [
            {"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamB, "teamAScore": 100, "teamBScore": 101},
            {"matchupId": 2, "teamA": dummyTeamA, "teamB": dummyTeamC, "teamAScore": 100, "teamBScore": 102}]}]
        self.assertEqual(True, leagueDictVerifier.teamPlaysTwice(dummyWeek))
        dummyWeek = [{"weekNumber": 1, "matchups": [
            {"matchupId": 1, "teamA": dummyTeamA, "teamB": dummyTeamB, "teamAScore": 100, "teamBScore": 101},
            {"matchupId": 2, "teamA": dummyTeamC, "teamB": dummyTeamD, "teamAScore": 102, "teamBScore": 103}]}]
        self.assertEqual(False, leagueDictVerifier.teamPlaysTwice(dummyWeek))
