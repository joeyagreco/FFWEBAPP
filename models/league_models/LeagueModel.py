from dataclasses import dataclass

from models.league_models.YearModel import YearModel


@dataclass
class LeagueModel:
    leagueId: int
    leagueName: str
    numberOfTeams: int
    years: YearModel
