from typing import List

from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel


class LeagueModelNavigator:

    def getTeamById(self, leagueModel: LeagueModel, teamId: int) -> TeamModel:
        """
        Returns a Team object for the team with the given ID in the given league.
        Throws Exception if a team with the given ID is not in the given league.
        """
        for team in leagueModel.getTeams():
            if team.getTeamId() == teamId:
                return team
        raise Exception("Given TeamID is not in the given LeagueModel")

    def teamsPlayInWeek(self, week: WeekModel, team1Id: int, opponentIds: list) -> bool:
        """
        Returns a boolean on whether teams with the given IDs play in the given week.
        """
        for matchup in week.getMatchups():
            if matchup.getTeamA().getTeamId() == team1Id and matchup.getTeamB().getTeamId() in opponentIds or matchup.getTeamB().getTeamId() == team1Id and matchup.getTeamA().getTeamId() in opponentIds:
                return True
        return False

    def teamsPlayEachOther(self, leagueModel: LeagueModel, team1Id: int, team2Id: int) -> bool:
        """
        Returns a boolean on whether the teams with the given IDs play at all in the given league.
        """
        for week in leagueModel.getWeeks():
            if self.teamsPlayInWeek(week, team1Id, [team2Id]):
                return True
        return False

    def gamesPlayedByTeam(self, leagueModel: LeagueModel, teamId: int, **params) -> int:
        """
        Returns as an int the number of games played in the given league by the team with the given ID.
        THROUGHWEEK: [int] Gives games played through that week.
        ONLYWEEKS: [list] Gives games played for the given week numbers.
        VSTEAMIDS: [list] Gives games played vs teams with the given IDs.
        """
        throughWeek = params.pop("throughWeek", self.getNumberOfWeeksInLeague(leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", self.getAllTeamIdsInLeague(leagueModel, excludeId=teamId))
        gamesPlayed = 0
        for week in leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == teamId and matchup.getTeamB().getTeamId() in vsTeamIds or matchup.getTeamB().getTeamId() == teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    gamesPlayed += 1
        return gamesPlayed

    def totalLeaguePoints(self, leagueModel: LeagueModel, **params) -> float:
        """
        Returns a float that is the total amount of points scored in the given league.
        THROUGHWEEK: [int] Gives total league points scored through that week.
        ONLYWEEKS: [list] Gives total league points for the given week numbers.
        """
        throughWeek = params.pop("throughWeek", self.getNumberOfWeeksInLeague(leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        rounder = Rounder()
        totalPoints = 0
        for week in leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                totalPoints += matchup.getTeamAScore()
                totalPoints += matchup.getTeamBScore()
        return rounder.normalRound(totalPoints, rounder.getDecimalPlacesRoundedToInScores(leagueModel))

    def totalPointsScoredByTeam(self, leagueModel: LeagueModel, teamId: int, **params) -> float:
        """
        Returns a float that is the total amount of points scored by the team with the given ID in the given league.
        THROUGHWEEK: [int] Gives total points scored through that week.
        ONLYWEEKS: [list] Gives total points for the given week numbers.
        VSTEAMIDS: [list] Gives total points vs teams with the given IDs.
        """
        throughWeek = params.pop("throughWeek", self.getNumberOfWeeksInLeague(leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", self.getAllTeamIdsInLeague(leagueModel, excludeId=teamId))
        rounder = Rounder()
        totalPoints = 0
        for week in leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    totalPoints += matchup.getTeamAScore()
                elif matchup.getTeamB().getTeamId() == teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    totalPoints += matchup.getTeamBScore()
        return rounder.normalRound(totalPoints, rounder.getDecimalPlacesRoundedToInScores(leagueModel))

    def getGameOutcomeAsString(self, matchup: MatchupModel, teamId: int):
        """
        Returns a string representation [win/loss/tie] of the outcome of the given game for the team with the given ID.
        Returns None if a team with the given ID does not play in this matchup.
        """
        if teamId != matchup.getTeamA().getTeamId() and teamId != matchup.getTeamB().getTeamId():
            # the given team doesn't play in the given matchup
            return None
        if teamId == matchup.getTeamA().getTeamId():
            # given team is team A
            isTeamA = True
        else:
            # given team is team B
            isTeamA = False
        if matchup.getTeamAScore() > matchup.getTeamBScore():
            if isTeamA:
                return "Win"
            return "Loss"
        elif matchup.getTeamAScore() < matchup.getTeamBScore():
            if isTeamA:
                return "Loss"
            return "Win"
        else:
            return "Tie"

    def getAllScoresInLeague(self, leagueModel: LeagueModel, **params) -> List[float]:
        """
        Returns as a list of floats all of the scores in the given leagueModel.
        Note: These scores will be properly rounded.
        THROUGHWEEK: [int] Gives all league scores through that week.
        ONLYWEEKS: [list] Gives all league scores for the given week numbers.
        """
        throughWeek = params.pop("throughWeek", self.getNumberOfWeeksInLeague(leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        rounder = Rounder()
        decimalPlacesToRoundTo = rounder.getDecimalPlacesRoundedToInScores(leagueModel)
        allScores = []
        for week in leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                scoreA = matchup.getTeamAScore()
                scoreB = matchup.getTeamBScore()
                scoreA = rounder.normalRound(scoreA, decimalPlacesToRoundTo)
                scoreB = rounder.normalRound(scoreB, decimalPlacesToRoundTo)
                allScores.append(scoreA)
                allScores.append(scoreB)
        return allScores

    def getAllScoresOfTeam(self, leagueModel: LeagueModel, teamId: int, **params) -> List[float]:
        """
        Returns as a list of floats all of the scores in the given leagueModel that the team with the given ID had.
        Note: These scores will be properly rounded.
        THROUGHWEEK: [int] Gives all scores through that week.
        ONLYWEEKS: [list] Gives all scores for the given week numbers.
        VSTEAMIDS: [list] Gives all scores vs teams with the given IDs.
        """
        throughWeek = params.pop("throughWeek", self.getNumberOfWeeksInLeague(leagueModel))
        onlyWeeks = params.pop("onlyWeeks", None)
        vsTeamIds = params.pop("vsTeamIds", self.getAllTeamIdsInLeague(leagueModel, excludeId=teamId))
        rounder = Rounder()
        decimalPlacesToRoundTo = rounder.getDecimalPlacesRoundedToInScores(leagueModel)
        allScores = []
        for week in leagueModel.getWeeks():
            if onlyWeeks and week.getWeekNumber() not in onlyWeeks:
                continue
            elif week.getWeekNumber() > throughWeek:
                break
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == teamId and matchup.getTeamB().getTeamId() in vsTeamIds:
                    score = matchup.getTeamAScore()
                    score = rounder.normalRound(score, decimalPlacesToRoundTo)
                    allScores.append(score)
                elif matchup.getTeamB().getTeamId() == teamId and matchup.getTeamA().getTeamId() in vsTeamIds:
                    score = matchup.getTeamBScore()
                    score = rounder.normalRound(score, decimalPlacesToRoundTo)
                    allScores.append(score)
        return allScores

    def getNumberOfWeeksInLeague(self, leagueModel: LeagueModel) -> int:
        """
        Returns as an int the number of weeks that are in the given leagueModel.
        """
        return len(leagueModel.getWeeks())

    def getAllTeamIdsInLeague(self, leagueModel: LeagueModel, **params) -> List[int]:
        """
        Returns as a list of ints all of the team IDs in the given leagueModel.
        """
        excludedId = params.pop("excludeId", None)
        teamIds = []
        for team in leagueModel.getTeams():
            if team.getTeamId() is not excludedId:
                teamIds.append(team.getTeamId())
        return teamIds

    def getAllWeeksTeamsPlayEachOther(self, leagueModel: LeagueModel, team1Id: int, opponentTeamIds: list) -> List[int]:
        """
        Returns as a list of ints all of the weeks that the team with team1Id plays any of the teams with ids in opponentTeamIds.
        """
        weeks = []
        for week in leagueModel.getWeeks():
            for matchup in week.getMatchups():
                if matchup.getTeamA().getTeamId() == team1Id and matchup.getTeamB().getTeamId() in opponentTeamIds or matchup.getTeamB().getTeamId() == team1Id and matchup.getTeamA().getTeamId() in opponentTeamIds:
                    weeks.append(week.getWeekNumber())
        return weeks



