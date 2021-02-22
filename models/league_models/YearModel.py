class YearModel:

    def __init__(self, year, teams, weeks):
        self.__year = year
        self.__teams = teams
        self.__weeks = weeks

    def getYear(self):
        return self.__year

    def getTeams(self):
        return self.__teams

    def getWeeks(self):
        return self.__weeks
