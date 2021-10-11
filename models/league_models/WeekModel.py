from dataclasses import dataclass
from typing import List

from models.league_models.MatchupModel import MatchupModel


@dataclass
class WeekModel:
    weekNumber: int
    matchups: List[MatchupModel]
