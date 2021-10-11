from dataclasses import dataclass

from models.league_models.TeamModel import TeamModel


@dataclass
class MatchupModel:
    matchupId: int
    teamA: TeamModel
    teamB: TeamModel
    teamAScore: float
    teamBScore: float
