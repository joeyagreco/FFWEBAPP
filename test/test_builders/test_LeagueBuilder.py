import unittest

from builders.LeagueBuilder import LeagueBuilder
from models.league_models.TeamModel import TeamModel


class TestLeagueBuilder(unittest.TestCase):

    def test_getLeagueObjectId(self):
        leagueDict = {"_id": 123456, "leagueName": "test", "numberOfTeams": 6, "teams": [], "weeks": []}
        leagueObject = LeagueBuilder(leagueDict).getLeagueObject()
        leagueId = leagueObject.getLeagueId()
        self.assertEqual(123456, leagueId)

    def test_getLeagueObjectName(self):
        leagueDict = {"_id": 123456, "leagueName": "test", "numberOfTeams": 6, "teams": [], "weeks": []}
        leagueObject = LeagueBuilder(leagueDict).getLeagueObject()
        leagueName = leagueObject.getLeagueName()
        self.assertEqual("test", leagueName)

    def test_getLeagueObjectNumberOfTeams(self):
        leagueDict = {"_id": 123456, "leagueName": "test", "numberOfTeams": 6, "teams": [], "weeks": []}
        leagueObject = LeagueBuilder(leagueDict).getLeagueObject()
        leagueNumberOfTeams = leagueObject.getNumberOfTeams()
        self.assertEqual(6, leagueNumberOfTeams)

    def test_getLeagueObjectTeam(self):
        team1 = {"teamId": 1, "teamName": "team1"}
        team2 = {"teamId": 2, "teamName": "team2"}
        team3 = {"teamId": 3, "teamName": "team3"}
        team4 = {"teamId": 4, "teamName": "team4"}
        team5 = {"teamId": 5, "teamName": "team5"}
        team6 = {"teamId": 6, "teamName": "team6"}
        teamList = [team1, team2, team3, team4, team5, team6]
        leagueDict = {"_id": 123456, "leagueName": "test", "numberOfTeams": 6, "teams": teamList, "weeks": []}
        leagueObject = LeagueBuilder(leagueDict).getLeagueObject()
        leagueTeams = leagueObject.getTeams()
        self.assertEqual(1, leagueTeams[0].getTeamId())
        self.assertEqual("team1", leagueTeams[0].getTeamName())
