import enum


class GenericDataTypes(enum.Enum):
    """
    enumeration for data type for the fields used by records of TuneData, StatusLog,
    TrailerExtra These are upper case names, so that they don't clash with standard
    type names.
    """
    NULL = 0
    CHAR = 1
    TRUEFALSE = 2
    YESNO = 3
    ONOFF = 4
    UCHAR = 5
    SHORT = 6
    USHORT = 7
    LONG = 8
    ULONG = 9
    FLOAT = 10
    DOUBLE = 11
    CHAR_STRING = 12
    WCHAR_STRING = 13
