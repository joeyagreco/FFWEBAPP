from models.league_models.TeamModel import TeamModel


class MarginOfVictoryModel:

    def __init__(self, marginOfVictory: float, winningTeam: TeamModel, winningTeamPoints: float, losingTeam: TeamModel, losingTeamPoints: float, week: int):
        self.__marginOfVictory = marginOfVictory
        self.__winningTeam = winningTeam
        self.__winningTeamPoints = winningTeamPoints
        self.__losingTeam = losingTeam
        self.__losingTeamPoints = losingTeamPoints
        self.__week = week

    def getMarginOfVictory(self):
        return self.__marginOfVictory

    def getWinningTeam(self):
        return self.__winningTeam

    def getWinningTeamPoints(self):
        return self.__winningTeamPoints

    def getLosingTeam(self):
        return self.__losingTeam

    def getLosingTeamPoints(self):
        return self.__losingTeamPoints

    def getWeek(self):
        return self.__week
