from typing import List

from helpers.Constants import Constants
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel


class LeagueModelNavigator:
    """
    This class is used to navigate a LeagueModel object [or other object models contained within it].
    """

    @staticmethod
    def getTeamById(leagueModel: LeagueModel, year: str, teamId: int) -> TeamModel:
        """
        Returns a Team object for the team with the given ID in the given league in the given year.
        Throws Exception if a team with the given ID is not in the given league.
        """
        for team in leagueModel.years[str(year)].getTeams():
            if team.teamId == teamId:
                return team
        raise Exception("Given TeamID is not in the given LeagueModel at the given year.")

    @staticmethod
    def teamsPlayInWeek(week: WeekModel, team1Id: int, opponentIds: list) -> bool:
        """
        Returns a boolean on whether teams with the given IDs play in the given week.
        """
        for matchup in week.matchups:
            if matchup.teamA.teamId == team1Id and matchup.teamB.teamId in opponentIds or matchup.teamB.teamId == team1Id and matchup.teamA.teamId in opponentIds:
                return True
        return False

    @classmethod
    def teamsPlayEachOther(cls, leagueModel: LeagueModel, years: list, team1Id: int, team2Id: int) -> bool:
        """
        Returns a boolean on whether the teams with the given IDs play at all in the given league in the given year.
        """
        for year in years:
            for week in leagueModel.years[str(year)].getWeeks():
                if cls.teamsPlayInWeek(week, team1Id, [team2Id]):
                    return True
        return False

    @classmethod
    def gamesPlayedByTeam(cls, leagueModel: LeagueModel, years: list, teamId: int, **params) -> int:
        """
        Returns as an int the number of games played in the given league in the given years by the team with the given ID.
        THROUGHWEEK: [int] Gives games played through that week.
        ONLYWEEKS: [list] Gives games played for the given week numbers.
        VSTEAMIDS: [list] Gives games played vs teams with the given IDs.
        """
        gamesPlayed = 0
        for year in years:
            throughWeek = params.pop("throughWeek", cls.getNumberOfWeeksInLeague(leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", cls.getAllTeamIdsInLeague(leagueModel, year, excludeId=[teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in leagueModel.years[str(year)].getWeeks():
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                for matchup in week.matchups:
                    if matchup.teamA.teamId == teamId and matchup.teamB.teamId in vsTeamIds or matchup.teamB.teamId == teamId and matchup.teamA.teamId in vsTeamIds:
                        gamesPlayed += 1
        return gamesPlayed

    @classmethod
    def totalLeaguePoints(cls, leagueModel: LeagueModel, years: list, **params) -> float:
        """
        Returns a float that is the total amount of points scored in the given league in the given year.
        THROUGHWEEK: [int] Gives total league points scored through that week.
        ONLYWEEKS: [list] Gives total league points for the given week numbers.
        """
        totalPoints = 0
        for year in years:
            throughWeek = params.pop("throughWeek", cls.getNumberOfWeeksInLeague(leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            for week in leagueModel.years[str(year)].getWeeks():
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                for matchup in week.matchups:
                    totalPoints += matchup.teamAScore
                    totalPoints += matchup.teamBScore
        return Rounder.normalRound(totalPoints, Rounder.getDecimalPlacesRoundedToInScores(leagueModel))

    @classmethod
    def totalPointsScoredByTeam(cls, leagueModel: LeagueModel, years: list, teamId: int, **params) -> float:
        """
        Returns a float that is the total amount of points scored by the team with the given ID in the given league in the given years.
        THROUGHWEEK: [int] Gives total points scored through that week.
        ONLYWEEKS: [list] Gives total points for the given week numbers.
        VSTEAMIDS: [list] Gives total points vs teams with the given IDs.
        """
        totalPoints = 0
        for year in years:
            throughWeek = params.pop("throughWeek", cls.getNumberOfWeeksInLeague(leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", cls.getAllTeamIdsInLeague(leagueModel, year, excludeId=[teamId]))
            params["vsTeamIds"] = vsTeamIds
            for week in leagueModel.years[str(year)].getWeeks():
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                for matchup in week.matchups:
                    if matchup.teamA.teamId == teamId and matchup.teamB.teamId in vsTeamIds:
                        totalPoints += matchup.teamAScore
                    elif matchup.teamB.teamId == teamId and matchup.teamA.teamId in vsTeamIds:
                        totalPoints += matchup.teamBScore
        return Rounder.normalRound(totalPoints, Rounder.getDecimalPlacesRoundedToInScores(leagueModel))

    @staticmethod
    def getGameOutcomeAsString(matchup: MatchupModel, teamId: int):
        """
        Returns a string representation [win/loss/tie] of the outcome of the given game for the team with the given ID.
        Returns None if a team with the given ID does not play in this matchup.
        """
        if teamId != matchup.teamA.teamId and teamId != matchup.teamB.teamId:
            # the given team doesn't play in the given matchup
            return None
        if teamId == matchup.teamA.teamId:
            # given team is team A
            isTeamA = True
        else:
            # given team is team B
            isTeamA = False
        if matchup.teamAScore > matchup.teamBScore:
            if isTeamA:
                return Constants.WIN
            return Constants.LOSS
        elif matchup.teamAScore < matchup.teamBScore:
            if isTeamA:
                return Constants.LOSS
            return Constants.WIN
        else:
            return Constants.TIE

    @classmethod
    def getAllScoresInLeague(cls, leagueModel: LeagueModel, years: list, **params) -> List[float]:
        """
        Returns as a list of floats all of the scores in the given leagueModel in the given years.
        Note: These scores will be properly rounded.
        THROUGHWEEK: [int] Gives all league scores through that week.
        ONLYWEEKS: [list] Gives all league scores for the given week numbers.
        """
        allScores = []
        for year in years:
            throughWeek = params.pop("throughWeek", cls.getNumberOfWeeksInLeague(leagueModel, year))
            onlyWeeks = params.pop("onlyWeeks", None)
            decimalPlacesToRoundTo = Rounder.getDecimalPlacesRoundedToInScores(leagueModel)
            for week in leagueModel.years[str(year)].getWeeks():
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                for matchup in week.matchups:
                    scoreA = matchup.teamAScore
                    scoreB = matchup.teamBScore
                    scoreA = Rounder.normalRound(scoreA, decimalPlacesToRoundTo)
                    scoreB = Rounder.normalRound(scoreB, decimalPlacesToRoundTo)
                    allScores.append(scoreA)
                    allScores.append(scoreB)
        return allScores

    @classmethod
    def getAllScoresOfTeam(cls, leagueModel: LeagueModel, years: list, teamId: int, **params) -> List[float]:
        """
        Returns as a list of floats all of the scores in the given leagueModel in the given year that the team with the given ID had.
        Note: These scores will be properly rounded.
        THROUGHWEEK: [int] Gives all scores through that week.
        ONLYWEEKS: [list] Gives all scores for the given week numbers.
        VSTEAMIDS: [list] Gives all scores vs teams with the given IDs.
        """
        allScores = []
        for year in years:
            throughWeek = params.pop("throughWeek", cls.getNumberOfWeeksInLeague(leagueModel, year))
            params["throughWeek"] = throughWeek
            onlyWeeks = params.pop("onlyWeeks", None)
            params["onlyWeeks"] = onlyWeeks
            vsTeamIds = params.pop("vsTeamIds", cls.getAllTeamIdsInLeague(leagueModel, year, excludeId=[teamId]))
            params["vsTeamIds"] = vsTeamIds
            decimalPlacesToRoundTo = Rounder.getDecimalPlacesRoundedToInScores(leagueModel)
            for week in leagueModel.years[str(year)].getWeeks():
                if onlyWeeks and week.weekNumber not in onlyWeeks:
                    continue
                elif week.weekNumber > throughWeek:
                    break
                for matchup in week.matchups:
                    if matchup.teamA.teamId == teamId and matchup.teamB.teamId in vsTeamIds:
                        score = matchup.teamAScore
                        score = Rounder.normalRound(score, decimalPlacesToRoundTo)
                        allScores.append(score)
                    elif matchup.teamB.teamId == teamId and matchup.teamA.teamId in vsTeamIds:
                        score = matchup.teamBScore
                        score = Rounder.normalRound(score, decimalPlacesToRoundTo)
                        allScores.append(score)
        return allScores

    @staticmethod
    def getNumberOfWeeksInLeague(leagueModel: LeagueModel, year: int, **params):
        """
        Returns as an int the number of weeks that are in the given leagueModel.
        ASLIST: [boolean] Gives all week numbers as an ordered list.
        """
        asList = params.pop("asList", False)
        numberOfWeeks = len(leagueModel.years[str(year)].getWeeks())
        if asList:
            return [x + 1 for x in range(numberOfWeeks)]
        return numberOfWeeks

    @staticmethod
    def getAllTeamIdsInLeague(leagueModel: LeagueModel, year: int, **params) -> List[int]:
        """
        Returns as a list of ints all of the team IDs in the given leagueModel.
        EXCLUDEIDS: [list] List of team IDs that will be excluded from the return list.
        """
        excludeIds = params.pop("excludeIds", [])
        teamIds = []
        for team in leagueModel.years[str(year)].getTeams():
            if team.teamId not in excludeIds:
                teamIds.append(team.teamId)
        return teamIds

    @staticmethod
    def getAllWeeksTeamsPlayEachOther(leagueModel: LeagueModel, year: int, team1Id: int, opponentTeamIds: list,
                                      **params) -> List[int]:
        """
        Returns as a list of ints all of the weeks in the given league in the given year that the team with team1Id plays any of the teams with ids in opponentTeamIds.
        ONLYWEEKS: [list] Gives weeks teams play each other for the given week numbers.
        """
        onlyWeeks = params.pop("onlyWeeks", None)
        weeks = []
        for week in leagueModel.years[str(year)].getWeeks():
            if onlyWeeks and week.weekNumber not in onlyWeeks:
                continue
            for matchup in week.matchups:
                if matchup.teamA.teamId == team1Id and matchup.teamB.teamId in opponentTeamIds or matchup.teamB.teamId == team1Id and matchup.teamA.teamId in opponentTeamIds:
                    weeks.append(week.weekNumber)
        return weeks

    @classmethod
    def getListOfTeamScores(cls, leagueModel: LeagueModel, year: int, teamId: int, **params):
        """
        Returns as a list of floats all of the scores in order that the team with the given ID in the given league in the given year scored.
        THROUGHWEEK: [int] Gives list of scores through that week.
        ANDOPPONENTSCORE: [int] Gives list of tuples with (teamIdScore, opponentTeamIdScore)
        """
        throughWeek = params.pop("throughWeek", cls.getNumberOfWeeksInLeague(leagueModel, year))
        andOpponentScore = params.pop("andOpponentScore", False)

        scores = []
        for week in leagueModel.years[str(year)].getWeeks():
            if week.weekNumber > throughWeek:
                break
            for matchup in week.matchups:
                if matchup.teamA.teamId == teamId:
                    if andOpponentScore:
                        scores.append((matchup.teamAScore, matchup.teamBScore))
                        continue
                    scores.append(matchup.teamAScore)
                elif matchup.teamB.teamId == teamId:
                    if andOpponentScore:
                        scores.append((matchup.teamBScore, matchup.teamAScore))
                        continue
                    scores.append(matchup.teamBScore)
        return scores

    @staticmethod
    def getListOfYearsInLeague(leagueModel: LeagueModel, **params):
        """
        This returns as a list of TeamModels of all the years in the given league.
        This does not include year0.
        ASINTS: (boolean) If True, returns as a list of ints representing the years
        """
        asInts = params.pop("asInts", False)
        years = []
        for year in leagueModel.years:
            if year != "0":
                if asInts:
                    years.append(year)
                else:
                    years.append(leagueModel.years[year])
        return years

    @staticmethod
    def getDictOfYearModelsWithoutZero(leagueModel: LeagueModel):
        """
        This returns as a dict of TeamModels of all the years in the given league without year0.
        """
        years = leagueModel.years
        del years[0]
        return leagueModel.years

    @classmethod
    def getAllYearsWithWeeks(cls, leagueModel: LeagueModel, **params):
        """
        This returns as a list of TeamModels of all the years in the given league that have at least 1 week.
        ASINTS: (boolean) If True, returns as a list of ints representing the years
        """
        asInts = params.pop("asInts", False)
        allYears = leagueModel.years
        years = []
        for year in allYears:
            weeks = allYears[year].getWeeks()
            if weeks and len(weeks) > 0:
                if asInts:
                    years.append(int(year))
                else:
                    years.append(allYears[year])
        return years

    @classmethod
    def getMostRecentYear(cls, leagueModel: LeagueModel, **params):
        """
        This returns the most recent (highest-numbered) year in this league.
        ASINT: (boolean) If True, returns the most recent year as an int
        WITHWEEKS: (boolean) If True, returns the most recent year that has AT LEAST 1 week in it
        """
        asInt = params.pop("asInt", False)
        withWeeks = params.pop("withWeeks", False)

        if withWeeks:
            allYearsList = cls.getAllYearsWithWeeks(leagueModel)
            allYears = dict()
            for year in allYearsList:
                allYears[year.getYear()] = year
        else:
            allYears = leagueModel.years
        if len(allYears) > 0:
            mostRecentYear = allYears[max(allYears.keys())]
            if asInt:
                return int(mostRecentYear.getYear())
            else:
                return mostRecentYear
        else:
            return None
