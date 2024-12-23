import enum


class DetectorType(enum.Enum):
    """
    Specifies inclusion or exclusion of the detector value.
    """
    Valid = 0
    Any = 1
    NotValid = 2
