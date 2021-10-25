import enum


class EventAccurateMass(enum.Enum):
    """
    Determines how accurate mass calibration was done.
    """
    Internal = 0
    External = 1
    Off = 2
