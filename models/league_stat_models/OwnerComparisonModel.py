from dataclasses import dataclass


@dataclass
class OwnerComparisonModel:
    awal: float
    awalPerGame: float
    losses: int
    maxScore: float
    minScore: float
    ownerId: int
    ownerName: str
    plusMinus: float
    ppg: float
    ppgAgainst: float
    scoringShare: float
    scoringShareAgainst: float
    smartWins: float
    stddev: float
    strengthOfSchedule: float
    teamLuck: float
    teamScore: float
    teamSuccess: float
    ties: int
    wal: float
    winPercentage: float
    wins: int
