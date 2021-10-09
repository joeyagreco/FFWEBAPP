from dataclasses import dataclass

from models.league_models.TeamModel import TeamModel


@dataclass
class StreakModel:
    firstDate: str
    firstTeam: TeamModel
    lastDate: str
    lastTeam: TeamModel
    ongoing: bool
    owner: TeamModel
    streakNumber: int
