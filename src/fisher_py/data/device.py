import enum

class Device(enum.Enum):
    """
    Data acquisition device
    """
    none = -1
    MS = 0
    MSAnalog = 1
    Analog = 2
    UV = 3
    Pda = 4
    Other = 5
