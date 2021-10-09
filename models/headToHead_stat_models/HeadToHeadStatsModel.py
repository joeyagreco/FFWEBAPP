from dataclasses import dataclass


@dataclass
class HeadToHeadStatsModel:
    teamId: int
    teamName: str
    wins: int
    losses: int
    ties: int
    winPercentage: float
    ppg: float
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
    wal: float
    awalPerGame: float
