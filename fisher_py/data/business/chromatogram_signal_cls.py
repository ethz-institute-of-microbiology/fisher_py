from __future__ import annotations
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data.business import Range
from fisher_py.data.business.chromatogram_signal import ChromatogramData
from fisher_py.utils import to_net_list
from typing import List


class ChromatogramSignal(NetWrapperBase):
    """
    This represents the data for a chromatogram
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.ChromatogramSignal

    def __init__(self, *args):
        """
        Initializes a new instance of the ThermoFisher.CommonCore.Data.Business.ChromatogramSignal
        class.
        
        Parameters:
        signal:
        Clone from this interface
        """
        super().__init__()

        if len(args) == 0:
            self._wrapped_object = self._wrapped_type()
        elif len(args) == 1:
            self._wrapped_object = self._wrapped_type(args[0])
        else:
            raise ValueError('Unable to create chromatogram signal')

    @property
    def signal_times(self) -> List[float]:
        """
        Gets or sets the signal times.
        
        Value:
        The signal times.
        """
        return self._get_wrapped_object_().SignalTimes

    @signal_times.setter
    def signal_times(self, value: List[float]):
        """
        Gets or sets the signal times.
        
        Value:
        The signal times.
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().SignalTimes = value

    @property
    def time_range(self) -> Range:
        """
        Gets the time range.
        """
        return Range._get_wrapper_(self._get_wrapped_object_().TimeRange)

    @property
    def start_time(self) -> float:
        """
        Gets the time at the start of the signal
        """
        return self._get_wrapped_object_().StartTime

    @property
    def end_time(self) -> float:
        """
        Gets the time at the end of the signal
        """
        return self._get_wrapped_object_().EndTime

    @property
    def base_peak_masses(self) -> List[float]:
        """
        Gets the signal base peak masses.
        
        Value:
        The signal base peak masses. May be null (should not be used) when HasBasePeakData
        returns false
        """
        return self._get_wrapped_object_().BasePeakMasses

    @property
    def signal_base_peak_masses(self) -> List[float]:
        """
        Gets or sets the signal base peak masses.
        
        Value:
        The signal times.
        """
        return self._get_wrapped_object_().SignalBasePeakMasses

    @signal_base_peak_masses.setter
    def signal_base_peak_masses(self, value: List[float]):
        """
        Gets or sets the signal base peak masses.
        
        Value:
        The signal times.
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().SignalBasePeakMasses = value

    @property
    def scans(self) -> List[int]:
        """
        Gets the signal scans.
        
        Value:
        The signal scans.
        """
        return self._get_wrapped_object_().Scans

    @property
    def signal_scans(self) -> List[int]:
        """
        Gets or sets the signal scans.
        
        Value:
        The signal scans.
        """
        return self._get_wrapped_object_().SignalScans

    @signal_scans.setter
    def signal_scans(self, value: List[int]):
        """
        Gets or sets the signal scans.
        
        Value:
        The signal scans.
        """
        assert type(value) is List[int]
        value = to_net_list(value, int)
        self._get_wrapped_object_().SignalScans = value

    @property
    def intensities(self) -> List[float]:
        """
        Gets the intensities.
        
        Value:
        The signal intensities.
        """
        return self._get_wrapped_object_().Intensities

    @property
    def signal_intensities(self) -> List[float]:
        """
        Gets or sets the signal intensities.
        
        Value:
        The signal intensities.
        """
        return self._get_wrapped_object_().SignalIntensities

    @signal_intensities.setter
    def signal_intensities(self, value: List[float]):
        """
        Gets or sets the signal intensities.
        
        Value:
        The signal intensities.
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().SignalIntensities = value

    @property
    def has_base_peak_data(self) -> bool:
        """
        Gets a value indicating whether there is any base peak data in this signal
        """
        return self._get_wrapped_object_().HasBasePeakData

    @property
    def length(self) -> int:
        """
        Gets the number of points in the signal
        """
        return self._get_wrapped_object_().Length

    @property
    def times(self) -> List[float]:
        """
        Gets the times.
        """
        return self._get_wrapped_object_().Times

    @staticmethod
    def from_chromatogram_data(chromatogram_data: ChromatogramData) -> List[ChromatogramSignal]:
        """
        Create an array of signals from chromatogramData. The Interface ThermoFisher.CommonCore.Data.Interfaces.IChromatogramData
        describes data read from a file (if using IRawData). This constructor converts
        to an array of type Signal, simplifying use of individual chromatograms with
        Peak integration.
        
        Parameters:
        chromatogramData:
        data (usually read from file) to convert into signals
        
        Returns:
        The constructed signals, or null if the input is null
        """
        assert type(chromatogram_data) is ChromatogramData
        signals = ChromatogramSignal._wrapped_type.FromChromatogramData(chromatogram_data._get_wrapped_object_())
        return [ChromatogramSignal._get_wrapper_(s) for s in signals]

    @staticmethod
    def from_time_and_intensity(time: List[float], intensity: List[float]) -> ChromatogramSignal:
        """
        Summary:
            Create a Chromatogram signal, from time and intensity arrays
        
        Parameters:
          time:
            array of retention times
        
          intensity:
            array of intensities at each time
        
        Returns:
            The constructed signal, or null if either of the inputs are null, or the inputs
            are not the same length
        """
        assert type(time) is list
        assert type(intensity) is list
        time = to_net_list(time, float)
        intensity = to_net_list(intensity, float)
        return ChromatogramSignal._get_wrapper_(ChromatogramSignal._wrapped_type.FromTimeAndIntensity(time, intensity))

    @staticmethod
    def from_time_intensity_scan(time: List[float], intensity: List[float], scan: List[int]) -> ChromatogramSignal:
        """
        Summary:
            Create a Chromatogram signal, from time, intensity and scan arrays
        
        Parameters:
          time:
            array of retention times
        
          intensity:
            array of intensities at each time
        
          scan:
            array of scan numbers for each time
        
        Returns:
            The constructed signal, or null if either of the inputs are null, or the inputs
            are not the same length
        """
        assert type(time) is list
        assert type(intensity) is list
        assert type(scan) is list
        time = to_net_list(time, float)
        intensity = to_net_list(intensity, float)
        scan = to_net_list(scan, int)
        return ChromatogramSignal._get_wrapper_(ChromatogramSignal._wrapped_type.FromTimeIntensityScan(time, intensity, scan))
    
    @staticmethod
    def from_time_intensity_scan_base_peak(time: List[float], intensity: List[float], scan: List[int], base_peak: List[float]) -> ChromatogramSignal:
        """
        Summary:
            Create a Chromatogram signal, from time, intensity, scan and base peak arrays
        
        Parameters:
          time:
            array of retention times
        
          intensity:
            array of intensities at each time
        
          scan:
            array of scan numbers for each time
        
          basePeak:
            Array of base peak masses for each time
        
        Returns:
            The constructed signal, or null if either of the inputs are null, or the inputs
            are not the same length
        """
        assert type(time) is list
        assert type(intensity) is list
        assert type(scan) is list
        assert type(base_peak) is list
        time = to_net_list(time, float)
        intensity = to_net_list(intensity, float)
        scan = to_net_list(scan, int)
        base_peak = to_net_list(base_peak, float)
        return ChromatogramSignal._get_wrapper_(ChromatogramSignal._wrapped_type.FromTimeIntensityScanBasePeak(time, intensity, scan, base_peak))

    @staticmethod
    def to_chromatogram_data(signals: List[ChromatogramSignal]) -> ChromatogramData:
        """
        Summary:
            Create chromatogram data interface from signals. The Interface ThermoFisher.CommonCore.Data.Interfaces.IChromatogramData
            describes data read from a file (if using IRawData).
        //
        Parameters:
          signals:
            data (usually read from file) to convert into signals
        //
        Returns:
            The constructed signals, or null if the input is null
        """
        assert type(signals) is list
        net_signals = to_net_list([s._get_wrapped_object_() for s in signals], ChromatogramSignal._wrapped_type)
        return ChromatogramData._get_wrapper_(ChromatogramSignal._wrapped_type.ToChromatogramData(net_signals))

    def clone(self) -> object:
        """
        Creates a new object that is a (deep) copy of the current instance.
        
        Returns:
        A new object that is a copy of this instance.
        """
        return self._get_wrapped_object_().Clone()

    def delay(self, delay: float):
        """
        Add a delay to all times. This is intended to support "detector delays" where
        multiple detector see the same sample at different times.
        
        Parameters:
        delay:
        The delay.
        """
        self._get_wrapped_object_().Delay(delay)

    def valid(self) -> bool:
        """
        Test if the signal is valid
        
        Returns:
        True if both times and intensities have been set, and are the same length
        """
        return self._get_wrapped_object_().Valid()

