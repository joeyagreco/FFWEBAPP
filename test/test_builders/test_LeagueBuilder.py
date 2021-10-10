import unittest

from builders.LeagueBuilder import LeagueBuilder


class TestLeagueBuilder(unittest.TestCase):

    def test_getLeagueObjectId(self):
        leagueDict = {"_id": 123456, "leagueName": "test", "numberOfTeams": 6,
                      "years": {"1234": {"year": 1234, "teams": [], "weeks": []}}}
        leagueObject = LeagueBuilder(leagueDict).getLeagueObject()
        leagueId = leagueObject.leagueId
        self.assertEqual(123456, leagueId)

    def test_getLeagueObjectName(self):
        leagueDict = {"_id": 123456, "leagueName": "test", "numberOfTeams": 6,
                      "years": {"1234": {"year": 1234, "teams": [], "weeks": []}}}
        leagueObject = LeagueBuilder(leagueDict).getLeagueObject()
        leagueName = leagueObject.leagueName
        self.assertEqual("test", leagueName)

    def test_getLeagueObjectNumberOfTeams(self):
        leagueDict = {"_id": 123456, "leagueName": "test", "numberOfTeams": 6,
                      "years": {"1234": {"year": 1234, "teams": [], "weeks": []}}}
        leagueObject = LeagueBuilder(leagueDict).getLeagueObject()
        leagueNumberOfTeams = leagueObject.numberOfTeams
        self.assertEqual(6, leagueNumberOfTeams)

    def test_getLeagueObjectTeams(self):
        team1 = {"teamId": 1, "teamName": "team1"}
        team2 = {"teamId": 2, "teamName": "team2"}
        team3 = {"teamId": 3, "teamName": "team3"}
        team4 = {"teamId": 4, "teamName": "team4"}
        team5 = {"teamId": 5, "teamName": "team5"}
        team6 = {"teamId": 6, "teamName": "team6"}
        teamList = [team1, team2, team3, team4, team5, team6]
        leagueDict = {"_id": 123456, "leagueName": "test", "numberOfTeams": 6,
                      "years": {"1234": {"year": 1234, "teams": teamList, "weeks": []}}}
        leagueObject = LeagueBuilder(leagueDict).getLeagueObject()
        leagueTeams = leagueObject.years["1234"].getTeams()
        self.assertEqual(1, leagueTeams[0].getTeamId())
        self.assertEqual("team1", leagueTeams[0].getTeamName())
        self.assertEqual(6, len(leagueTeams))

    def test_getLeagueObjectWeeks(self):
        team1 = {"teamId": 1, "teamName": "team1"}
        team2 = {"teamId": 2, "teamName": "team2"}
        team3 = {"teamId": 3, "teamName": "team3"}
        team4 = {"teamId": 4, "teamName": "team4"}
        team5 = {"teamId": 5, "teamName": "team5"}
        team6 = {"teamId": 6, "teamName": "team6"}
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = {"matchupId": 1, "teamA": team1, "teamB": team2, "teamAScore": 100, "teamBScore": 101}
        matchup2 = {"matchupId": 2, "teamA": team3, "teamB": team4, "teamAScore": 102, "teamBScore": 103}
        matchup3 = {"matchupId": 3, "teamA": team5, "teamB": team6, "teamAScore": 104, "teamBScore": 105}
        matchupList = [matchup1, matchup2, matchup3]
        week1 = {"weekNumber": 1, "matchups": matchupList}
        leagueDict = {"_id": 123456, "leagueName": "test", "numberOfTeams": 6,
                      "years": {"1234": {"year": 1234, "teams": teamList, "weeks": [week1]}}}
        leagueObject = LeagueBuilder(leagueDict).getLeagueObject()
        leagueWeeks = leagueObject.years["1234"].getWeeks()
        self.assertEqual(1, leagueWeeks[0].getWeekNumber())
        self.assertEqual(1, len(leagueWeeks))
        self.assertEqual(3, len(leagueWeeks[0].getMatchups()))
        self.assertEqual(1, leagueWeeks[0].getMatchups()[0].getMatchupId())
        self.assertEqual(1, leagueWeeks[0].getMatchups()[0].getTeamA().getTeamId())
        self.assertEqual("team1", leagueWeeks[0].getMatchups()[0].getTeamA().getTeamName())
        self.assertEqual(2, leagueWeeks[0].getMatchups()[0].getTeamB().getTeamId())
        self.assertEqual("team2", leagueWeeks[0].getMatchups()[0].getTeamB().getTeamName())
        self.assertEqual(100, leagueWeeks[0].getMatchups()[0].getTeamAScore())
        self.assertEqual(101, leagueWeeks[0].getMatchups()[0].getTeamBScore())
