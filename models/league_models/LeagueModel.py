class LeagueModel:

    # def __init__(self, leagueId: int, leagueName: str, numberOfTeams: int, teams: List[TeamModel], weeks: List[WeekModel]):
    def __init__(self, leagueId: int, leagueName: str, numberOfTeams: int, teams, weeks):
        self.__leagueId = leagueId
        self.__leagueName = leagueName
        self.__numberOfTeams = numberOfTeams
        self.__teams = teams
        self.__weeks = weeks

    def getLeagueId(self):
        return self.__leagueId

    def getLeagueName(self):
        return self.__leagueName

    def getNumberOfTeams(self):
        return self.__numberOfTeams

    def getTeams(self):
        return self.__teams

    def getWeeks(self):
        return self.__weeks
