import enum


class SectorScanType(enum.Enum):
    """
    Specifies type of sector scan.
    """
    SectorBScan = 0
    SectorEScan = 1
    Any = 2
