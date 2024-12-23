import enum


class BracketType(enum.Enum):
    """
    Specifies a sequence bracket type. This determines which groups of samples use
    the same calibration curve.
    """
    Unspecified = 0
    Overlapped = 1
    none = 2
    NonOverlapped = 3
    Open = 4
