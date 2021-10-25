import enum


class PeakOptions(enum.Enum):
    """
    Features which can be set per peak, such as "reference compound"
    """
    none = 0
    Saturated = 1
    Fragmented = 2
    Merged = 4
    Exception = 8
    Reference = 16
    Modified = 32
    LockPeak = 64
