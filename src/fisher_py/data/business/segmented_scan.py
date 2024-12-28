from __future__ import annotations
from typing import List
from fisher_py.utils import is_number, to_net_list
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data.business import Range, MassOptions, SimpleScan
from fisher_py.data import PeakOptions


class SegmentedScan(NetWrapperBase):
    """
    Defines a scan with mass range segments.
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.SegmentedScan

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def flags(self) -> List[PeakOptions]:
        """
        Gets or sets flags, such as "saturated" for each peak.
        """
        return [PeakOptions(v) for v in self._get_wrapped_object_().Flags]

    @flags.setter
    def flags(self, value: List[PeakOptions]):
        """
        Gets or sets flags, such as "saturated" for each peak.
        """
        assert type(value) is list
        value = to_net_list(value, int)
        self._get_wrapped_object_().Flags = [v.value for v in value]

    @property
    def intensities(self) -> List[float]:
        """
        Gets or sets the Intensity (or absorbance) values for each point in the scan
        """
        return self._get_wrapped_object_().Intensities

    @intensities.setter
    def intensities(self, value: List[float]):
        """
        Gets or sets the Intensity (or absorbance) values for each point in the scan
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().Intensities = value

    @property
    def positions(self) -> List[float]:
        """
        Gets or sets the positions (mass or wavelength) for each point in the scan
        """
        return self._get_wrapped_object_().Positions

    @positions.setter
    def positions(self, value: List[float]):
        """
        Gets or sets the positions (mass or wavelength) for each point in the scan
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().Positions = value

    @property
    def segment_lengths(self) -> List[int]:
        """
        Gets SegmentLengths.
        """
        return self._get_wrapped_object_().SegmentLengths

    @property
    def segment_sizes(self) -> List[int]:
        """
        Gets or sets the number of data points in each segment
        """
        return self._get_wrapped_object_().SegmentSizes

    @segment_sizes.setter
    def segment_sizes(self, value: List[int]):
        """
        Gets or sets the number of data points in each segment
        """
        assert type(value) is list
        value = to_net_list(value, int)
        self._get_wrapped_object_().SegmentSizes = value

    @property
    def segment_count(self) -> int:
        """
        Gets or sets The number of segments
        """
        return self._get_wrapped_object_().SegmentCount

    @segment_count.setter
    def segment_count(self, value: int):
        """
        Gets or sets The number of segments
        """
        assert type(value) is int
        value = to_net_list(value, int)
        self._get_wrapped_object_().SegmentCount = value

    @property
    def ranges(self) -> List[Range]:
        """
        Gets or sets the Mass ranges for each scan segment
        """
        return [Range._get_wrapper_(r) for r in self._get_wrapped_object_().Ranges]

    @ranges.setter
    def ranges(self, value: List[Range]):
        """
        Gets or sets the Mass ranges for each scan segment
        """
        assert type(value) is list
        value = to_net_list([i._get_wrapped_object_() for i in value], Range._wrapped_type)
        self._get_wrapped_object_().Ranges = value

    @property
    def mass_ranges(self) -> List[Range]:
        """
        Gets the Mass ranges for each scan segment
        """
        return [Range._get_wrapper_(r) for r in self._get_wrapped_object_().MassRanges]

    @property
    def position_count(self) -> int:
        """
        Gets or sets the The size of the position and intensity arrays. The number of
        peaks in the scan (total for all segments)
        """
        return self._get_wrapped_object_().PositionCount

    @position_count.setter
    def position_count(self, value: int):
        """
        Gets or sets the The size of the position and intensity arrays. The number of
        peaks in the scan (total for all segments)
        """
        assert type(value) is int
        value = to_net_list(value, int)
        self._get_wrapped_object_().PositionCount = value

    @property
    def scan_number(self) -> int:
        """
        Gets or sets the he number of this scan.
        """
        return self._get_wrapped_object_().ScanNumber

    @scan_number.setter
    def scan_number(self, value: int):
        """
        Gets or sets the he number of this scan.
        """
        assert type(value) is int
        value = to_net_list(value, int)
        self._get_wrapped_object_().ScanNumber = value

    def from_mass_and_intensities(self, masses: List[float], intensities: List[float]) -> SegmentedScan:
        """
        Create a scan from simple X,Y data. This method creates a scan with one segment.
        For efficiency, the references to the mass and intensity data are maintained
        within the constructed object. If this is not desired, clone the mass and intensity
        arrays on calling this constructor. Masses are assumed to be in ascending order.
        
        Parameters:
        masses:
        Mass data for the scan
        
        intensities:
        Intensity data for the scan
        
        Returns:
        A scan with one segment
        
        Exceptions:
        T:System.ArgumentNullException:
        masses is null.
        
        T:System.ArgumentNullException:
        intensities is null.
        
        T:System.ArgumentException:
        Intensities must have same length as masses
        """
        return SegmentedScan._get_wrapper_(self._get_wrapped_object().FromMassesAndIntensities(masses, intensities))

    def base_intensity(self, ranges: List[Range], tolerance_options: MassOptions) -> float:
        """
        Return the largest intensity (base value) in the ranges supplied
        
        Parameters:
        ranges:
        Ranges of positions (masses, wavelengths)
        
        toleranceOptions:
        If the ranges have equal mass values, then toleranceOptions are used to determine
        a band subtracted from low and added to high to search for matching masses
        
        Returns:
        Largest intensity in all ranges
        """
        assert type(ranges) is list
        assert type(tolerance_options) is MassOptions
        net_ranges = to_net_list([r._get_wrapped_object() for r in ranges], Range._wrapped_type)
        return self._get_wrapped_object().BaseIntensity(net_ranges, tolerance_options._get_wrapped_object_())

    def base_intensity(self, ranges: List[Range], tolerance: float) -> float:
        """
        Return the largest intensity (base value) in the ranges supplies
        
        Parameters:
        ranges:
        Ranges of positions
        
        tolerance:
        If the ranges have equal mass values, then tolerance is subtracted from low and
        added to high to search for matching masses
        
        Returns:
        The largest intensity in all ranges
        """
        assert type(ranges) is list
        assert is_number(tolerance)
        net_ranges = to_net_list([r._get_wrapped_object() for r in ranges], Range._wrapped_type)
        return self._get_wrapped_object().BaseIntensity(net_ranges, float(tolerance))

    def clone(self) -> SegmentedScan:
        """
        Creates a new object that is a copy of the current instance.
        
        Returns:
        A new object that is a copy of this instance.
        """
        return SegmentedScan._get_wrapper_(self._get_wrapped_object().Clone())

    def deep_clone(self) -> SegmentedScan:
        """
        Make a deep clone of this object.
        
        Returns:
        An object containing all data in this, and no shared references
        """
        return SegmentedScan._get_wrapper_(self._get_wrapped_object().DeepClone())

    def index_of_segment_start(self, segment: int) -> int:
        """
        Find the index of the first packet in a segment
        
        Parameters:
        segment:
        segment number (starting from 0)
        
        Returns:
        the index of the first packet in a segment
        """
        return self._get_wrapped_object().IndexOfSegmentStart(segment)

    def sum_intensities(self, ranges: List[Range], tolerance_options: MassOptions) -> float:
        """
        Sum all masses within the ranges
        
        Parameters:
        ranges:
        List of ranges to sum
        
        toleranceOptions:
        If the ranges have equal mass values, then toleranceOptions are used to determine
        a band subtracted from low and added to high to search for matching masses
        
        Returns:
        Sum of intensities in all ranges
        """
        assert type(ranges) is list
        assert type(tolerance_options) is MassOptions
        net_ranges = to_net_list([r._get_wrapped_object() for r in ranges], Range._wrapped_type)
        return self._get_wrapped_object().SumIntensities(net_ranges, tolerance_options._get_wrapped_object_())

    def sum_intensities(self, ranges: List[Range], tolerance: float) -> float:
        """
        Sum all masses within the ranges
        
        Parameters:
        ranges:
        List of ranges to sum
        
        tolerance:
        If the ranges have equal mass values, then tolerance is subtracted from low and
        added to high to search for matching masses
        
        Returns:
        Sum of intensities in all ranges
        """
        return self._get_wrapped_object().SumIntensities(ranges, tolerance)

    def to_simple_scan(self) -> SimpleScan:
        """
        Convert to simple scan. This permits calling code to free up references to unused
        parts of the scan data.
        
        Returns:
        The ThermoFisher.CommonCore.Data.Interfaces.ISimpleScanAccess.
        """
        return SimpleScan._get_wrapper_(self._get_wrapped_object().ToSimpleScan())

    def try_validate(self) -> bool:
        """
        Test if this is a valid object (all streams are not null. All data has same length)
        
        Returns:
        True if valid.
        """
        return self._get_wrapped_object().TryValidate()

    def validate(self):
        """
        Test if this is a valid object (all streams are not null. All data has same length)
        
        Exceptions:
        T:System.ArgumentException:
        is thrown if this instance does not contain valid data.
        """
        self._get_wrapped_object().Validate()
