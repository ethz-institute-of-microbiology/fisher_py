from fisher_py.net_wrapping import NetWrapperBase
from typing import List


class ScanDependentDetails(NetWrapperBase):

    @property
    def scan_index(self) -> int:
        """
        Gets the index of the scan.
        
        Value:
        The index of the scan.
        """
        return self._get_wrapped_object_().ScanIndex

    @property
    def filter_string(self) -> str:
        """
        Gets the filter string.
        
        Value:
        The filter string.
        """
        return self._get_wrapped_object_().FilterString

    @property
    def precursor_mass_array(self) -> List[float]:
        """
        Gets the precursor array.
        
        Value:
        The precursor mass array.
        """
        return self._get_wrapped_object_().PrecursorMassArray

    @property
    def isolation_width_array(self) -> List[float]:
        """
        Gets the isolation width array.
        
        Value:
        The isolation width array.
        """
        return self._get_wrapped_object_().IsolationWidthArray

