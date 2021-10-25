import enum


class ScanDataType(enum.Enum):
    """
    Specifies data type of scan.
    """
    Centroid = 0
    Profile = 1
    Any = 2
