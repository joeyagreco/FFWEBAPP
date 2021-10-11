from dataclasses import dataclass


@dataclass
class HeadToHeadStatsModel:
    awal: float
    awalPerGame: float
    losses: int
    maxScore: float
    minScore: float
    plusMinus: float
    ppg: float
    scoringShare: float
    smartWins: float
    stddev: float
    teamId: int
    teamLuck: float
    teamName: str
    teamScore: float
    teamSuccess: float
    ties: int
    wal: float
    winPercentage: float
    wins: int
