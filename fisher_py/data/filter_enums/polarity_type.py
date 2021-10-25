import enum


class PolarityType(enum.Enum):
    """
    Specifies polarity of scan.
    """
    Negative = 0
    Positive = 1
    Any = 2
