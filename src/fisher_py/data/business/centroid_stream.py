from __future__ import annotations
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data import PeakOptions
from fisher_py.data.business import Range, LabelPeak, MassOptions, SimpleScan, SegmentedScan, ScanStatistics
from fisher_py.utils import to_net_list
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from fisher_py.data.business import Scan


class CentroidStream(NetWrapperBase):

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.CentroidStream

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def noises(self) -> List[float]:
        """
        Gets or sets the list of noise level near peak
        """
        return list(self._get_wrapped_object_().Noises)

    @noises.setter
    def noises(self, value: List[float]):
        """
        Gets or sets the list of noise level near peak
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().Noises = value

    @property
    def masses(self) -> List[float]:
        """
        Gets or sets the list of masses of each centroid
        """
        return list(self._get_wrapped_object_().Masses)

    @masses.setter
    def masses(self, value: List[float]):
        """
        Gets or sets the list of masses of each centroid
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().Masses = value

    @property
    def length(self) -> int:
        """
        Gets or sets the number of centroids
        """
        return self._get_wrapped_object_().Length

    @length.setter
    def length(self, value: int):
        """
        Gets or sets the number of centroids
        """
        assert type(value) is int
        self._get_wrapped_object_().Length = value

    @property
    def intensities(self) -> List[float]:
        """
        Gets or sets the list of Intensities for each centroid
        """
        return list(self._get_wrapped_object_().Intensities)

    @intensities.setter
    def intensities(self, value: List[float]):
        """
        Gets or sets the list of Intensities for each centroid
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().Intensities = value

    @property
    def flags(self) -> List[PeakOptions]:
        """
        Gets or sets the flags for the peaks (such as reference)
        """
        return [PeakOptions(f) for f in self._get_wrapped_object_().Flags]

    @flags.setter
    def flags(self, value: List[PeakOptions]):
        """
        Gets or sets the flags for the peaks (such as reference)
        """
        assert type(value) is list
        value = to_net_list([v.value for v in value], int)
        self._get_wrapped_object_().Flags = value

    @property
    def coefficients_count(self) -> int:
        """
        Gets or sets the coefficients count.
        """
        return self._get_wrapped_object_().CoefficientsCount

    @coefficients_count.setter
    def coefficients_count(self, value: int):
        """
        Gets or sets the coefficients count.
        """
        assert type(value) is int
        self._get_wrapped_object_().CoefficientsCount = value

    @property
    def coefficients(self) -> List[float]:
        """
        Gets or sets the calibration Coefficients
        """
        return list(self._get_wrapped_object_().Coefficients)

    @coefficients.setter
    def coefficients(self, value: List[float]):
        """
        Gets or sets the calibration Coefficients
        """
        assert type(value) is list
        self._get_wrapped_object_().Coefficients = value

    @property
    def charges(self) -> List[float]:
        """
        Gets or sets the list of charge calculated for peak
        """
        return list(self._get_wrapped_object_().Charges)

    @charges.setter
    def charges(self, value: List[float]):
        """
        Gets or sets the list of charge calculated for peak
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().Charges = value

    @property
    def base_peak_resolution(self) -> float:
        """
        Gets the resolution of most intense peak
        """
        return self._get_wrapped_object_().BasePeakResolution

    @property
    def base_peak_noise(self) -> float:
        """
        Gets the noise of most intense peak
        """
        return self._get_wrapped_object_().BasePeakNoise

    @property
    def base_peak_mass(self) -> float:
        """
        Gets the mass of most intense peak
        """
        return self._get_wrapped_object_().BasePeakMass

    @property
    def base_peak_intensity(self) -> float:
        """
        Gets the intensity of most intense peak
        """
        return self._get_wrapped_object_().BasePeakIntensity

    @property
    def baselines(self) -> List[float]:
        """
        Gets or sets the list of baseline at each peak
        """
        return list(self._get_wrapped_object_().Baselines)

    @baselines.setter
    def baselines(self, value: List[float]):
        """
        Gets or sets the list of baseline at each peak
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().Baselines = value

    @property
    def resolutions(self) -> List[float]:
        """
        Gets or sets resolution of each peak
        """
        return list(self._get_wrapped_object_().Resolutions)

    @resolutions.setter
    def resolutions(self, value: List[float]):
        """
        Gets or sets resolution of each peak
        """
        assert type(value) is list
        value = to_net_list(value, float)
        self._get_wrapped_object_().Resolutions = value

    @property
    def scan_number(self) -> int:
        """
        Gets or sets the scan Number
        """
        return self._get_wrapped_object_().ScanNumber

    @scan_number.setter
    def scan_number(self, value: int):
        """
        Gets or sets the scan Number
        """
        assert type(value) is int
        self._get_wrapped_object_().ScanNumber = value

    def base_intensity(self, ranges: List[Range], tolerance_options: MassOptions) -> float:
        """
        Return the largest intensity (base value) in the ranges supplies
        
        Parameters:
        ranges:
        Ranges of masses
        
        toleranceOptions:
        If the ranges have equal mass values, then toleranceOptions are used to determine
        a band subtracted from low and added to high to search for matching masses
        
        Returns:
        Largest intensity in all ranges
        """
        net_ranges = [v.value for v in ranges]
        return self._get_wrapped_object().BaseIntensity(net_ranges, tolerance_options._get_wrapped_object_())

    def clear(self):
        """
        Clears all the data.
        """
        self._get_wrapped_object().Clear()

    def clone(self) -> object:
        """
        Creates a new object that is a copy of the current instance.
        
        Returns:
        A new object that is a copy of this instance.
        """
        return self._get_wrapped_object().Clone()

    def deep_clone(self) -> CentroidStream:
        """
        Make a deep clone of this object.
        
        Returns:
        An object containing all data in this, and no shared references
        """
        return CentroidStream._get_wrapper_(self._get_wrapped_object().DeepClone())

    def get_centroids(self) -> List[LabelPeak]:
        """
        Get the list centroids.
        
        Returns:
        The centroids in the scan
        """
        return [LabelPeak._get_wrapper_(c) for c in self._get_wrapped_object().GetCentroids()]

    def get_label_peak(self, index: int) -> LabelPeak:
        """
        Convert the data for a given peak in this stream into a LabelPeak
        
        Parameters:
        index:
        The index of the peak to convert.
        
        Returns:
        Extracted data for the selected peak
        """
        return LabelPeak._get_wrapper_(self._get_wrapped_object().GetLabelPeak(index))

    def get_label_peaks(self) -> List[LabelPeak]:
        """
        Convert the data into LabelPeak objects
        
        Returns:
        """
        return [LabelPeak._get_wrapper_(p) for p in self._get_wrapped_object().GetLabelPeaks()]

    def refresh_base_details(self):
        """
        Forces re-computation of Base peaks , intensities.
        """
        self._get_wrapped_object().RefreshBaseDetails()

    def set_label_peaks(self, label_peaks: List[LabelPeak]) -> bool:
        """
        Convert data into this object from an array of LabelPeaks
        
        Parameters:
        labelPeaks:
        
        Returns:
        true on success. False if the labels peaks are null or empty
        """
        return self._get_wrapped_object().SetLabelPeaks([p._wrapped_object for p in label_peaks])

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
        net_ranges = to_net_list([v.value for v in ranges], Range._wrapped_type)
        return self._get_wrapped_object().SumIntensities(net_ranges, tolerance_options._get_wrapped_object_())

    def sum_masses(self, ranges: List[Range], tolerance: float) -> float:
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
        net_ranges = to_net_list([v.value for v in ranges], Range._wrapped_type)
        return self._get_wrapped_object().SumMasses(net_ranges, tolerance)

    def to_scan(self, original_scan_stats: ScanStatistics) -> Scan:
        """
        Convert to Scan. This feature is intended for use where an application or algorithm
        needs data in "Scan" format, with centroid information in the "SegmentedScan"
        property of the Scan. (such as typical centroid data from ITMS), but the data
        in this scan came from an FTMS detector, which would have the profile data in
        "SegmentedScan" and the centroid data in this object. The data is first converted
        to SegmentedScan format (using ToSegmentedScan) then a new Scan is made containing
        that data (with no data in "CentroidStream). Data from this object is duplicated
        (deep copy), such that changing values in the returned object will not affect
        data in this object. This initializes the returned scan's "ScanStatistics" based
        on the returned mass and intensity data. If the (optional) originalScanStats
        parameter is included, information from that is used to initialize RT, scan number
        and other fields which cannot be calculated from this data. The only values updated
        in the scan statistics are "BasePeakMass" and "BasePeakIntenity". All other values
        are either as copied from the supplied parameter, or defaults. Application should
        set any other values needed in the Scan, such as "ScansCombined, ToleranceUnit,
        MassResolution", which cannot be determined from the supplied parameters.
        
        Parameters:
        originalScanStats:
        If this is supplied, the scan statistics are initialized as a deep clone of the
        supplied object (so that RT etc. get preserved) then the values of BasePeakMass
        and BasePeakIntensity are updated from this object
        
        Returns:
        The ThermoFisher.CommonCore.Data.Business.SegmentedScan.
        """
        from fisher_py.data.business import Scan
        return Scan._get_wrapper_(self._get_wrapped_object().ToScan(original_scan_stats._get_wrapped_object_()))

    def to_segmented_scan(self) -> SegmentedScan:
        """
        Convert to segmented scan. This feature is intended for use where an application
        or algorithm in "SegmentedScan" format, such as typical centroid data from ITMS,
        but the data in this scan came from an FTMS detector, which would have the profile
        data in "SegmentedScan" and the centroid data in this object. Data from this
        object is duplicated (deep copy), such that changing values in the returned object
        will not affect data in this object.
        
        Returns:
        The ThermoFisher.CommonCore.Data.Business.SegmentedScan.
        """
        return SegmentedScan._get_wrapper_(self._get_wrapped_object().ToSegmentedScan())

    def to_simple_scan(self) -> SimpleScan:
        """
        there can be an advantage in doing this conversion, as when this object goes
        out of scope the converted object only holds the mass and intensity refs, and
        will need less memory.
        
        Returns:
        The ThermoFisher.CommonCore.Data.Business.SimpleScan.
        """
        return SimpleScan._get_wrapper_(self._get_wrapped_object().ToSimpleScan())

    def try_validate(self) -> bool:
        """
        Test if this is a valid object (all streams are not null. All data has same length)
        
        Returns:
        true if the object has valid data in it.
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
