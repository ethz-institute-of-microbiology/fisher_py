from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from typing import List


class ChromatogramData(NetWrapperBase):

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.ChromatogramSignal

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def positions_array(self) -> List[List[float]]:
        """
        Gets Times in minutes for each chromatogram
        """
        return [[n for n in sublist] for sublist in self._get_wrapped_object_().PositionsArray]

    @property
    def scan_numbers_array(self) -> List[List[int]]:
        """
        Gets Scan numbers for data points in each chromatogram
        """
        return [[n for n in sublist] for sublist in self._get_wrapped_object_().ScanNumbersArray]

    @property
    def intensities_array(self) -> List[List[float]]:
        """
        Gets Intensities for each chromatogram
        """
        return [[n for n in sublist] for sublist in self._get_wrapped_object_().IntensitiesArray]

    @property
    def length(self) -> int:
        """
        Gets The number of chromatograms in this object
        """
        return self._get_wrapped_object_().Length
