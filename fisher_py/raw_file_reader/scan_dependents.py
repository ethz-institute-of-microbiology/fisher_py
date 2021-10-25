from fisher_py.net_wrapping import NetWrapperBase
from fisher_py.data import RawFileClassification, ScanDependentDetails
from fisher_py.utils import to_net_list
from typing import List


class ScanDependents(NetWrapperBase):
    """
    The ScanDependents interface. Result of call to "GetScanDependents" Provides
    a set of scan numbers which were created form a particular master scan.
    """

    @property
    def raw_file_instrument_type(self) -> RawFileClassification:
        """
        Gets or sets the type of the raw file instrument.
        
        Value:
        The type of the raw file instrument.
        """
        return RawFileClassification(self._get_wrapped_object_().RawFileInstrumentType)

    @raw_file_instrument_type.setter
    def raw_file_instrument_type(self, value: RawFileClassification):
        """
        Gets or sets the type of the raw file instrument.
        
        Value:
        The type of the raw file instrument.
        """
        assert type(value) is RawFileClassification
        self._get_wrapped_object_().RawFileInstrumentType = value.value

    @property
    def scan_dependent_detail_array(self) -> List[ScanDependentDetails]:
        """
        Gets or sets the scan dependent detail array.
        
        Value:
        The scan dependent detail array.
        """
        return [ScanDependentDetails._get_wrapper_(s) for s in self._get_wrapped_object_().ScanDependentDetailArray]

    @scan_dependent_detail_array.setter
    def scan_dependent_detail_array(self, value: List[ScanDependentDetails]):
        """
        Gets or sets the scan dependent detail array.
        
        Value:
        The scan dependent detail array.
        """
        assert type(value) is list
        value = to_net_list(value, type(value[0]._get_wrapped_object_()) if len(value) > 0 else object)
        self._get_wrapped_object_().ScanDependentDetailArray = [s._get_wrapped_object_() for s in value]

