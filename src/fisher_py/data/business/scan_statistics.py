from __future__ import annotations
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data.business import SpectrumPacketType


class ScanStatistics(NetWrapperBase):
    """
    Summary information about a scan.
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.ScanStatistics

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def wavelength_step(self) -> float:
        """
        Gets or sets the wave length step.
        """
        return self._get_wrapped_object_().WavelengthStep

    @wavelength_step.setter
    def wavelength_step(self, value: float):
        """
        Gets or sets the wave length step.
        """
        assert type(value) is float
        self._get_wrapped_object_().WavelengthStep = value

    @property
    def absorbance_unit_scale(self) -> float:
        """
        Gets or sets the absorbance unit scale.
        """
        return self._get_wrapped_object_().AbsorbanceUnitScale

    @absorbance_unit_scale.setter
    def absorbance_unit_scale(self, value: float):
        """
        Gets or sets the absorbance unit scale.
        """
        assert type(value) is float
        self._get_wrapped_object_().AbsorbanceUnitScale = value

    @property
    def is_uniform_time(self) -> bool:
        """
        Gets or sets a value indicating whether is uniform time.
        """
        return self._get_wrapped_object_().IsUniformTime

    @is_uniform_time.setter
    def is_uniform_time(self, value: bool):
        """
        Gets or sets a value indicating whether is uniform time.
        """
        assert type(value) is bool
        self._get_wrapped_object_().IsUniformTime = value

    @property
    def frequency(self) -> float:
        """
        Gets or sets the frequency.
        """
        return self._get_wrapped_object_().Frequency

    @frequency.setter
    def frequency(self, value: float):
        """
        Gets or sets the frequency.
        """
        assert type(value) is float
        self._get_wrapped_object_().Frequency = value

    @property
    def is_centroid_scan(self) -> bool:
        """
        Gets or sets a value indicating whether this scan contains centroid data (else
        profile)
        """
        return self._get_wrapped_object_().IsCentroidScan

    @is_centroid_scan.setter
    def is_centroid_scan(self, value: bool):
        """
        Gets or sets a value indicating whether this scan contains centroid data (else
        profile)
        """
        assert type(value) is bool
        self._get_wrapped_object_().IsCentroidScan = value

    @property
    def segment_number(self) -> int:
        """
        Gets or sets the time segment number for this event
        """
        return self._get_wrapped_object_().SegmentNumber

    @segment_number.setter
    def segment_number(self, value: int):
        """
        Gets or sets the time segment number for this event
        """
        assert type(value) is int
        self._get_wrapped_object_().SegmentNumber = value

    @property
    def scan_event_number(self) -> int:
        """
        Gets or sets the event (scan type) number within segment
        """
        return self._get_wrapped_object_().ScanEventNumber

    @scan_event_number.setter
    def scan_event_number(self, value: int):
        """
        Gets or sets the event (scan type) number within segment
        """
        assert type(value) is int
        self._get_wrapped_object_().ScanEventNumber = value

    @property
    def scan_number(self) -> int:
        """
        Gets or sets the number of the scan
        """
        return self._get_wrapped_object_().ScanNumber

    @scan_number.setter
    def scan_number(self, value: int):
        """
        Gets or sets the number of the scan
        """
        assert type(value) is int
        self._get_wrapped_object_().ScanNumber = value

    @property
    def number_of_channels(self) -> int:
        """
        Gets or sets the number of channels acquired in this scan, if this is UV or analog
        data,
        """
        return self._get_wrapped_object_().NumberOfChannels

    @number_of_channels.setter
    def number_of_channels(self, value: int):
        """
        Gets or sets the number of channels acquired in this scan, if this is UV or analog
        data,
        """
        assert type(value) is int
        self._get_wrapped_object_().NumberOfChannels = value

    @property
    def packet_count(self) -> int:
        """
        Gets or sets the Number of point in scan
        """
        return self._get_wrapped_object_().PacketCount

    @packet_count.setter
    def packet_count(self, value: int):
        """
        Gets or sets the Number of point in scan
        """
        assert type(value) is int
        self._get_wrapped_object_().PacketCount = value

    @property
    def start_time(self) -> float:
        """
        Gets or sets the time at start of scan (minutes)
        """
        return self._get_wrapped_object_().StartTime

    @start_time.setter
    def start_time(self, value: float):
        """
        Gets or sets the time at start of scan (minutes)
        """
        assert type(value) is float
        self._get_wrapped_object_().StartTime = value

    @property
    def tic(self) -> float:
        """
        Gets or sets the total Ion Current for scan
        """
        return self._get_wrapped_object_().TIC

    @tic.setter
    def tic(self, value: float):
        """
        Gets or sets the total Ion Current for scan
        """
        assert type(value) is float
        self._get_wrapped_object_().TIC = value

    @property
    def base_peak_mass(self) -> float:
        """
        Gets or sets the mass of largest peak in scan
        """
        return self._get_wrapped_object_().BasePeakMass

    @base_peak_mass.setter
    def base_peak_mass(self, value: float):
        """
        Gets or sets the mass of largest peak in scan
        """
        assert type(value) is float
        self._get_wrapped_object_().BasePeakMass = value

    @property
    def base_peak_intensity(self) -> float:
        """
        Gets or sets the intensity of highest peak in scan
        """
        return self._get_wrapped_object_().BasePeakIntensity

    @base_peak_intensity.setter
    def base_peak_intensity(self, value: float):
        """
        Gets or sets the intensity of highest peak in scan
        """
        assert type(value) is float
        self._get_wrapped_object_().BasePeakIntensity = value

    @property
    def short_wavelength(self) -> float:
        """
        Gets or sets the shortest wavelength in PDA scan
        """
        return self._get_wrapped_object_().ShortWavelength

    @short_wavelength.setter
    def short_wavelength(self, value: float):
        """
        Gets or sets the shortest wavelength in PDA scan
        """
        assert type(value) is float
        self._get_wrapped_object_().ShortWavelength = value

    @property
    def long_wavelength(self) -> float:
        """
        Gets or sets the longest wavelength in PDA scan
        """
        return self._get_wrapped_object_().LongWavelength

    @long_wavelength.setter
    def long_wavelength(self, value: float):
        """
        Gets or sets the longest wavelength in PDA scan
        """
        assert type(value) is float
        self._get_wrapped_object_().LongWavelength = value

    @property
    def low_mass(self) -> float:
        """
        Gets or sets the lowest mass in scan
        """
        return self._get_wrapped_object_().LowMass

    @low_mass.setter
    def low_mass(self, value: float):
        """
        Gets or sets the lowest mass in scan
        """
        assert type(value) is float
        self._get_wrapped_object_().LowMass = value

    @property
    def high_mass(self) -> float:
        """
        Gets or sets the highest mass in scan
        """
        return self._get_wrapped_object_().HighMass

    @high_mass.setter
    def high_mass(self, value: float):
        """
        Gets or sets the highest mass in scan
        """
        assert type(value) is float
        self._get_wrapped_object_().HighMass = value

    @property
    def spectrum_packet_type(self) -> SpectrumPacketType:
        """
        Gets the packet format used in this scan. (read only). Value can be set using
        the "PacketType" property.
        """
        return SpectrumPacketType(self._get_wrapped_object_().SpectrumPacketType)

    @property
    def packet_type(self) -> int:
        """
        Gets or sets the indication of data format used by this scan. See also SpectrumPacketType
        for decoding to an enum.
        """
        return self._get_wrapped_object_().PacketType

    @packet_type.setter
    def packet_type(self, value: int):
        """
        Gets or sets the indication of data format used by this scan. See also SpectrumPacketType
        for decoding to an enum.
        """
        assert type(value) is int
        self._get_wrapped_object_().PacketType = value

    @property
    def scan_type(self) -> str:
        """
        Gets or sets a String defining the scan type, for filtering
        """
        return self._get_wrapped_object_().ScanType

    @scan_type.setter
    def scan_type(self, value: str):
        """
        Gets or sets a String defining the scan type, for filtering
        """
        assert type(value) is str
        self._get_wrapped_object_().ScanType = value

    @property
    def cycle_number(self) -> int:
        """
        Gets or sets the cycle number. Cycle number used to associate events within a
        scan event cycle. For example, on the first cycle of scan events, all the events
        would set this to '1'. On the second cycle, all the events would set this to
        '2'. This field must be set by devices if supporting compound names for filtering.
        However, it may be set in all acquisitions to help processing algorithms.
        """
        return self._get_wrapped_object_().CycleNumber

    @cycle_number.setter
    def cycle_number(self, value: int):
        """
        Gets or sets the cycle number. Cycle number used to associate events within a
        scan event cycle. For example, on the first cycle of scan events, all the events
        would set this to '1'. On the second cycle, all the events would set this to
        '2'. This field must be set by devices if supporting compound names for filtering.
        However, it may be set in all acquisitions to help processing algorithms.
        """
        assert type(value) is int
        self._get_wrapped_object_().CycleNumber = value

    def clone(self) -> ScanStatistics:
        """
        Creates a new object that is a copy of the current instance.
        
        Returns:
        A new object that is a copy of this instance.
        """
        return ScanStatistics._get_wrapper_(self._get_wrapped_object().Clone())

    def copy_to(self, stats: ScanStatistics, deep: bool):
        """
        Copy all fields
        
        Parameters:
        stats:
        Copy into this object
        
        deep:
        If set, make a "deep copy" which will evaluate any lazy items and ensure no internal
        source references
        """
        self._get_wrapped_object().CopyTo(stats._get_wrapped_object_(), deep)

    def deep_clone(self) -> ScanStatistics:
        """
        Produce a deep copy of an object. Must not contain any references into the original.
        
        Returns:
        A deep clone of all objects in this
        """
        return ScanStatistics._get_wrapper_(self._get_wrapped_object().DeepClone())
