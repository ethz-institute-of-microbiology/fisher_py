import enum


class TriState(enum.Enum):
    """
    The feature state. By default: On. This tri-state enum is designed for filtering
    """
    On = 0
    Off = 1
    Any = 2
