from dataclasses import dataclass

from models.league_models.TeamModel import TeamModel


@dataclass
class MarginOfVictoryModel:
    losingTeam: TeamModel
    losingTeamPoints: float
    marginOfVictory: float
    week: int
    winningTeam: TeamModel
    winningTeamPoints: float
    year: int
