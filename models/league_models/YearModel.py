class YearModel:

    def __init__(self, teams, weeks):
        self.__teams = teams
        self.__weeks = weeks

    def getTeams(self):
        return self.__teams

    def getWeeks(self):
        return self.__weeks
