import enum


class EnergyType(enum.Enum):
    """
    Specifies precursor(collision) energy validation type.
    """
    Valid = 0
    Any = 1
