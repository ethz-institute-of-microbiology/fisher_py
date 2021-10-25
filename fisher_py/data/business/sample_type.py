import enum

class SampleType(enum.Enum):
    """
    Enumeration of sample types
    """
    Unknown = 0
    Blank = 1
    QC = 2
    StdClear = 3
    StdUpdate = 4
    StdBracket = 5
    StdBracketStart = 6
    StdBracketEnd = 7
    Program = 8
    SolventBlank = 9
    MatrixBlank = 10
    MatrixSpike = 11
    MatrixSpikeDuplicate = 12
