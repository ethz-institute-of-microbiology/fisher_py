import enum


class BarcodeStatusType(enum.Enum):
    """
    Enumeration of possible bar code status values
    """
    NotRead = 0
    Read = 1
    Unreadable = 2
    Error = 3
    Wait = 4