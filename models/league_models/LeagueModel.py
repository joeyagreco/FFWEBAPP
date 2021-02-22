class LeagueModel:

    def __init__(self, leagueId: int, leagueName: str, numberOfTeams: int, years):
        self.__leagueId = leagueId
        self.__leagueName = leagueName
        self.__numberOfTeams = numberOfTeams
        self.__years = years

    def getLeagueId(self):
        return self.__leagueId

    def getLeagueName(self):
        return self.__leagueName

    def getNumberOfTeams(self):
        return self.__numberOfTeams

    def getYears(self):
        return self.__years
