from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data.filter_enums import MassAnalyzerType
from fisher_py.data.business import Scan
from fisher_py.raw_file_reader import RawFileAccess
from fisher_py.mass_precision_estimator import EstimatorResults
from fisher_py.utils import to_net_list
from typing import List


class PrecisionEstimate(NetWrapperBase):

    _wrapped_type = ThermoFisher.CommonCore.MassPrecisionEstimator.PrecisionEstimate

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()
        self._raw_file = None

    @property
    def raw_file(self) -> RawFileAccess:
        """
        Gets the raw file as an open IRawData objects.
        """
        return self._raw_file

    @raw_file.setter
    def raw_file(self, value: RawFileAccess):
        """
        Sets the raw file as an open IRawData objects.
        """
        assert type(value) is RawFileAccess
        self._raw_file = value
        self._get_wrapped_object_().Rawfile = value._get_wrapped_object_()

    @property
    def scan_number(self) -> int:
        """
        Gets the scan number of the scan to be analyzed
        
        Value:
        The scan number.
        """
        return self._get_wrapped_object_().ScanNumber

    @scan_number.setter
    def scan_number(self, value: int):
        """
        Sets the scan number of the scan to be analyzed
        
        Value:
        The scan number.
        """
        assert type(value) is int
        self._get_wrapped_object_().ScanNumber = value

    def dispose(self):
        """
        Performs application-defined tasks associated with freeing, releasing, or resetting
        unmanaged resources.
        """
        self._get_wrapped_object_().Dispose()

    def get_ion_time(self, analyzer_type: MassAnalyzerType, scan: Scan, trailer_headings: List[str], trailer_values: List[str]) -> float:
        """
        Calculate the ion time (fill (traps and FT) or dwell time (quads))
        
        Parameters:
        analyzerType:
        The analyzer type
        
        scan:
        The scan to process
        
        trailerHeadings:
        The trailer extra data headings
        
        trailerValues:
        The trailer extra data values
        
        Returns:
        The calculated ion time
        """
        assert type(analyzer_type) is MassAnalyzerType
        assert type(scan) is Scan
        assert type(trailer_headings) is list
        assert type(trailer_values) is list
        trailer_headings = to_net_list(trailer_headings, str)
        trailer_values = to_net_list(trailer_values, str)
        return self._get_wrapped_object_().GetIonTime(analyzer_type.value, scan._get_wrapped_object_(), trailer_headings, trailer_values)

    def get_mass_precision_estimate(self, scan: Scan, analyzer_type: MassAnalyzerType, ion_time: float, resolution: float) -> List[EstimatorResults]:
        """
        Gets mass precision estimate and stores them in a class property list of classes
        This method will throw an Exception or ArgumentException if a problem occurs
        during processing.
        
        Parameters:
        scan:
        The scan to process
        
        analyzerType:
        The analyzer type for the scan
        
        ionTime:
        The ion time for the scan
        
        resolution:
        The resolution for the scan
        
        Returns:
        Returns the list of Mass Precision Estimation results
        """
        return self._get_wrapped_object_().GetMassPrecisionEstimate(scan, analyzer_type, ion_time, resolution)

    def get_mass_precision_estimate(self) -> List[EstimatorResults]:
        """
        Gets mass precision estimate and stores them in a class property list of classes
        This method will throw an Exception or ArgumentException if a problem occurs
        during processing.
        
        Returns:
        Returns the list of Mass Precision Estimation results
        """
        return [EstimatorResults._get_wrapper_(e) for e in self._get_wrapped_object_().GetMassPrecisionEstimate()]
