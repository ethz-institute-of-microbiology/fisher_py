from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from typing import List


class SimpleScan(NetWrapperBase):

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.SimpleScan

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def masses(self) -> List[float]:
        """
        Gets the list of masses of each centroid
        """
        return self._get_wrapped_object_().Masses

    @property
    def intensities(self) -> List[float]:
        """
        Gets the list of Intensities for each centroid
        """
        return self._get_wrapped_object_().Intensities
