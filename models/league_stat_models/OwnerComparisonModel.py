from dataclasses import dataclass


@dataclass
class OwnerComparisonModel:
    ownerId: int
    ownerName: str
    wins: int
    losses: int
    ties: int
    winPercentage: float
    ppg: float
    ppgAgainst: float
    plusMinus: float
    stddev: float
    maxScore: float
    minScore: float
    awal: float
    teamScore: float
    teamSuccess: float
    teamLuck: float
    smartWins: float
    scoringShare: float
    strengthOfSchedule: float
    wal: float
    scoringShareAgainst: float
    awalPerGame: float
