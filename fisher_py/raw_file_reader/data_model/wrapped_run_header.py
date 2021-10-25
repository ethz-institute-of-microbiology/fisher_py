from fisher_py.net_wrapping import NetWrapperBase
from fisher_py.data import ToleranceUnits


class WrappedRunHeader(NetWrapperBase):
    """
    Information about the file stream
    """

    def __init__(self):
        super().__init__()
        # can only be used for wrapping (no Python side instantiation

    @property
    def spectra_count(self) -> int:
        """
        Gets the count of recorded spectra
        """
        return self._get_wrapped_object_().SpectraCount

    @property
    def high_mass(self) -> float:
        """
        Gets the highest recorded mass in file
        """
        return self._get_wrapped_object_().HighMass

    @property
    def low_mass(self) -> float:
        """
        Gets the lowest recorded mass in file
        """
        return self._get_wrapped_object_().LowMass

    @property
    def end_time(self) -> float:
        """
        Gets the time of last scan in file
        """
        return self._get_wrapped_object_().EndTime

    @property
    def start_time(self) -> float:
        """
        Gets the time of first scan in file
        """
        return self._get_wrapped_object_().StartTime

    @property
    def last_spectrum(self) -> int:
        """
        Gets the last spectrum (scan) number. If this is less than 1, then there are
        no scans acquired yet.
        """
        return self._get_wrapped_object_().LastSpectrum

    @property
    def first_spectrum(self) -> int:
        """
        Gets the first spectrum (scan) number (typically 1).
        """
        return self._get_wrapped_object_().FirstSpectrum

    @property
    def comment_2(self) -> str:
        """
        Gets the second comment about this data stream.
        """
        return self._get_wrapped_object_().Comment2

    @property
    def comment_1(self) -> str:
        """
        Gets the first comment about this data stream.
        """
        return self._get_wrapped_object_().Comment1

    @property
    def max_intensity(self) -> float:
        """
        Gets the max intensity.
        """
        return self._get_wrapped_object_().MaxIntensity

    @property
    def filter_mass_precision(self) -> int:
        """
        Gets the number of digits of precision suggested for formatting masses in the
        filters.
        """
        return self._get_wrapped_object_().FilterMassPrecision

    @property
    def expected_run_time(self) -> float:
        """
        Gets the expected data acquisition time.
        """
        return self._get_wrapped_object_().ExpectedRunTime

    @property
    def mass_resolution(self) -> float:
        """
        Gets the mass resolution of this instrument.
        """
        return self._get_wrapped_object_().MassResolution

    @property
    def in_acquisition(self) -> int:
        """
        Gets a value indicating whether this file is being created. 0: File is complete.
        All other positive values: The file is in acquisition. Negative values are undefined.
        """
        return self._get_wrapped_object_().InAcquisition

    @property
    def trailer_extra_count(self) -> int:
        """
        Gets the count of "trailer extra" records. Typically, same as the count of scans.
        """
        return self._get_wrapped_object_().TrailerExtraCount

    @property
    def trailer_scan_event_count(self) -> int:
        """
        Gets the count of "scan events"
        """
        return self._get_wrapped_object_().TrailerScanEventCount

    @property
    def error_log_count(self) -> int:
        """
        Gets the count of error log entries
        """
        return self._get_wrapped_object_().ErrorLogCount

    @property
    def tune_data_count(self) -> int:
        """
        Gets the count of tune data entries
        """
        return self._get_wrapped_object_().TuneDataCount

    @property
    def status_log_count(self) -> int:
        """
        Gets the count of status log entries
        """
        return self._get_wrapped_object_().StatusLogCount

    @property
    def tolerance_unit(self) -> ToleranceUnits:
        """
        Gets the tolerance units
        """
        return ToleranceUnits(self._get_wrapped_object_().ToleranceUnit)

    @property
    def max_integrated_intensity(self) -> float:
        """
        Gets the max integrated intensity.
        """
        return self._get_wrapped_object_().MaxIntegratedIntensity