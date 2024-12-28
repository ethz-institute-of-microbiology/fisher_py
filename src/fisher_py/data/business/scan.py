from __future__ import annotations
from fisher_py.data.business.range import Range
from typing import List, Any, TYPE_CHECKING
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data import PeakOptions
from fisher_py.data.business import (
    MassToFrequencyConverter, NoiseAndBaseline, ScanStatistics, SegmentedScan, ToleranceMode, 
    CentroidStream, CachedScanProvider
)
from fisher_py.utils import to_net_list

if TYPE_CHECKING:
    from fisher_py.raw_file_reader import RawFileAccess


class Scan(NetWrapperBase):
    """
    Class to represent a scan
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.Scan

    def __init__(self, *args):
        super().__init__()

        if len(args) == 0:
            self._wrapped_object = self._wrapped_type()
        else:
            if len(args) == 1:
                converter = args[0]
                raw_file_noise = None
            elif len(args) == 2:
                converter, raw_file_noise = args
                assert type(raw_file_noise) is list
                if len(raw_file_noise) > 0:
                    assert type(raw_file_noise[0]) is NoiseAndBaseline
                    raw_file_noise = to_net_list(raw_file_noise, NoiseAndBaseline._wrapped_type)
            else:
                raise ValueError('Unable to create Scan.')

            assert type(converter) is MassToFrequencyConverter
            self._wrapped_object(converter._get_wrapped_object_(), [o._get_wrapped_object_() for o in raw_file_noise])

    @property
    def preferred_base_peak_mass(self) -> float:
        """
        Gets Mass of base peak default data stream (usually centroid stream, if present).
        Falls back to ThermoFisher.CommonCore.Data.Business.Scan.SegmentedScan data if
        centroid stream is not preferred or not present
        """
        return self._get_wrapped_object_().PreferredBasePeakMass

    @property
    def preferred_base_peak_noise(self) -> float:
        """
        Gets Noise of base peak for default data stream (usually centroid stream, if
        present). Falls back to zero if centroid stream is not preferred or not present
        """
        return self._get_wrapped_object_().PreferredBasePeakNoise

    @property
    def preferred_base_peak_resolution(self) -> float:
        """
        Gets Resolution of base peak for default data stream (usually centroid stream,
        if present). Falls back to zero if centroid stream is not preferred or not present
        """
        return self._get_wrapped_object_().PreferredBasePeakResolution

    @property
    def preferred_flags(self) -> List[PeakOptions]:
        """
        Gets peak flags (such as saturated) for default data stream (usually centroid
        stream, if present). Falls back to ThermoFisher.CommonCore.Data.Business.Scan.SegmentedScan
        data if centroid stream is not preferred or not present
        """
        return list(self._get_wrapped_object_().PreferredFlags)

    @property
    def preferred_intensities(self) -> List[float]:
        """
        Gets Intensity for default data stream (usually centroid stream, if present).
        Falls back to ThermoFisher.CommonCore.Data.Business.Scan.SegmentedScan data if
        centroid stream is not preferred or not present
        """
        return list(self._get_wrapped_object_().PreferredIntensities)

    @property
    def preferred_masses(self) -> List[float]:
        """
        Gets the Mass for default data stream (usually centroid stream, if present).
        Falls back to ThermoFisher.CommonCore.Data.Business.Scan.SegmentedScan data if
        centroid stream is not preferred or not present
        """
        return list(self._get_wrapped_object_().PreferredMasses)

    @property
    def preferred_noises(self) -> List[float]:
        """
        Gets Noises for default data stream (usually centroid stream, if present). Returns
        an empty array if centroid stream is not preferred or not present
        """
        return list(self._get_wrapped_object_().PreferredNoises)

    @property
    def preferred_baselines(self) -> List[float]:
        """
        Gets Baselines for default data stream (usually centroid stream, if present).
        Returns an empty array if centroid stream is not preferred or not present
        """
        return list(self._get_wrapped_object_().PreferredBaselines)

    @property
    def scans_combined(self) -> int:
        """
        Gets or sets the number of scans which were combined to create this scan. For
        example: By the scan averager. This can be zero if this is a "scan read from
        a file"
        """
        return self._get_wrapped_object_().ScansCombined

    @scans_combined.setter
    def scans_combined(self, value: int):
        """
        Gets or sets the number of scans which were combined to create this scan. For
        example: By the scan averager. This can be zero if this is a "scan read from
        a file"
        """
        assert type(value) is int
        self._get_wrapped_object_().ScansCombined = value

    @property
    def preferred_base_peak_intensity(self) -> float:
        """
        Gets peak flags (such as saturated) for default data stream (usually centroid
        stream, if present). Falls back to ThermoFisher.CommonCore.Data.Business.Scan.SegmentedScan
        data if centroid stream is not preferred or not present
        """
        return self._get_wrapped_object_().PreferredBasePeakIntensity

    @property
    def scan_statistics(self) -> ScanStatistics:
        """
        Gets or sets Header information for the scan
        """
        return ScanStatistics._get_wrapper_(self._get_wrapped_object_().ScanStatistics)

    @scan_statistics.setter
    def scan_statistics(self, value: ScanStatistics):
        """
        Gets or sets Header information for the scan
        """
        assert type(value) is ScanStatistics
        self._get_wrapped_object_().ScanStatistics = value._get_wrapped_object_()

    @property
    def scan_statistics_access(self) -> ScanStatistics:
        """
        Gets Header information for the scan
        """
        return ScanStatistics._get_wrapper_(self._get_wrapped_object_().ScanStatisticsAccess)

    @property
    def scan_type(self) -> str:
        """
        Gets or sets Type of scan (for filtering)
        """
        return self._get_wrapped_object_().ScanType

    @scan_type.setter
    def scan_type(self, value: str):
        """
        Gets or sets Type of scan (for filtering)
        """
        assert type(value) is str
        self._get_wrapped_object_().ScanType = value

    @property
    def segmented_scan(self) -> SegmentedScan:
        """
        Gets or sets The data for the scan
        """
        return SegmentedScan._get_wrapper_(self._get_wrapped_object_().SegmentedScan)

    @segmented_scan.setter
    def segmented_scan(self, value: SegmentedScan):
        """
        Gets or sets The data for the scan
        """
        assert type(value) is SegmentedScan
        self._get_wrapped_object_().SegmentedScan = value._get_wrapped_object_()

    @property
    def segmented_scan_access(self) -> SegmentedScan:
        """
        Gets The data for the scan
        """
        return SegmentedScan._get_wrapper_(self._get_wrapped_object_().SegmentedScanAccess)

    @property
    def subtraction_pointer(self) -> Any:
        """
        Gets or sets IScanSubtract interface pointer.
        
        Returns:
        Interface to perform subtraction
        """
        return self._get_wrapped_object_().SubtractionPointer

    @subtraction_pointer.setter
    def subtraction_pointer(self, value: Any):
        """
        Gets or sets IScanSubtract interface pointer.
        
        Returns:
        Interface to perform subtraction
        """
        self._get_wrapped_object_().SubtractionPointer = value

    @property
    def scan_adder(self) -> Any:
        """
        Gets or sets IScanAdd interface. This delegates addition of FT profile scans.
        
        Returns:
        Interface to perform addition
        """
        return self._get_wrapped_object_().ScanAdder

    @scan_adder.setter
    def scan_adder(self, value: Any):
        """
        Gets or sets IScanAdd interface. This delegates addition of FT profile scans.
        
        Returns:
        Interface to perform addition
        """
        self._get_wrapped_object_().ScanAdder = value

    @property
    def preferred_resolutions(self) -> List[float]:
        """
        Gets Resolutions for default data stream (usually centroid stream, if present).
        Returns an empty array if centroid stream is not preferred or not present
        """
        return self._get_wrapped_object_().PreferredResolutions

    @property
    def prefer_centroids(self) -> bool:
        """
        Gets or sets a value indicating whether, when requesting "Preferred data", the
        centroid stream will be returned. For example "ThermoFisher.CommonCore.Data.Business.Scan.PreferredMasses",
        "ThermoFisher.CommonCore.Data.Business.Scan.PreferredIntensities". If this property
        is false, or there is no centroid stream, then these methods will return the
        data from ThermoFisher.CommonCore.Data.Business.Scan.SegmentedScan. For greater
        efficiency, callers should cache the return of "ThermoFisher.CommonCore.Data.Business.Scan.PreferredMasses".
        Typically data processing, such as elemental compositions, should use these methods.
        """
        return self._get_wrapped_object_().PreferCentroids

    @prefer_centroids.setter
    def prefer_centroids(self, value: bool):
        """
        Gets or sets a value indicating whether, when requesting "Preferred data", the
        centroid stream will be returned. For example "ThermoFisher.CommonCore.Data.Business.Scan.PreferredMasses",
        "ThermoFisher.CommonCore.Data.Business.Scan.PreferredIntensities". If this property
        is false, or there is no centroid stream, then these methods will return the
        data from ThermoFisher.CommonCore.Data.Business.Scan.SegmentedScan. For greater
        efficiency, callers should cache the return of "ThermoFisher.CommonCore.Data.Business.Scan.PreferredMasses".
        Typically data processing, such as elemental compositions, should use these methods.
        """
        assert type(value) is bool
        self._get_wrapped_object_().PreferCentroids = value

    @property
    def is_user_tolerance(self) -> bool:
        """
        Gets or sets a value indicating whether the User Tolerance value is being used.
        """
        return self._get_wrapped_object_().IsUserTolerance

    @is_user_tolerance.setter
    def is_user_tolerance(self, value: bool):
        """
        Gets or sets a value indicating whether the User Tolerance value is being used.
        """
        assert type(value) is bool
        self._get_wrapped_object_().IsUserTolerance = value

    @property
    def tolerance_unit(self) -> ToleranceMode:
        """
        Gets or sets the Tolerance value.
        """
        return ToleranceMode(self._get_wrapped_object_().ToleranceUnit)

    @tolerance_unit.setter
    def tolerance_unit(self, value: ToleranceMode):
        """
        Gets or sets the Tolerance value.
        """
        assert type(value) is ToleranceMode
        self._get_wrapped_object_().ToleranceUnit = value.value

    @property
    def mass_resolution(self) -> float:
        """
        Gets or sets the mass resolution for all scan arithmetic operations
        """
        return self._get_wrapped_object_().MassResolution

    @mass_resolution.setter
    def mass_resolution(self, value: float):
        """
        Gets or sets the mass resolution for all scan arithmetic operations
        """
        assert type(value) is float
        self._get_wrapped_object_().MassResolution = value

    @property
    def centroid_scan(self) -> CentroidStream:
        """
        Gets or sets A second data stream for the scan
        """
        return CentroidStream._get_wrapper_(self._get_wrapped_object_().CentroidScan)

    @centroid_scan.setter
    def centroid_scan(self, value: CentroidStream):
        """
        Gets or sets A second data stream for the scan
        """
        assert type(value) is CentroidStream
        self._get_wrapped_object_().CentroidScan = value._get_wrapped_object_()

    @property
    def always_merge_segments(self) -> bool:
        """
        Get or sets a value indicating whether scan + and - operators will merge data
        from scans which were not scanned over a similar range. Only applicable when
        scans only have a single segment. By default: Scans are considered incompatible
        if: The span of the scanned mass range differs by 10% The start or end of the
        scanned mass range differs by 10% If this is set as "true" then any mass ranges
        will be merged.
        """
        return self._get_wrapped_object_().AlwaysMergeSegments

    @always_merge_segments.setter
    def always_merge_segments(self, value: bool):
        """
        Get or sets a value indicating whether scan + and - operators will merge data
        from scans which were not scanned over a similar range. Only applicable when
        scans only have a single segment. By default: Scans are considered incompatible
        if: The span of the scanned mass range differs by 10% The start or end of the
        scanned mass range differs by 10% If this is set as "true" then any mass ranges
        will be merged.
        """
        assert type(value) is bool
        self._get_wrapped_object_().AlwaysMergeSegments = value

    @property
    def has_centroid_stream(self) -> bool:
        """
        Gets a value indicating whether this scan has a centroid stream.
        """
        return self._get_wrapped_object_().HasCentroidStream

    @property
    def centroid_stream_access(self) -> CentroidStream:
        """
        Gets A second data stream for the scan
        """
        return CentroidStream._get_wrapper_(self._get_wrapped_object_().CentroidStreamAccess)

    @property
    def has_noise_table(self) -> bool:
        """
        Gets a value indicating whether this scan has a noise table. This will be true
        only if the scan was constructed with the overload containing this table. Note
        that this is not related to having "noise and baseline" values with centroid
        stream data. This is a separate table, used for spectrum averaging and subtraction
        of orbitrap data
        """
        return self._get_wrapped_object_().HasNoiseTable

    @staticmethod
    def at_time(raw_file: RawFileAccess, time: float) -> Scan:
        """
        Create a scan object from a file and a retention time.
        
        Parameters:
        rawFile:
        File to read from
        
        time:
        time of Scan number to read
        
        Returns:
        The scan read, or null of the scan number if not valid
        """
        return Scan._get_wrapper_(Scan._wrapped_type.AtTime(raw_file._get_wrapped_object_(), time))

    @staticmethod
    def can_merged_scan( identical_flag: bool, current_scan: Scan, to_merge: Scan) -> bool:
        """
        test if 2 scans can be averaged or subtracted.
        
        Parameters:
        identicalFlag:
        Returned as "true" if all segments are the same
        
        currentScan:
        Current scan object
        
        toMerge:
        The scan to possibly add
        
        Returns:
        true if scans can be merged
        """
        return Scan._wrapped_type.CanMergeScan(identical_flag, current_scan._get_wrapped_object_(), to_merge._get_wrapped_object_())

    @staticmethod
    def create_scan_reader(cache_size: int) -> CachedScanProvider:
        """
        Create an object which can be used to read scans from a file, with optional caching.
        This is valuable if repeated operations (such as averaging) are expected over
        the same region of data. Scans returned from each call are unique objects, even
        if called repeatedly with the same scan number.
        
        Parameters:
        cacheSize:
        Number of scans cached. When set to 1 or more, this creates a FIFO, keeping track
        of the most recently read scans. If a scan in the FIFO is requested again, it
        is pulled from the cache. If a scan is not in the cache, then a new scan is read
        from the file. If the cache is full, the oldest scan is dropped. The newly read
        scan is that added to the FIFO cache. If size is set to 0, this makes a trivial
        object with no overheads, that directly gets scans from the file.
        
        Returns:
        Object to read scans from a file
        """
        return CachedScanProvider._get_wrapper_(Scan._wrapped_type.CreateScanReader(cache_size))

    @staticmethod
    def from_file(raw_file: RawFileAccess, scan_number: int) -> Scan:
        """
        Create a scan object from a file and a scan number.
        
        Parameters:
        rawFile:
        File to read from
        
        scanNumber:
        Scan number to read
        
        Returns:
        The scan read, or null of the scan number if not valid
        """
        assert type(scan_number) is int
        return Scan._get_wrapper_(Scan._wrapped_type.FromFile(raw_file._get_wrapped_object_(), scan_number))

    def to_centroid(current_scan: Scan) -> Scan:
        """
        Converts the segmented scan to centroid scan. Used to centroid profile data.
        
        Parameters:
        currentScan:
        The scan to centroid
        
        Returns:
        The centroided version of the scan
        """
        return Scan._get_wrapper_(Scan._wrapped_type.ToCentroid(current_scan._get_wrapped_object_()))

    def deep_clone(self) -> Scan:
        """
        Make a deep clone of this scan.
        
        Returns:
        An object containing all data in the input, and no shared references
        """
        return Scan._get_wrapper_(self._get_wrapped_object().DeepClone())

    def generate_frequency_table(self) -> List[float]:
        """
        generate frequency table for this scan. This method only applied to "FT" format
        scans which have mass to frequency calibration data. When a scan in constructed
        from processing algorithms, such as averaging, a frequency to mass converter
        is used to create this scan. This same converter can be used to create a frequency
        table, which would be needed when writing averaged (or subtracted) data to a
        raw file.
        
        Returns:
        The frequency table.
        """
        return self._get_wrapped_object().GenerateFrequencyTable()

    def generate_noise_table(self) -> List[NoiseAndBaseline]:
        """
        Generates a "noise and baseline table". This table is only relevant to FT format
        data. For other data, an empty list is returned. This table is intended for use
        when exporting processed (averaged, subtracted) scans to a raw file. If this
        scan is the result of a calculation such as "average of subtract" it may be constructed
        using an overload which includes a noise and baseline table. If so: that tale
        is returned. Otherwise, a table is generated by extracting data from the scan.
        
        Returns:
        The nose and baseline data
        """
        return [NoiseAndBaseline._get_wrapper_(n) for n in self._get_wrapped_object().GenerateNoiseTable()]

    def slice(self, mass_ranges: List[Range], trim_mass_range: bool, expand_profiles: bool) -> Scan:
        """
        Return a slice of a scan which only contains data within the supplied mass Range
        or ranges. For example: For a scan with data from m/z 200 to 700, and a single
        mass range of 300 to 400: This returns a new scan containing all data with the
        range 300 to 400.
        
        Parameters:
        massRanges:
        The mass ranges, where data should be retained. When multiple ranges are supplied,
        all data which is in at least one range is included in the returned scan
        
        trimMassRange:
        If this is true, then the scan will reset the scan's mass range to the bounds
        of the supplied mass ranges
        
        expandProfiles:
        This setting only applies when the scan has both profile and centroid data. If
        true: When there isa centroid near the start or end of a range, and the first
        or final "above zero" section of the profile includes that peak, then the profile
        is extended, to include the points which contribute to that peak. A maximum of
        10 points may be added
        
        Returns:
        A copy of the scan, with only the data in the supplied ranges
        """
        net_mass_ranges = [r._get_wrapped_object_() for r in mass_ranges]
        return Scan._get_wrapper_(self._get_wrapped_object().Slice(net_mass_ranges, trim_mass_range, expand_profiles))
