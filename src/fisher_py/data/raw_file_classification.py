import enum


class RawFileClassification(enum.Enum):
    """
    RawFile Classification
    """
    Indeterminate = 0
    StandardRaw = 1
    MasterScanNumberRaw = 2
