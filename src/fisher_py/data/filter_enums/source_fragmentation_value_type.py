import enum


class SourceFragmentationValueType(enum.Enum):
    """
    Specifies how source fragmentation values are interpreted.
    """
    NoValue = 0
    SingleValue = 1
    Ramp = 2
    SIM = 3
    Any = 4
