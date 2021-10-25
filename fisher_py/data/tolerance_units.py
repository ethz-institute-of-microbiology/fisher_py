import enum


class ToleranceUnits(enum.Enum):
    """
    The units that you can associate with mass tolerance
    """
    mmu = 0
    ppm = 1
    amu = 2
