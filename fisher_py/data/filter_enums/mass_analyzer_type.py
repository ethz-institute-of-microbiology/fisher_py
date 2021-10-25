import enum


class MassAnalyzerType(enum.Enum):
    """
    Specifies type of mass analyzer in scans.
    """
    MassAnalyzerITMS = 0
    MassAnalyzerTQMS = 1
    MassAnalyzerSQMS = 2
    MassAnalyzerTOFMS = 3
    MassAnalyzerFTMS = 4
    MassAnalyzerSector = 5
    Any = 6
