from __future__ import annotations
from typing import List, Tuple
from fisher_py.data.auto_sampler_information import AutoSamplerInformation
from fisher_py.exceptions.raw_file_exception import NoSelectedDeviceException, NoSelectedMsDeviceException
from fisher_py.raw_file_reader import ScanDependents
from fisher_py.utils import datetime_net_to_py, is_number, to_net_list
from fisher_py.data.business import (
    RunHeader, InstrumentSelection, SampleInformation, CentroidStream, ChromatogramTraceSettings,
    MassOptions, InstrumentData, ScanStatistics, SegmentedScan, LogEntry, HeaderItem, StatusLogValues,
    TuneDataValues, Scan
)
from fisher_py.data.business.chromatogram_signal import ChromatogramData
from fisher_py.raw_file_reader.data_model import WrappedRunHeader
from fisher_py.data import (
    Device, ScanFilter, ScanEvent, FtAverageOptions, FileError, FileHeader, ScanEvents, ErrorLogEntry
)
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.exceptions import RawFileException
from datetime import datetime
import os
import System


class RawFileAccess(NetWrapperBase):
    """
    Enables access to raw files
    """

    def __init__(self, file_path: str=None):
        """
        Create raw file access for given file path

        :param file_path: Path to the raw file
        """
        super().__init__()

        self._run_header = None
        self._instrument_selection = None
        self._sample_information = None

        if file_path is None:
            return

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f'No raw file with path "{file_path}" found.')

        # try to load file
        try:
            self._wrapped_object = ThermoFisher.CommonCore.RawFileReader.RawFileReaderAdapter.FileFactory(file_path)
        except Exception as e:
            raise RawFileException(f'Raw file import failed. {e}')
        
        # determine if import generated an error without raising an exception
        if self.file_error.has_error:
            raise RawFileException(self.file_error.error_message)

    # properties
    
    @property
    def auto_sampler_information(self) -> AutoSamplerInformation:
        """
        Gets the auto sampler (tray) information.
        """
        wrapped_object = self._get_wrapped_object_()
        if hasattr(wrapped_object, 'AutoSamplerInformation'):
            return AutoSamplerInformation._get_wrapper_(wrapped_object.AutoSamplerInformation)
        return None
    
    @property
    def computer_name(self) -> str:
        """
        Gets the name of the computer, used to create this file.
        """
        return self._get_wrapped_object_().ComputerName
    
    @property
    def user_label(self) -> List[str]:
        """
        Gets the user labels of this raw file.
        """
        wrapped_object = self._get_wrapped_object_()
        if hasattr(wrapped_object, 'UserLabel'):
            return tuple(wrapped_object.UserLabel)
        return None

    @property
    def include_reference_and_exception_data(self) -> bool:
        """
        Gets or sets a value indicating whether reference and exception peaks should
        be returned (by default they are not). Reference and exception peaks are internal
        mass calibration data within a scan.
        """
        return self._get_wrapped_object_().IncludeReferenceAndExceptionData

    @include_reference_and_exception_data.setter
    def include_reference_and_exception_data(self, value: bool):
        """
        Gets or sets a value indicating whether reference and exception peaks should
        be returned (by default they are not). Reference and exception peaks are internal
        mass calibration data within a scan.
        """
        assert type(value) is bool
        self._get_wrapped_object_().IncludeReferenceAndExceptionData = value

    @property
    def run_header(self) -> RunHeader:
        """
        Gets the current instrument's run header. The run header records information
        related to all data acquired by this instrument (such as the highest scan number
        "LastSpectrum")
        """
        if self._run_header is None:
            try:
                self._run_header = RunHeader._get_wrapper_(self._get_wrapped_object_().RunHeader)
            except ThermoFisher.CommonCore.Data.Business.NoSelectedDeviceException:
                raise NoSelectedDeviceException()
        return self._run_header

    @property
    def run_header_ex(self) -> WrappedRunHeader:
        """
        Information about the file stream
        """
        try:
            return WrappedRunHeader._get_wrapper_(self._get_wrapped_object_().RunHeaderEx)
        except ThermoFisher.CommonCore.Data.Business.NoSelectedDeviceException:
                raise NoSelectedDeviceException()

    @property
    def instrument_methods_count(self) -> int:
        """
        Gets the number of instruments which have saved method data, within the instrument
        method embedded in this file.
        """
        #TODO: This call fails on POSIX systems but not on Windows.
        # Once new DLLs are available that fix the problem, this
        # try-block can be removed.
        try:
            return self._get_wrapped_object_().InstrumentMethodsCount
        except System.NullReferenceException:
            return None

    @property
    def path(self) -> str:
        """
        Gets the path to original data. A raw file may have been moved or translated
        to other formats. This property always returns the path (folder) where the file
        was created (acquired)
        """
        return self._get_wrapped_object_().Path

    @property
    def file_name(self) -> str:
        """
        Gets the name of acquired file (excluding path).
        """
        return self._get_wrapped_object_().FileName

    @property
    def creation_date(self) -> datetime:
        """
        Gets the date when this data was created.
        """
        return datetime_net_to_py(self._get_wrapped_object_().CreationDate)

    @property
    def selected_instrument(self) -> InstrumentSelection:
        """
        Gets the instrument as last set by a call to ThermoFisher.CommonCore.Data.Interfaces.IRawData.SelectInstrument(ThermoFisher.CommonCore.Data.Business.Device,System.Int32).
        If this has never been set, returns null.
        """
        selected_instrument = self._get_wrapped_object_().SelectedInstrument
        self._instrument_selection = InstrumentSelection(selected_instrument.InstrumentIndex, Device(selected_instrument.DeviceType))
        return self._instrument_selection

    @property
    def sample_information(self) -> SampleInformation:
        """
        Gets various details about the sample (such as comments).
        """
        if self._sample_information is None:
            self._sample_information = SampleInformation._get_wrapper_(self._get_wrapped_object_().SampleInformation)
        return self._sample_information

    @property
    def instrument_count(self) -> int:
        """
        Gets the number of instruments (data streams) in this file. For example, a file
        with an MS detector and a 4 channel UV may have an instrument count of 2. To
        find out how many instruments there are of a particular category call ThermoFisher.CommonCore.Data.Interfaces.IRawData.GetInstrumentCountOfType(ThermoFisher.CommonCore.Data.Business.Device)
        with the desired instrument type. Instrument count related methods could, for
        example, be used to format a list of instruments available to select in the UI
        of an application. To start reading data from a particular instrument, call ThermoFisher.CommonCore.Data.Interfaces.IRawData.SelectInstrument(ThermoFisher.CommonCore.Data.Business.Device,System.Int32).
        """
        return self._get_wrapped_object_().InstrumentCount

    @property
    def is_error(self) -> bool:
        """
        Gets a value indicating whether the last file operation caused an error.
        """
        return self._get_wrapped_object_().IsError

    @property
    def in_acquisition(self) -> bool:
        """
        Gets a value indicating whether the file is being acquired (not complete).
        """
        return self._get_wrapped_object_().InAcquisition

    @property
    def creator_id(self) -> str:
        """
        Gets the name of person creating data.
        """
        return self._get_wrapped_object_().CreatorId
    
    @property
    def file_error(self) -> FileError:
        """
        Gets the file error state.
        """
        wrapped_object = self._get_wrapped_object_()
        if hasattr(wrapped_object, 'FileError'):
            return FileError._get_wrapper_(wrapped_object.FileError)
        return None
    
    @property
    def file_header(self) -> FileHeader:
        """
        Gets the raw file header.
        """
        wrapped_object = self._get_wrapped_object_()
        if hasattr(wrapped_object, 'FileHeader'):
            return FileHeader._get_wrapper_(wrapped_object.FileHeader)
        return None

    @property
    def is_open(self) -> bool:
        """
        Gets a value indicating whether the data file was successfully opened.
        """
        return self._get_wrapped_object_().IsOpen
    
    @property
    def has_instrument_method(self) -> bool:
        """
        Gets a value indicating whether this file has an instrument method.
        """
        return self._get_wrapped_object_().HasInstrumentMethod
    
    @property
    def has_ms_data(self) -> bool:
        """
        Gets a value indicating whether this file has MS data.
        """
        return self._get_wrapped_object_().HasMsData
    
    @property
    def scan_events(self) -> ScanEvents:
        """
        Gets the scan events. This is the set of events which have been programmed in
        advance of collecting data (based on the MS method). This does not analyze any
        scan data.
        """
        try:
            return ScanEvents._get_wrapper_(self._get_wrapped_object_().ScanEvents)
        except ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException as e:
                raise NoSelectedMsDeviceException(e.Message)
    
    @property
    def status_log_plottable_data(self) -> List[Tuple[str, int]]:
        """
        Gets the labels and index positions of the status log items which may be plotted.
        That is, the numeric items. Index is a zero based index into the log record (the
        array returned by GetStatusLogHeaderInformation) Labels names are returned by
        "Key" and the index into the log record is "Value".
        """
        try:
            kv_list = self._get_wrapped_object_().StatusLogPlottableData
            return tuple((kv.Key, kv.Value) for kv in kv_list)
        except ThermoFisher.CommonCore.Data.Business.NoSelectedDeviceException:
                raise NoSelectedDeviceException()
    
    def get_scan_events(self, first_scan_number: int, last_scan_number: int) -> List[ScanEvent]:
        """
        Summary:
            This method permits events to be read as a block for a range of scans, which
            may reduce overheads involved in requesting one by one. Events define how scans
            were acquired. Potentially, in some data models, the same "event" may apply to
            several scans so it is permissible for the same reference to appear multiple
            times.
        
        Parameters:
          firstScanNumber:
            The first scan whose event is needed
        
          lastScanNumber:
            The last scan
        
        Returns:
            An array of scan events
        """
        assert type(first_scan_number) is int
        assert type(last_scan_number) is int
        return [ScanEvent._get_wrapper_(e) for e in self._get_wrapped_object_().GetScanEvents(first_scan_number, last_scan_number)]

    def get_scan_event_string_for_scan_number(self, scan: int) -> List[str]:
        """
        Summary:
            Gets the scan event as a string for a scan.
        
        Parameters:
          scan:
            The scan number.
        
        Returns:
            The event as a string.
        
        Exceptions:
          T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
            Thrown if the selected device is not of type MS
        """
        assert type(scan) is int
        return self._get_wrapped_object_().GetScanEventStringForScanNumber(scan)

    def get_all_instrument_names_from_instrument_method(self) -> List[str]:
        """
        Gets names of all instruments, which have a method stored in the raw file's copy
        of the instrument method file. These names are "Device internal names" which
        map to storage names within an instrument method, and other instrument data (such
        as registry keys). Use "GetAllInstrumentFriendlyNamesFromInstrumentMethod" (in
        IRawDataPlus) to get display names for instruments.
        
        Returns:
        The instrument names.
        """        
        #TODO: This call fails on POSIX systems but not on Windows.
        # Once new DLLs are available that fix the problem, this
        # try-block can be removed.
        try:
            return self._get_wrapped_object_().GetAllInstrumentNamesFromInstrumentMethod()
        except System.NullReferenceException:
            return None

    def get_auto_filters(self) -> List[str]:
        """
        Gets the filter strings for this file. This analyses all scans types in the file.
        It may take some time, especially with data dependent files. Filters are grouped,
        within tolerance (as defined by the MS detector).
        
        Returns:
        A string for each auto filter from the raw file
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if this is called without first selecting an MS detector
        """
        return self._get_wrapped_object_().GetAutoFilters()

    def get_filters(self):
        """
        Summary:
             Calculate the filters for this raw file, and return as an array.
        
         Returns:
             Auto generated list of unique filters
        
         Exceptions:
           T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
             Thrown if the selected device is not of type MS
        """
        return [ScanFilter(f) for f in self._get_wrapped_object_().GetFilters()]

    def get_filter_for_scan_number(self, scan: int) -> ScanFilter:
        """
        Summary:
            Get the filter (scanning method) for a scan number. This returns the scanning
            method in the form of a filter rule set, so that it can be used to select similar
            scans (for example in a chromatogram). This method is only defined for MS detectors.
            Calling for other detectors or with no selected detector is a coding error which
            may result in a null return or exceptions, depending on the implementation.
        
        Parameters:
          scan:
            The scan number.
        
        Returns:
            The ThermoFisher.CommonCore.Data.Interfaces.IScanFilter.
        
        Exceptions:
          T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
            Thrown if the selected device is not of type MS
        """
        return ScanFilter(self._get_wrapped_object_().GetFilterForScanNumber(scan))

    def get_scan_event_for_scan_number(self, scan: int) -> ScanEvent:
        """
        Summary:
            Gets the scan event details for a scan. Determines how this scan was programmed.
        
        Parameters:
          scan:
            The scan number.
        
        Returns:
            The ThermoFisher.CommonCore.Data.Interfaces.IScanEvent interface, to get detailed
            information about a scan.
        
        Exceptions:
          T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
            Thrown if the selected device is not of type MS
        """
        return ScanEvent._get_wrapper_(self._get_wrapped_object_().GetScanEventForScanNumber(scan))

    def get_centroid_stream(self, scan_number: int, include_reference_and_exception_peaks: bool) -> CentroidStream:
        """
        Get the centroids saved with a profile scan. This is only valid for data types
        which support multiple sets of data per scan (such as Orbitrap data). This method
        does not "Centroid profile data".
        
        Parameters:
        scanNumber:
        Scan number
        
        includeReferenceAndExceptionPeaks:
        determines if peaks flagged as ref should be returned
        
        Returns:
        centroid stream for specified scanNumber.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        return CentroidStream._get_wrapper_(self._get_wrapped_object_().GetCentroidStream(scan_number, include_reference_and_exception_peaks))

    def get_chromatogram_data(self, settings: List[ChromatogramTraceSettings], start_scan: int, end_scan: int, tolerance_options: MassOptions=None) -> ChromatogramData:
        """
        Create a chromatogram from the data stream
        
        Parameters:
        settings:
        Definition of how the chromatogram is read
        
        startScan:
        First scan to read from. -1 for "all data"
        
        endScan:
        Last scan to read from. -1 for "all data"
        
        toleranceOptions:
        For mass range or base peak chromatograms, if the ranges have equal low and high
        mass values (within 1.0E-6), then toleranceOptions are used to determine a band
        subtracted from low and added to high to search for matching masses. if this
        is set to "null" then the tolerance is defaulted to +/- 0.5.
        
        Returns:
        Chromatogram points
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.RequiresChromatographicDeviceException:
        Thrown if the selected device is of a type that does not support chromatogram
        generation
        
        T:ThermoFisher.CommonCore.Data.Business.InvalidFilterFormatException:
        Thrown if filters are sent (for MS chromatograms) which cannot be parsed
        """
        net_settings = [s._get_wrapped_object_() for s in settings]

        if tolerance_options is None:
            return ChromatogramData._get_wrapper_(self._get_wrapped_object_().GetChromatogramData(net_settings, start_scan, end_scan))
        else:
            net_options = tolerance_options._get_wrapped_object_()
            return ChromatogramData._get_wrapper_(self._get_wrapped_object_().GetChromatogramData(net_settings, start_scan, end_scan, net_options))

    def get_instrument_count_of_type(self, type_: Device) -> int:
        """
        Get the number of instruments (data streams) of a certain classification. For
        example: the number of UV devices which logged data into this file.
        
        Parameters:
        type:
        The device type to count
        
        Returns:
        The number of devices of this type
        """
        assert type(type_) is Device
        return self._get_wrapped_object_().GetInstrumentCountOfType(type_.value)

    def get_instrument_data(self) -> InstrumentData:
        """
        Gets the definition of the selected instrument.
        
        Returns:
        data about the selected instrument, for example the instrument name
        """
        return InstrumentData._get_wrapper_(self._get_wrapped_object_().GetInstrumentData())

    def get_instrument_method(self, index: int) -> str:
        """
        Gets a text form of an instrument method, for a specific instrument.
        
        Parameters:
        index:
        The index into the count of available instruments. The property "InstrumentMethodsCount",
        determines the valid range of "index" for this call.
        
        Returns:
        A text version of the method. Some instruments do not log this data. Always test
        "string.IsNullOrEmpty" on the returned value.
        """
        assert type(index) is int
        
        #TODO: This call fails on POSIX systems but not on Windows.
        # Once new DLLs are available that fix the problem, this
        # try-block can be removed.
        try:
            return self._get_wrapped_object_().GetInstrumentMethod(index)
        except System.NullReferenceException:
            return None

    def get_instrument_type(self, index: int) -> Device:
        """
        Gets the device type for an instrument data stream
        
        Parameters:
        index:
        The data stream
        
        Returns:
        The device at type the index
        """
        assert type(index) is int
        return Device(self._get_wrapped_object_().GetInstrumentType(index))

    def get_scan_stats_for_scan_number(self, scan_number: int) -> ScanStatistics:
        """
        Get the scan statistics for a scan. For example: The retention time of the scan.
        
        Parameters:
        scanNumber:
        scan number
        
        Returns:
        Statistics for scan
        """
        assert type(scan_number) is int
        return ScanStatistics._get_wrapper_(self._get_wrapped_object_().GetScanStatsForScanNumber(scan_number))

    def get_scan_type(self, scan_number: int) -> str:
        """
        Get a string representing the scan type (for filtering). For more complete tests
        on filters, consider using the IScanFilter interface. If reading data using IRawDataPlus,
        you may use ThermoFisher.CommonCore.Data.Interfaces.IRawDataPlus.GetFilterForScanNumber(System.Int32)
        A filter string (possibly entered from the UI) may be parsed using ThermoFisher.CommonCore.Data.Interfaces.IRawDataPlus.GetFilterFromString(System.String)
        If the RT is known, and not the scan number, use ScanNumberFromRetentionTime
        to convert the time to a scan number.
        
        Parameters:
        scanNumber:
        Scan number whose type is needed
        
        Returns:
        Type of scan, in string format. To compare individual filter fields, the ScanDefinition
        class can be used.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        assert type(scan_number) is int
        return self._get_wrapped_object_().GetScanType(scan_number)

    def get_segmented_scan_from_scan_number(self, scan_number: int, stats: ScanStatistics) -> SegmentedScan:
        """
        Gets scan data for the given scan number. It will also fill stats object, if
        any supplied. For most detector types, this is the only data for the scan, and
        contains either profile or centroid information (depending on the type of scan
        performed). For Orbitrap data (FT packet formats), this returns the first set
        of data for the scan (typically profile). The second set of data (centroids)
        are available from the GetCentroidStream method. The "Segmented" format is used
        for SIM and SRM modes, where there may be multiple mass ranges (segments) of
        a scan. Full scan data has only one segment.
        
        Parameters:
        scanNumber:
        The scan number.
        
        stats:
        statistics for the scan
        
        Returns:
        The segmented scan
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedDeviceException:
        Thrown if no device has been selected
        """
        assert type(scan_number) is int
        assert type(stats) is ScanStatistics
        return SegmentedScan._get_wrapper_(self._get_wrapped_object_().GetSegmentedScanFromScanNumber(scan_number, stats._get_wrapped_object_()))

    def get_segment_event_table(self) -> List[List[str]]:
        """
        Gets the segment event table for the current instrument. This table indicates
        planned scan types for the MS detector. It is usually created from an instrument
        method, by the detector. With data dependent or custom scan types, this will
        not be a complete list of scan types used within the file. If this object implements
        the derived IRawDataPlus interface, then This same data can be obtained in object
        format (instead of string) with the IRawDataPlus property "ScanEvents"
        
        Returns:
        A two dimensional array of events. The first index is segment index (segment
        number-1). The second is event index (event number -1) within the segment.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        return self._get_wrapped_object_().GetSegmentEventTable()

    def get_status_log_entries_count(self) -> int:
        """
        returns the number of entries in the current instrument's status log
        
        Returns:
        The number of available status log entries.
        """
        return self._get_wrapped_object_().GetStatusLogEntriesCount()

    def get_status_log_for_retention_time(self, retention_time: float) -> LogEntry:
        """
        Gets the status log nearest to a retention time.
        
        Parameters:
        retentionTime:
        The retention time.
        
        Returns:
        ThermoFisher.CommonCore.Data.Business.LogEntry object containing status log information.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedDeviceException:
        Thrown if no device has been selected
        """
        assert is_number(retention_time)
        return LogEntry._get_wrapper_(self._get_wrapped_object_().GetStatusLogForRetentionTime(float(retention_time)))

    def get_status_log_header_information(self) -> List[HeaderItem]:
        """
        Returns the header information for the current instrument's status log. This
        defines the format of the log entries.
        
        Returns:
        The headers (list of prefixes for the strings).
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedDeviceException:
        Thrown if no device has been selected
        """
        return [HeaderItem._get_wrapper_(i) for i in self._get_wrapped_object_().GetStatusLogHeaderInformation()]

    def get_status_log_values(self, status_log_index: int, if_formatted: bool) -> StatusLogValues:
        """
        Returns the Status log values for the current instrument, for the given status
        record. This is most likely for diagnostics or archiving. Applications which
        need logged data near a scan should use "GetStatusLogForRetentionTime". Note
        that this does not return the "labels" for the fields.
        
        Parameters:
        statusLogIndex:
        Index into table of status logs
        
        ifFormatted:
        true if they should be formatted as per the data definition for this field (recommended
        for display). Unformatted values may be returned with default precision (for
        float or double) Which may be better for graphing or archiving
        
        Returns:
        The status log values.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedDeviceException:
        Thrown if no device has been selected
        """
        assert type(status_log_index) is int
        assert type(if_formatted) is bool
        return StatusLogValues._get_wrapper_(self._get_wrapped_object_().GetStatusLogValues(status_log_index, if_formatted))

    def get_trailer_extra_header_information(self) -> List[HeaderItem]:
        """
        Gets the trailer extra header information. This is common across all scan numbers.
        This defines the format of additional data logged by an MS detector, at each
        scan. For example, a particular detector may wish to record "analyzer 3 temperature"
        at each scan, for diagnostic purposes. Since this is not a defined field in "ScanHeader"
        it would be created as a custom "trailer" field for a given instrument. The field
        definitions occur only once, and apply to all trailer extra records in the file.
        In the example given, only the numeric value of "analyzer 3 temperature" would
        be logged with each scan, without repeating the label.
        
        Returns:
        The headers defining the "trailer extra" record format.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        return [HeaderItem._get_wrapper_(h) for h in self._get_wrapped_object_().GetTrailerExtraHeaderInformation()]

    def get_trailer_extra_information(self, scan_number: int) -> LogEntry:
        """
        Gets the array of headers and values for this scan number. The values are formatted
        as per the header settings.
        
        Parameters:
        scanNumber:
        The scan for which this information is needed
        
        Returns:
        Extra information about the scan
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        assert type(scan_number) is int
        return LogEntry._get_wrapper_(self._get_wrapped_object_().GetTrailerExtraInformation(scan_number))

    def get_trailer_extra_values(self, scan_number: int, if_formatted: bool) -> List[str]:
        """
        Gets the Trailer Extra values for the specified scan number. If ifFormatted =
        true, then the values will be formatted as per the header settings.
        
        Parameters:
        scanNumber:
        scan whose trailer data is needed
        
        ifFormatted:
        true if the data should be formatted
        
        Returns:
        The strings representing trailer data.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        assert type(scan_number) is int
        assert type(if_formatted) is bool
        return self._get_wrapped_object_().GetTrailerExtraValues(scan_number, if_formatted)

    def get_scan_dependents(self, scan_number: int, filter_precision_decimals: int) -> ScanDependents:
        """
        Summary:
            Get scan dependents. Returns a list of scans, for which this scan was the parent.
        
        Parameters:
          scanNumber:
            The scan number.
        
          filterPrecisionDecimals:
            The filter precision decimals.
        
        Returns:
            Information about how data dependent scanning was performed.
        
        Exceptions:
          T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
            Thrown if the selected device is not of type MS
        """
        assert type(scan_number) is int
        assert type(filter_precision_decimals) is int
        return ScanDependents._get_wrapper_(self._get_wrapped_object_().GetScanDependents(scan_number, filter_precision_decimals))

    def get_tune_data(self, tune_data_index: int) -> LogEntry:
        """
        Gets a text form of the instrument tuning method, at a given index. The number
        of available tune methods can be obtained from GetTuneDataCount.
        
        Parameters:
        tuneDataIndex:
        tune data index
        
        Returns:
        ThermoFisher.CommonCore.Data.Business.LogEntry object containing tune data for
        specified tuneDataIndex.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        assert type(tune_data_index) is int
        return LogEntry._get_wrapper_(self._get_wrapped_object_().GetTuneData(tune_data_index))

    def get_tune_data_count(self) -> int:
        """
        Return the number of tune data entries. Each entry describes MS tuning conditions,
        used to acquire this file.
        
        Returns:
        The number of tune methods saved in the raw file>.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        return self._get_wrapped_object_().GetTuneDataCount()

    def get_tune_data_header_information(self) -> List[HeaderItem]:
        """
        Return the header information for the current instrument's tune data. This defines
        the fields used for a record which defines how the instrument was tuned. This
        method only applies to MS detectors. These items can be paired with the "TuneDataValues"
        to correctly display each tune record in the file.
        
        Returns:
        The headers/>.
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        return [HeaderItem._get_wrapper_(i) for i in self._get_wrapped_object_().GetTuneDataHeaderInformation()]

    def get_tune_data_values(self, tune_data_index: int, if_formatted: bool) -> TuneDataValues:
        """
        Return tune data values for the specified index. This method only applies to
        MS detectors. This contains only the data values, and not the headers.
        
        Parameters:
        tuneDataIndex:
        index into tune tables
        
        ifFormatted:
        true if formatting should be done. Normally you would set "ifFormatted" to true,
        to format based on the precision defined in the header. Setting this to false
        uses default number formatting. This may be better for diagnostic charting, as
        numbers may have higher precision than the default format.
        
        Returns:
        The tune data
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedMsDeviceException:
        Thrown if the selected device is not of type MS
        """
        assert type(tune_data_index) is int
        assert type(if_formatted) is bool
        return TuneDataValues._get_wrapper_(self._get_wrapped_object_().GetTuneDataValues(tune_data_index, if_formatted))

    def is_centroid_scan_from_scan_number(self, scan_number: int) -> bool:
        """
        Test if a scan is centroid format
        
        Parameters:
        scanNumber:
        Number of the scan
        
        Returns:
        True if the scan is centroid format
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedDeviceException:
        Thrown if no device has been selected
        """
        assert type(scan_number) is int
        return self._get_wrapped_object_().IsCentroidScanFromScanNumber(scan_number)

    def refresh_view_of_file(self) -> bool:
        """
        Re-read the current file, to get the latest data. Only meaningful when the raw
        file is InAcquisition when opened, or on the last refresh call. After acquisition
        is completed further calls have no effect.
        For example, the value of "LastSpectrum" in the Run Header of a detector may
        be 60 after a refresh call. Even after new scans become acquired, this value
        will remain at 60, from the application's view of the data, until RefreshViewOfFile
        is called again. If GetRunHeader is called again, the number of scans may now
        be a larger value, such as 100
        
        Returns:
        true, if refresh was OK.
        """
        return self._get_wrapped_object_().RefreshViewOfFile()

    def retention_time_from_scan_number(self, scan_number: int) -> float:
        """
        Get the retention time (minutes) from a scan number
        
        Parameters:
        scanNumber:
        Scan number
        
        Returns:
        Retention time (start time) of scan
        
        Exceptions:
        T:ThermoFisher.CommonCore.Data.Business.NoSelectedDeviceException:
        Thrown if no device has been selected
        """
        assert type(scan_number) is int
        return self._get_wrapped_object_().RetentionTimeFromScanNumber(scan_number)

    def scan_number_from_retention_time(self, time: float) -> int:
        """
        Get the nearest scan number to a retention time
        
        Parameters:
        time:
        Retention time (minutes)
        
        Returns:
        Scan number in the selected instrument which is closest to this time. If there
        are no scans, -1 is returned.
        """
        assert is_number(time)
        return self._get_wrapped_object_().ScanNumberFromRetentionTime(float(time))

    def select_instrument(self, instrument_type: Device, instrument_index: int):
        """
        Choose the data stream from the data source. This must be called before reading
        data from a detector (such as chromatograms or scans). You may call ThermoFisher.CommonCore.Data.Interfaces.IRawData.GetInstrumentCountOfType(ThermoFisher.CommonCore.Data.Business.Device)
        to determine if there is at least one instrument of the required device type.
        
        Parameters:
        instrumentType:
        Type of instrument
        
        instrumentIndex:
        Stream number (1 based)
        """
        assert type(instrument_type) is Device
        assert type(instrument_index) is int
        self._get_wrapped_object_().SelectInstrument(instrument_type.value, instrument_index)

    def default_mass_options(self) -> MassOptions:
        """
        Summary:
            Get the mass tolerance and precision values from a raw file
        
        Parameters:
          rawData:
            Raw file
        
        Returns:
            The default tolerance and filter precision
        """
        return MassOptions._get_wrapper_(ThermoFisher.CommonCore.Data.Extensions.DefaultMassOptions(self._get_wrapped_object_()))

    def average_scans_in_scan_range(self, start_scan: int, end_scan: int, scan_filter: ScanFilter, options: MassOptions=None, average_options: FtAverageOptions=None) -> Scan:
        """
        Summary:
            Gets the average of scans between the given scan numbers, which match the supplied
            filter rules.
        
        Parameters:
          data:
            File to read from
        
          startScan:
            start scan
        
          endScan:
            end scan
        
          filter:
            filter rules

          options:
            mass tolerance settings. If not supplied, these are default from the raw file
        
          averageOptions:
            The average Options (for FT format data).
        
        Returns:
            the averaged scan. Use Scan.ScansCombined to find how many scans were averaged.
        """
        assert type(start_scan) is int
        assert type(end_scan) is int
        assert type(scan_filter) is ScanFilter or type(scan_filter) is str

        if type(scan_filter) is ScanFilter:
            scan_filter = scan_filter._get_wrapped_object_()

        if options is not None:
            assert type(options) is MassOptions
            options = options._get_wrapped_object_()
        if average_options is not None:
            assert type(average_options) is FtAverageOptions
            average_options = average_options._get_wrapped_object_()

        averaged_scan = ThermoFisher.CommonCore.Data.Extensions.AverageScansInScanRange(self._get_wrapped_object_(), start_scan, end_scan, scan_filter, options, average_options)
        return Scan._get_wrapper_(averaged_scan) if averaged_scan is not None else None

    def average_scans(self, scans: List[int], options: MassOptions=None, average_options: FtAverageOptions=None, always_merge_segments: bool=False) -> Scan:
        """
        Summary:
            Calculates the average spectra based upon the list supplied. The application
            should filter the data before making this code, to ensure that the scans are
            of equivalent format. The result, when the list contains scans of different formats
            (such as linear trap MS centroid data added to orbitrap MS/MS profile data) is
            undefined. If the first scan in the list contains "FT Profile", then the FT data
            profile is averaged for each scan in the list. The combined profile is then centroided.
            If the first scan is profile data, but not orbitrap data: All scans are summed,
            starting from the final scan in this list, moving back to the first scan in the
            list, and the average is then computed. For simple centroid data formats: The
            scan stats "TIC" value is used to find the "most abundant scan". This scan is
            then used as the "first scan of the average". Scans are then added to this average,
            taking scans alternatively before and after the apex, merging data within tolerance.
        
        Parameters:
          data:
            File to read from
        
          scans:
            list of scans to average
        
          options:
            mass tolerance settings. If not supplied, these are default from the raw file
        
          averageOptions:
            The average Options (for FT format data).
        
          alwaysMergeSegments:
            Merge segments, even if mass ranges are not similar. Only applies to data with
            1 mass segment
        
        Returns:
            The average of the listed scans. Use Scan.ScansCombined to find how many scans
            were averaged.
        """
        assert type(scans) is list
        assert type(always_merge_segments) is bool
        if options is not None:
            assert type(options) is MassOptions
            options = options._get_wrapped_object_()
        if average_options is not None:
            assert type(average_options) is FtAverageOptions
            average_options = average_options._get_wrapped_object_()
        scans = to_net_list(scans, int)
        return Scan._get_wrapper_(ThermoFisher.CommonCore.Data.Extensions.AverageScans(self._get_wrapped_object_(), scans, options, average_options, always_merge_segments))
    
    def get_error_log_item(self, index: int) -> ErrorLogEntry:
        """
        Summary:
            Gets an entry from the instrument error log.
        
        Parameters:
            index:
                Zero based index. The number of records available is RunHeaderEx.ErrorLogCount
        
        Returns:
            An interface to read a specific log entry
        """
        assert type(index) is int
        net_entry = self._get_wrapped_object_().GetErrorLogItem(index)
        return ErrorLogEntry._get_wrapper_(net_entry) if net_entry else None

    def __enter__(self) -> RawFileAccess:
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dispose()

    def dispose(self):
        """
        Dispose object
        """
        self._get_wrapped_object_().Dispose()


if __name__ == '__main__':
    raw_file_path = r"D:\Nextcloud\Shared\MS\data\00_raw\00_corrected_ion_mass\20210407_15mer_bleomycin.raw"

    with RawFileAccess(raw_file_path) as raw_file:
        raw_file.select_instrument(Device.MS, 1)
        print(raw_file.creator_id)
    