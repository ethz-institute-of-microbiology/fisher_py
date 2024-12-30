import enum

class ToleranceMode(enum.Enum):
    """
    Specifies units for measuring mass tolerance.
    Tolerance is used to determine if a results should be kept, in formula search.
    If the exact mass of a formula is not within tolerance of a measured mass from
    an instrument, then the formula is not considered a valid result.
    """
    none = 0,
    Amu = 1,
    Mmu = 2,
    Ppm = 3
