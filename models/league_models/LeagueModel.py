from dataclasses import dataclass


@dataclass
class LeagueModel:
    leagueId: int
    leagueName: str
    numberOfTeams: int
    years: dict
