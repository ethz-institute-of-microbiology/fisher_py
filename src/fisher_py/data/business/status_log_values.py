from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.utils import to_net_list
from typing import List


class StatusLogValues(NetWrapperBase):
    """
    Stores one record of status log values
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.StatusLogValues

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def retention_time(self) -> float:
        """
        Gets or sets the RetentionTime for this log entry
        """
        return self._get_wrapped_object_().RetentionTime

    @retention_time.setter
    def retention_time(self, value: float):
        """
        Gets or sets the RetentionTime for this log entry
        """
        assert type(value) is float
        self._get_wrapped_object_().RetentionTime = value

    @property
    def values(self) -> List[str]:
        """
        Gets or sets the array of status log values
        """
        return self._get_wrapped_object_().Values

    @values.setter
    def values(self, value: List[str]):
        """
        Gets or sets the array of status log values
        """
        assert type(value) is list
        value = to_net_list(value, str)
        self._get_wrapped_object_().Values = value

