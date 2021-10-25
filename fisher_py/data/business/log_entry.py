
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from typing import List


class LogEntry(NetWrapperBase):
    """
    Represents a single log.
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.LogEntry

    @property
    def labels(self) -> List[str]:
        """
        Gets or sets the labels in this log.
        """
        return list(self._get_wrapped_object_().Labels)

    @labels.setter
    def labels(self, value: List[str]):
        """
        Gets or sets the labels in this log.
        """
        assert type(value) is List[str]
        self._get_wrapped_object_().Labels = value

    @property
    def values(self) -> List[str]:
        """
        Gets or sets the values in this log.
        """
        return list(self._get_wrapped_object_().Values)

    @values.setter
    def values(self, value: List[str]):
        """
        Gets or sets the values in this log.
        """
        assert type(value) is List[str]
        self._get_wrapped_object_().Values = value

    @property
    def length(self) -> int:
        """
        Gets or sets the length of the log.
        """
        return self._get_wrapped_object_().Length

    @length.setter
    def length(self, value: int):
        """
        Gets or sets the length of the log.
        """
        assert type(value) is int
        self._get_wrapped_object_().Length = value

