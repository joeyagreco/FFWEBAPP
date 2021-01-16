import unittest

from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel


class TestLeagueModelNavigator(unittest.TestCase):

    def test_getTeamById(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)

        leagueModelNavigator = LeagueModelNavigator()
        team1 = leagueModelNavigator.getTeamById(leagueModel, 1)
        self.assertEqual("team1", team1.getTeamName())
        self.assertEqual(1, team1.getTeamId())
        self.assertRaises(Exception, leagueModelNavigator.getTeamById, leagueModel, 7)

    def test_teamsPlayInWeek(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)

        leagueModelNavigator = LeagueModelNavigator()
        self.assertTrue(leagueModelNavigator.teamsPlayInWeek(week1, 1, [2]))
        self.assertTrue(leagueModelNavigator.teamsPlayInWeek(week1, 1, [2, 3]))
        self.assertFalse(leagueModelNavigator.teamsPlayInWeek(week1, 1, [3]))
        self.assertFalse(leagueModelNavigator.teamsPlayInWeek(week1, 1, [3, 4, 5]))

    def test_teamsPlayEachOther(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)

        leagueModelNavigator = LeagueModelNavigator()
        self.assertTrue(leagueModelNavigator.teamsPlayEachOther(leagueModel, 1, 2))
        self.assertFalse(leagueModelNavigator.teamsPlayEachOther(leagueModel, 1, 3))

    def test_gamesPlayedByTeam(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        leagueModelNavigator = LeagueModelNavigator()
        team1GamesPlayed = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 1)
        team2GamesPlayed = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 2)
        team1GamesPlayed_1 = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 1, throughWeek=1)
        team1GamesPlayed_2 = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 1, throughWeek=2)
        team1GamesPlayed_vs2 = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 1, vsTeamIds=[2])
        team1GamesPlayed_vs3 = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 1, vsTeamIds=[3])
        team1GamesPlayed_only2 = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 1, onlyWeeks=[2])
        team1GamesPlayed_only1and2 = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 1, onlyWeeks=[1, 2])
        team1GamesPlayed_allParams = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 1, throughWeek=1, vsTeamIds=[2])
        nonTeamGamesPlayed = leagueModelNavigator.gamesPlayedByTeam(leagueModel, 7)
        self.assertEqual(2, team1GamesPlayed)
        self.assertEqual(2, team2GamesPlayed)
        self.assertEqual(1, team1GamesPlayed_1)
        self.assertEqual(2, team1GamesPlayed_2)
        self.assertEqual(2, team1GamesPlayed_vs2)
        self.assertEqual(0, team1GamesPlayed_vs3)
        self.assertEqual(1, team1GamesPlayed_only2)
        self.assertEqual(2, team1GamesPlayed_only1and2)
        self.assertEqual(1, team1GamesPlayed_allParams)
        self.assertEqual(0, nonTeamGamesPlayed)

    def test_totalLeaguePoints(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        leagueModelNavigator = LeagueModelNavigator()
        totalLeaguePoints1 = leagueModelNavigator.totalLeaguePoints(leagueModel, throughWeek=1)
        totalLeaguePoints2 = leagueModelNavigator.totalLeaguePoints(leagueModel, throughWeek=2)
        totalLeaguePoints1_1and2 = leagueModelNavigator.totalLeaguePoints(leagueModel, onlyIncludeWeeks=[1, 2])
        totalLeaguePoints1_2 = leagueModelNavigator.totalLeaguePoints(leagueModel, onlyIncludeWeeks=[2])
        totalLeaguePointsDefault = leagueModelNavigator.totalLeaguePoints(leagueModel)
        self.assertEqual(510.5, totalLeaguePoints1)
        self.assertEqual(1021, totalLeaguePoints2)
        self.assertEqual(1021, totalLeaguePoints1_1and2)
        self.assertEqual(510.5, totalLeaguePoints1_2)
        self.assertEqual(1021, totalLeaguePointsDefault)

    def test_totalPointsScoredByTeam(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        leagueModelNavigator = LeagueModelNavigator()
        totalTeamPoints1_1 = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, 1, throughWeek=1)
        totalTeamPoints1_2 = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, 1, throughWeek=2)
        totalTeamPoints1_vs2 = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, 1, vsTeamIds=[2])
        totalTeamPoints1_vs3 = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, 1, vsTeamIds=[3])
        totalTeamPoints1_allParams = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, 1, throughWeek=1, vsTeamIds=[2])
        totalTeamPoints1_default = leagueModelNavigator.totalPointsScoredByTeam(leagueModel, 1)
        self.assertEqual(100, totalTeamPoints1_1)
        self.assertEqual(200, totalTeamPoints1_2)
        self.assertEqual(200, totalTeamPoints1_vs2)
        self.assertEqual(0, totalTeamPoints1_vs3)
        self.assertEqual(100, totalTeamPoints1_allParams)
        self.assertEqual(200, totalTeamPoints1_default)

    def test_getGameOutcomeAsString(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)

        leagueModelNavigator = LeagueModelNavigator()
        team1Outcome = leagueModelNavigator.getGameOutcomeAsString(matchup1, 1)
        team2Outcome = leagueModelNavigator.getGameOutcomeAsString(matchup1, 2)
        team3Outcome = leagueModelNavigator.getGameOutcomeAsString(matchup2, 3)
        self.assertEqual("Loss", team1Outcome)
        self.assertEqual("Win", team2Outcome)
        self.assertEqual("Tie", team3Outcome)

    def test_getAllScoresInLeague(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        leagueModelNavigator = LeagueModelNavigator()
        allScores1 = leagueModelNavigator.getAllScoresInLeague(leagueModel, throughWeek=1)
        allScores2 = leagueModelNavigator.getAllScoresInLeague(leagueModel, throughWeek=2)
        allScoresDefault = leagueModelNavigator.getAllScoresInLeague(leagueModel)
        self.assertIsInstance(allScores1, list)
        self.assertEqual(6, len(allScores1))
        self.assertEqual(12, len(allScores2))
        self.assertEqual(12, len(allScoresDefault))

    def test_getAllScoresOfTeam(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 101, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        leagueModelNavigator = LeagueModelNavigator()
        allScores1_1 = leagueModelNavigator.getAllScoresOfTeam(leagueModel, 1, throughWeek=1)
        allScores1_2 = leagueModelNavigator.getAllScoresOfTeam(leagueModel, 1, throughWeek=2)
        allScores1_vs2 = leagueModelNavigator.getAllScoresOfTeam(leagueModel, 1, vsTeamIds=[2])
        allScores1_vs3 = leagueModelNavigator.getAllScoresOfTeam(leagueModel, 1, vsTeamIds=[3])
        allScores1_allParams = leagueModelNavigator.getAllScoresOfTeam(leagueModel, 1, throughWeek=1, vsTeamIds=[2])
        allScores1_default = leagueModelNavigator.getAllScoresOfTeam(leagueModel, 1)
        self.assertIsInstance(allScores1_1, list)
        self.assertEqual(1, len(allScores1_1))
        self.assertEqual(2, len(allScores1_2))
        self.assertEqual(2, len(allScores1_default))
        self.assertEqual(100, allScores1_1[0])
        self.assertEqual(101, allScores1_2[1])
        self.assertEqual(2, len(allScores1_vs2))
        self.assertEqual(0, len(allScores1_vs3))
        self.assertEqual(1, len(allScores1_allParams))
        self.assertEqual(101, allScores1_default[1])

    def test_getNumberOfWeeksInLeague(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)

        leagueModelNavigator = LeagueModelNavigator()
        numberOfWeeks = leagueModelNavigator.getNumberOfWeeksInLeague(leagueModel)
        self.assertIsInstance(numberOfWeeks, int)
        self.assertEqual(1, numberOfWeeks)

    def test_getAllTeamIdsInLeague(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)

        leagueModelNavigator = LeagueModelNavigator()
        allTeamIds = leagueModelNavigator.getAllTeamIdsInLeague(leagueModel)
        allTeamIds_exclude1 = leagueModelNavigator.getAllTeamIdsInLeague(leagueModel, excludeId=1)
        self.assertIsInstance(allTeamIds, list)
        self.assertEqual(6, len(allTeamIds))
        self.assertEqual(5, len(allTeamIds_exclude1))
        self.assertFalse(1 in allTeamIds_exclude1)

    def test_getAllWeeksTeamsPlayEachOther(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)
        leagueModelNavigator = LeagueModelNavigator()
        weeks1_vs2 = leagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 1, [2])
        weeks1_vs3 = leagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 1, [3])
        weeks1_vs2and3 = leagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 1, [2, 3])
        weeks1_vsNone = leagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 1, [])
        self.assertIsInstance(weeks1_vs2, list)
        self.assertEqual(2, len(weeks1_vs2))
        self.assertEqual(0, len(weeks1_vs3))
        self.assertEqual(2, len(weeks1_vs2and3))
        self.assertEqual(0, len(weeks1_vsNone))
