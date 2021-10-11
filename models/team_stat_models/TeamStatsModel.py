from dataclasses import dataclass


@dataclass
class TeamStatsModel:
    awal: float
    awalPerGame: float
    losses: int
    maxScore: float
    minScore: float
    plusMinus: float
    ppg: float
    ppgAgainst: float
    scoringShare: float
    scoringShareAgainst: float
    smartWins: float
    stddev: float
    strengthOfSchedule: float
    teamId: int
    teamLuck: float
    teamName: str
    teamScore: float
    teamSuccess: float
    ties: int
    wal: float
    winPercentage: float
    wins: int
    year: int
