import unittest

from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel


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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        team1_2020 = LeagueModelNavigator.getTeamById(leagueModel, 2020, 1)
        self.assertEqual("team1", team1_2020.getTeamName())
        self.assertEqual(1, team1_2020.getTeamId())
        self.assertRaises(Exception, LeagueModelNavigator.getTeamById, leagueModel, 7)

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
        self.assertTrue(LeagueModelNavigator.teamsPlayInWeek(week1, 1, [2]))
        self.assertTrue(LeagueModelNavigator.teamsPlayInWeek(week1, 1, [2, 3]))
        self.assertFalse(LeagueModelNavigator.teamsPlayInWeek(week1, 1, [3]))
        self.assertFalse(LeagueModelNavigator.teamsPlayInWeek(week1, 1, [3, 4, 5]))

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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        self.assertTrue(LeagueModelNavigator.teamsPlayEachOther(leagueModel, [2020], 1, 2))
        self.assertFalse(LeagueModelNavigator.teamsPlayEachOther(leagueModel, [2020], 1, 3))

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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        team1GamesPlayed = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 1)
        team2GamesPlayed = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 2)
        team1GamesPlayed_1 = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 1, throughWeek=1)
        team1GamesPlayed_2 = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 1, throughWeek=2)
        team1GamesPlayed_vs2 = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 1, vsTeamIds=[2])
        team1GamesPlayed_vs3 = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 1, vsTeamIds=[3])
        team1GamesPlayed_only2 = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 1, onlyWeeks=[2])
        team1GamesPlayed_only1and2 = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 1, onlyWeeks=[1, 2])
        team1GamesPlayed_allParams = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 1, throughWeek=1,
                                                                            vsTeamIds=[2])
        nonTeamGamesPlayed = LeagueModelNavigator.gamesPlayedByTeam(leagueModel, [2020], 7)
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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        totalLeaguePoints1 = LeagueModelNavigator.totalLeaguePoints(leagueModel, [2020], throughWeek=1)
        totalLeaguePoints2 = LeagueModelNavigator.totalLeaguePoints(leagueModel, [2020], throughWeek=2)
        totalLeaguePoints1_1and2 = LeagueModelNavigator.totalLeaguePoints(leagueModel, [2020], onlyWeeks=[1, 2])
        totalLeaguePoints1_2 = LeagueModelNavigator.totalLeaguePoints(leagueModel, [2020], onlyWeeks=[2])
        totalLeaguePointsDefault = LeagueModelNavigator.totalLeaguePoints(leagueModel, [2020])
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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        totalTeamPoints1_1 = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, [2020], 1, throughWeek=1)
        totalTeamPoints1_2 = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, [2020], 1, throughWeek=2)
        totalTeamPoints1_vs2 = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, [2020], 1, vsTeamIds=[2])
        totalTeamPoints1_vs3 = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, [2020], 1, vsTeamIds=[3])
        totalTeamPoints1_only2 = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, [2020], 1, onlyWeeks=[2])
        totalTeamPoints1_only1and2 = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, [2020], 1,
                                                                                  onlyWeeks=[1, 2])
        totalTeamPoints1_allParams = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, [2020], 1, throughWeek=1,
                                                                                  vsTeamIds=[2])
        totalTeamPoints1_default = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, [2020], 1)
        self.assertEqual(100, totalTeamPoints1_1)
        self.assertEqual(200, totalTeamPoints1_2)
        self.assertEqual(200, totalTeamPoints1_vs2)
        self.assertEqual(0, totalTeamPoints1_vs3)
        self.assertEqual(100, totalTeamPoints1_only2)
        self.assertEqual(200, totalTeamPoints1_only1and2)
        self.assertEqual(100, totalTeamPoints1_allParams)
        self.assertEqual(200, totalTeamPoints1_default)

    def test_getGameOutcomeAsString(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)

        team1Outcome = LeagueModelNavigator.getGameOutcomeAsString(matchup1, 1)
        team2Outcome = LeagueModelNavigator.getGameOutcomeAsString(matchup1, 2)
        team3Outcome = LeagueModelNavigator.getGameOutcomeAsString(matchup2, 3)
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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        allScores1 = LeagueModelNavigator.getAllScoresInLeague(leagueModel, [2020], throughWeek=1)
        allScores2 = LeagueModelNavigator.getAllScoresInLeague(leagueModel, [2020], throughWeek=2)
        allScoresDefault = LeagueModelNavigator.getAllScoresInLeague(leagueModel, [2020])
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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        allScores1_1 = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, [2020], 1, throughWeek=1)
        allScores1_2 = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, [2020], 1, throughWeek=2)
        allScores1_vs2 = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, [2020], 1, vsTeamIds=[2])
        allScores1_vs3 = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, [2020], 1, vsTeamIds=[3])
        allScores1_only2 = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, [2020], 1, onlyWeeks=[2])
        allScores1_only1and2 = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, [2020], 1, onlyWeeks=[1, 2])
        allScores1_allParams = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, [2020], 1, throughWeek=1,
                                                                       vsTeamIds=[2])
        allScores1_default = LeagueModelNavigator.getAllScoresOfTeam(leagueModel, [2020], 1)
        self.assertIsInstance(allScores1_1, list)
        self.assertEqual(1, len(allScores1_1))
        self.assertEqual(2, len(allScores1_2))
        self.assertEqual(2, len(allScores1_default))
        self.assertEqual(100, allScores1_1[0])
        self.assertEqual(101, allScores1_2[1])
        self.assertEqual(2, len(allScores1_vs2))
        self.assertEqual(0, len(allScores1_vs3))
        self.assertEqual(1, len(allScores1_only2))
        self.assertEqual(2, len(allScores1_only1and2))
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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        numberOfWeeks = LeagueModelNavigator.getNumberOfWeeksInLeague(leagueModel, 2020)
        numberOfWeeksAsList = LeagueModelNavigator.getNumberOfWeeksInLeague(leagueModel, 2020, asList=True)
        self.assertIsInstance(numberOfWeeks, int)
        self.assertIsInstance(numberOfWeeksAsList, list)
        self.assertEqual(1, numberOfWeeks)
        self.assertEqual(1, numberOfWeeksAsList[0])

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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        allTeamIds = LeagueModelNavigator.getAllTeamIdsInLeague(leagueModel, 2020)
        allTeamIds_exclude1 = LeagueModelNavigator.getAllTeamIdsInLeague(leagueModel, 2020, excludeIds=[1])
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
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        weeks1_vs2 = LeagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 2020, 1, [2])
        weeks1_vs3 = LeagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 2020, 1, [3])
        weeks1_vs2and3 = LeagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 2020, 1, [2, 3])
        weeks1_vsNone = LeagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 2020, 1, [])
        weeks1_vs2_only1 = LeagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 2020, 1, [2], onlyWeeks=[1])
        weeks1_vs2_only2 = LeagueModelNavigator.getAllWeeksTeamsPlayEachOther(leagueModel, 2020, 1, [2], onlyWeeks=[2])
        self.assertIsInstance(weeks1_vs2, list)
        self.assertEqual(2, len(weeks1_vs2))
        self.assertEqual(0, len(weeks1_vs3))
        self.assertEqual(2, len(weeks1_vs2and3))
        self.assertEqual(0, len(weeks1_vsNone))
        self.assertEqual(1, len(weeks1_vs2_only1))
        self.assertEqual(1, len(weeks1_vs2_only2))

    def test_getListOfTeamScores(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 95.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 102, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year = YearModel(2020, teamList, weekList)
        yearDict = {"2020": year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        team1_all = LeagueModelNavigator.getListOfTeamScores(leagueModel, 2020, 1)
        team2_all = LeagueModelNavigator.getListOfTeamScores(leagueModel, 2020, 2)
        team1_through1 = LeagueModelNavigator.getListOfTeamScores(leagueModel, 2020, 1, throughWeek=1)
        team2_through1 = LeagueModelNavigator.getListOfTeamScores(leagueModel, 2020, 2, throughWeek=1)
        team1_andOpponent = LeagueModelNavigator.getListOfTeamScores(leagueModel, 2020, 1, andOpponentScore=True)
        self.assertIsInstance(team1_all, list)
        self.assertEqual(2, len(team1_all))
        self.assertEqual(100, team1_all[0])
        self.assertEqual(100.5, team2_all[1])
        self.assertEqual(1, len(team1_through1))
        self.assertEqual(100, team1_through1[0])
        self.assertEqual(95.5, team2_through1[0])
        self.assertIsInstance(team1_andOpponent, list)
        self.assertIsInstance(team1_andOpponent[0], tuple)
        self.assertEqual(2, len(team1_andOpponent))
        self.assertEqual(team1_andOpponent[0][0], 100)
        self.assertEqual(team1_andOpponent[0][1], 95.5)

    def test_getListOfYearsInLeague(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 95.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 102, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        listOfYearsAsInts = LeagueModelNavigator.getListOfYearsInLeague(leagueModel, asInts=True)
        listOfYearsAsObjects = LeagueModelNavigator.getListOfYearsInLeague(leagueModel)
        self.assertEqual(1, len(listOfYearsAsInts))
        self.assertEqual(2020, listOfYearsAsInts[0])
        self.assertEqual(1, len(listOfYearsAsObjects))
        self.assertEqual(2020, listOfYearsAsObjects[0].getYear())

    def test_getDictOfYearModelsWithoutZero(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 95.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 102, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year = YearModel(2020, teamList, weekList)
        yearDict = {0: None, 2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        yearsWithoutZero = LeagueModelNavigator.getDictOfYearModelsWithoutZero(leagueModel)
        self.assertEqual(1, len(yearsWithoutZero))
        self.assertIsInstance(yearsWithoutZero[2020], YearModel)

    def test_getAllYearsWithWeeks(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 95.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 102, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year = YearModel(2020, teamList, weekList)
        year0 = YearModel(0, [], None)
        yearDict = {0: year0, 2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        yearsWithWeeks = LeagueModelNavigator.getAllYearsWithWeeks(leagueModel)
        yearsWithWeeksInt = LeagueModelNavigator.getAllYearsWithWeeks(leagueModel, asInts=True)
        self.assertEqual(1, len(yearsWithWeeks))
        self.assertEqual(2020, yearsWithWeeks[0].getYear())
        self.assertEqual(1, len(yearsWithWeeksInt))
        self.assertEqual(2020, yearsWithWeeksInt[0])

    def test_getMostRecentYear(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.6, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.6, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2021 = YearModel(2021, teamList, weekList)
        yearDict = {2020: year2020, 2021: year2021}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        mostRecent_default = LeagueModelNavigator.getMostRecentYear(leagueModel)
        mostRecent_asInt = LeagueModelNavigator.getMostRecentYear(leagueModel, asInt=True)
        mostRecent_withWeeks = LeagueModelNavigator.getMostRecentYear(leagueModel, withWeeks=True)
        mostRecent_asInt_withWeeks = LeagueModelNavigator.getMostRecentYear(leagueModel, asInt=True, withWeeks=True)
        self.assertIsInstance(mostRecent_default, YearModel)
        self.assertEqual(2021, mostRecent_default.getYear())
        self.assertIsInstance(mostRecent_asInt, int)
        self.assertEqual(2021, mostRecent_asInt)
        self.assertIsInstance(mostRecent_withWeeks, YearModel)
        self.assertEqual(2021, mostRecent_withWeeks.getYear())
        self.assertIsInstance(mostRecent_asInt_withWeeks, int)
        self.assertEqual(2021, mostRecent_asInt_withWeeks)

        year2022 = YearModel(2022, teamList, [])
        yearDict = {2020: year2020, 2021: year2021, 2022: year2022}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        mostRecent_withEmptyYear = LeagueModelNavigator.getMostRecentYear(leagueModel)
        mostRecent_withEmptyYear_withWeeks = LeagueModelNavigator.getMostRecentYear(leagueModel, withWeeks=True)
        mostRecent_withEmptyYear_withWeeks_asInt = LeagueModelNavigator.getMostRecentYear(leagueModel, asInt=True,
                                                                                          withWeeks=True)
        self.assertIsInstance(mostRecent_withEmptyYear, YearModel)
        self.assertEqual(2022, mostRecent_withEmptyYear.getYear())
        self.assertIsInstance(mostRecent_withEmptyYear_withWeeks, YearModel)
        self.assertEqual(2021, mostRecent_withEmptyYear_withWeeks.getYear())
        self.assertIsInstance(mostRecent_withEmptyYear_withWeeks_asInt, int)
        self.assertEqual(2021, mostRecent_withEmptyYear_withWeeks_asInt)
