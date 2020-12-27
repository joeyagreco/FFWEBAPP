from models.league_models.LeagueModel import LeagueModel


class EveryGameCalculator:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getMarginOfVictories(self):
        """
        Returns a list of MarginOfVictoryModels.
        """
        models = []
        for week in self.__leagueModel:
            for matchup in week.getMatchups():
                if matchup.getTeamAScore() > matchup.getTeamBScore():
                    # team A won
                    mov = matchup.getTeamAScore() - matchup.getTeamBScore()
                    teamFor = matchup.getTeamA()
                    teamForPoints = matchup.getTeamAScore()
                    teamAgainst = matchup.getTeamB()
                    teamAgainstPoints = matchup.getTeamBScore()
                    weekNumber = week.getWeekNumber()
                elif matchup.getTeamBScore() > matchup.getTeamAScore():
                    # team B won
                    mov = matchup.getTeamBScore() - matchup.getTeamAScore()
                    teamFor = matchup.getTeamB()
                    teamForPoints = matchup.getTeamBScore()
                    teamAgainst = matchup.getTeamA()
                    teamAgainstPoints = matchup.getTeamAScore()
                    weekNumber = week.getWeekNumber()
                else:
                    # tie, dont care about this
                    continue
                model = MarginOfVictoryModel(mov, teamFor, teamForPoints, teamAgainst, teamAgainstPoints, weekNumber)
