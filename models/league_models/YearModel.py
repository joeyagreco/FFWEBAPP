from dataclasses import dataclass
from typing import List

from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel


@dataclass
class YearModel:
    year: int
    teams: List[TeamModel]
    weeks: List[WeekModel]
