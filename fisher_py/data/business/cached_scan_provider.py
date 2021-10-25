from __future__ import annotations
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fisher_py.raw_file_reader import RawFileAccess
    from fisher_py.data.business import Scan


class CachedScanProvider(NetWrapperBase):

    def __init__(self):
        super().__init__()

    def get_scan_at_time(self, raw_data: RawFileAccess, time: float) -> Scan:
        """
        Create a scan object from a file and a retention time.
        
        Parameters:
        rawData:
        File to read from
        
        time:
        time of Scan number to read
        
        Returns:
        The scan read, or null if no scan was read
        """
        from fisher_py.data.business import Scan
        return Scan._get_wrapper_(self._get_wrapped_object().GetScanAtTime(raw_data._get_wrapped_object_(), time))

    def get_scan_from_scan_number(self, raw_data: RawFileAccess, scan_number: int) -> Scan:
        """
        Create a scan object from a file and a scan number.
        
        Parameters:
        rawData:
        File to read from
        
        scanNumber:
        Scan number to read
        
        Returns:
        The scan read, or null of the scan number if not valid
        """
        from fisher_py.data.business import Scan
        return Scan._get_wrapper_(self._get_wrapped_object().GetScanFromScanNumber(raw_data._get_wrapped_object_(), scan_number))
