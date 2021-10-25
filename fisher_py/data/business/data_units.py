import enum


class DataUnits(enum.Enum):
    """
    Units of data from a UV or analog devices (if known).
    """
    none = 0
    AbsorbanceUnits = 1
    MilliAbsorbanceUnits = 2
    MicroAbsorbanceUnits = 3
    Volts = 4
    MilliVolts = 5
    MicroVolts = 6
