from typing import Any, List
from datetime import datetime
import clr

clr.AddReference('System')
from System import DateTime, Double
import System.Collections.Generic as generic

def is_number(arg: Any) -> bool:
    return type(arg) is int or type(arg) is float


def datetime_net_to_py(net_date_time: DateTime) -> datetime:
    """
    Convert .NET DateTime to python datetime
    """
    return datetime(net_date_time.Year, net_date_time.Month, net_date_time.Day, net_date_time.Hour, net_date_time.Minute, net_date_time.Second, int(net_date_time.Millisecond * 1e3))


def datetime_py_to_net(py_date_time: datetime) -> DateTime:
    """
    Convert python datetime to .NET DateTime
    """
    return DateTime(py_date_time.year, py_date_time.month, py_date_time.day, py_date_time.hour, py_date_time.minute, py_date_time.second, int(float(py_date_time.microsecond) / 1e3))


def to_net_list(py_list: List[Any], t) -> Any:
    """
    Convert to .NET list
    """
    if type(t) is float:
        t = Double

    return generic.List[t](py_list)
