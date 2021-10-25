from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.utils import to_net_list
from typing import List


class TuneDataValues(NetWrapperBase):

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.TuneDataValues

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def id(self) -> int:
        """
        Gets or sets the index number of the tune record
        """
        return self._get_wrapped_object_().ID

    @id.setter
    def id(self, value: int):
        """
        Gets or sets the index number of the tune record
        """
        assert type(value) is int
        self._get_wrapped_object_().ID = value

    @property
    def values(self) -> List[str]:
        """
        Gets or sets the array of tune data values for an instrument
        """
        return self._get_wrapped_object_().Values

    @values.setter
    def values(self, value: List[str]):
        """
        Gets or sets the array of tune data values for an instrument
        """
        assert type(value) is list
        value = to_net_list(value, str)
        self._get_wrapped_object_().Values = value

