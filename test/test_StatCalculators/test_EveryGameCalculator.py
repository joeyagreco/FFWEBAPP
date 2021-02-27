import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
from models.league_stat_models.MarginOfVictoryModel import MarginOfVictoryModel
from models.league_stat_models.ScoreModel import ScoreModel
from packages.StatCalculators.EveryGameCalculator import EveryGameCalculator


class TestEveryGameCalculator(unittest.TestCase):

    def test_getAllMarginOfVictories(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 105, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        everyGameCalculator = EveryGameCalculator(leagueModel, [2020])
        movs = everyGameCalculator.getAllMarginOfVictories()
        self.assertEqual(1, len(movs))
        self.assertIsInstance(movs[0], MarginOfVictoryModel)
        self.assertEqual(0.5, movs[0].getMarginOfVictory())
        self.assertEqual(team2, movs[0].getWinningTeam())
        self.assertEqual(100.5, movs[0].getWinningTeamPoints())
        self.assertEqual(team1, movs[0].getLosingTeam())
        self.assertEqual(100, movs[0].getLosingTeamPoints())
        self.assertEqual(1, movs[0].getWeek())

    def test_getAllScores(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 101, 101)
        matchup3 = MatchupModel(3, team5, team6, 105, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        everyGameCalculator = EveryGameCalculator(leagueModel, [2020])
        allScores = everyGameCalculator.getAllScores()
        self.assertEqual(6, len(allScores))
        self.assertIsInstance(allScores[0], ScoreModel)



