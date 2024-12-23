import enum


class FilterAccurateMass(enum.Enum):
    """
    The filter rule for accurate mass.
    """
    Off = 0
    On = 1
    Internal = 2
    External = 3
    Any = 4
