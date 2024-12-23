import enum


class ScanModeType(enum.Enum):
    """
    Specifies scan mode in scans.
    """
    Full = 0
    Zoom = 1
    Sim = 2
    Srm = 3
    Crm = 4
    Any = 5
    Q1Ms = 6
    Q3Ms = 7
