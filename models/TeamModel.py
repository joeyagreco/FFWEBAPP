class TeamModel:

    def __init__(self, teamId: int, teamName: str):
        self.__teamId = teamId
        self.__teamName = teamName

    def getTeamId(self):
        return self.__teamId

    def getTeamName(self):
        return self.__teamName
