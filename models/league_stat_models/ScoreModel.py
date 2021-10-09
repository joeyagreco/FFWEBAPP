from dataclasses import dataclass

from models.league_models.TeamModel import TeamModel


@dataclass
class ScoreModel:
    outcome: str
    score: float
    teamAgainst: TeamModel
    teamFor: TeamModel
    week: int
    year: int
