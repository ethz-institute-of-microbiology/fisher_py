import enum


class CompensationVoltageType(enum.Enum):
    """
    Specifies compensation voltage type.
    """
    NoValue = 0
    SingleValue = 1
    Ramp = 2
    SIM = 3
    Any = 4
