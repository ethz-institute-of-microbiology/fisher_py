"""
A Python example program showing how to use RAWFileReader.  More information on the RAWFileReader methods used
in this example and the other methods available in RAWFileReader can be found in the RAWFileReader user
documentation, that is installed with the RAWFileReader software.
This program has been tested with RAWFileReader 4.0.22  Changes maybe necessary with other versions
of RAWFileReader.
"""

import sys
import os
import traceback
from typing import List
from fisher_py.raw_file_reader import RawFileReaderAdapter, RawFileAccess
from fisher_py.data.business import GenericDataTypes, ChromatogramTraceSettings, TraceType, ChromatogramSignal, SpectrumPacketType, Scan
from fisher_py.data.filter_enums import MsOrderType
from fisher_py.data import Device, ToleranceUnits
from fisher_py.mass_precision_estimator import PrecisionEstimate


class InclusionListItem(object):
    """
    The object used to store the inclusion/exclusion list items.
    """
    def __init__(self, descriptor: str, mass: float, threshold: float):
        self.descriptor = descriptor
        self.mass = mass
        self.threshold = threshold
        self.scan_number = 0


def list_trailer_extra_fields(raw_file: RawFileAccess):
    """
    Reads and reports the trailer extra data fields present in the RAW file.
    """
    # Get the Trailer Extra data fields present in the RAW file
    trailer_fields = raw_file.get_trailer_extra_header_information()

    # Display each value
    i = 0
    print('Trailer Extra Data Information:')

    for field in trailer_fields:
        print(f'   Field {i} = {field.label} storing data of type {field.data_type}')
        i += 1
    print('')


def list_status_log(raw_file: RawFileAccess, start_scan: int, end_scan: int):
    """
    Reads and reports the status log data fields present in the RAW file.
    """
    # Get the status log header information
    status_log = raw_file.get_status_log_header_information()

    # Display each value that is part of the status log.  They are stored as label/data type pairs
    i = 0
    print('Status Log Information:')

    for field in status_log:
        if field.label is not None and field != '' and field.data_type != GenericDataTypes.NULL:
            print(f'   Field {i} = {field.label} storing data of type {field.data_type}')
        i += 1
    print('')

    # Display the value for item 10 in the status log for each scan
    print('Status Information for item 10:')

    for scan in range(start_scan, end_scan):
        # Get the status log for this scan
        time = raw_file.retention_time_from_scan_number(scan)
        log_entry = raw_file.get_status_log_for_retention_time(time)

        # Print the values for one item
        print(f'   Scan {scan} = {log_entry.values[10]}')
    print('')


def get_inclusion_exclusion_list(raw_file: RawFileAccess, mass_tolerance: float) -> List[InclusionListItem]:
    """
    Reads the inclusion/exclusion list from the mass spectrometer method in the RAW file
    """
    # Select the MS instrument
    raw_file.select_instrument(Device.MS, 1)

    # Get the instrument method item(s) and look for the inclusion/exclusion list
    # which will be flagged by the "Mass List Table"
    inclusion_strings = list()

    for i in range(raw_file.instrument_methods_count):
        method_text = raw_file.get_instrument_method(i)
        if method_text is not None and 'Mass List Table' in method_text:
            save_line = False
            split_method = method_text.split('\n')

            for line in split_method:
                if 'Mass List Table' in line:
                    save_line = True
                elif 'End Mass List Table' in line:
                    save_line = False
                elif save_line:
                    inclusion_strings.append(line)
    
    # Create the inclusion/exclusion list 
    inclusion_list = list()

    # Convert each line from the inclusion/exclusion mass table into InclusionListItem objects
    # and add them to the inclusion/exclusion list.
    for line in inclusion_strings:
        # Skip the title line
        if 'CompoundName' in line:
            continue

        #  Split the line into its separate fields
        fields = line.split('|')

        if len(fields) == 4:
            inclusion_list.append(InclusionListItem(*fields))

    # Get the actual scan number for each mass in the inclusion list
    for scan in range(raw_file.run_header_ex.first_spectrum, raw_file.run_header_ex.last_spectrum):
        # Get the scan filter and event for this scan number        
        scan_filter = raw_file.get_filter_for_scan_number(scan)
        scan_event = raw_file.get_scan_event_for_scan_number(scan)

        # Only consider MS2 scans when looking for the spectrum corr3e
        if scan_filter.ms_order == MsOrderType.Ms2:
            # Get the reaction information in order to get the precursor mass for this spectrum
            reaction = scan_event.get_reaction(0)
            precursor_mass = reaction.precursor_mass
            tolerance = precursor_mass * mass_tolerance

            for item in inclusion_list:
                if item.mass >= precursor_mass - tolerance and item.mass <= precursor_mass + tolerance:
                    item.scan_numer = scan
                    break

    return inclusion_list


def get_chromatogram(raw_file: RawFileAccess, start_scan: int, end_scan: int, output_data: bool):
    """
    Reads the base peak chromatogram for the RAW file
    """
    # Define the settings for getting the Base Peak chromatogram
    settings = ChromatogramTraceSettings(TraceType.BasePeak)

    # Get the chromatogram from the RAW file. 
    data = raw_file.get_chromatogram_data([settings], start_scan, end_scan)

    # Split the data into the chromatograms
    trace = ChromatogramSignal.from_chromatogram_data(data)

    if trace[0].length > 0:
        # Print the chromatogram data (time, intensity values)
        print(f'Base Peak chromatogram ({trace[0].length} points)')

        if output_data:
            for i in range(trace[0].length):
                print(f'  {i} - {trace[0].times[i]}, {trace[0].intensities[i]}')
    print('')


def read_scan_information(raw_file: RawFileAccess, first_scan_number: int, last_scan_number: int, output_data: bool):
    """
    Reads the general scan information for each scan in the RAW file using the scan filter object and also the
    trailer extra data section for that same scan.
    """
    # Read each scan in the RAW File
    for scan in range(first_scan_number, last_scan_number+1):
        # Get the retention time for this scan number.  This is one of two comparable functions that will
        # convert between retention time and scan number.
        time = raw_file.retention_time_from_scan_number(scan)

        # Get the scan filter for this scan number
        # NOTE: A scan filter can also be created from the filter string using the GetFilterFromString in the
        # RawFileAccess.
        scan_filter = raw_file.get_filter_for_scan_number(scan)

        # Get the scan event for this scan number
        scan_event = raw_file.get_scan_event_for_scan_number(scan)
        
        # Get the ionizationMode, MS2 precursor mass, collision energy, and isolation width for each scan
        if scan_filter.ms_order == MsOrderType.Ms2:
            # Get the reaction information for the first precursor
            reaction = scan_event.get_reaction(0)

            precursor_mass = reaction.precursor_mass
            collision_energy = reaction.collision_energy
            isolation_width = reaction.isolation_width
            monoisotopic_mass = 0.0
            master_scan = 0
            ionization_mode = scan_filter.ionization_mode
            order = scan_filter.ms_order

            # Get the trailer extra data for this scan and then look for the monoisotopic m/z value in the 
            # trailer extra data list
            trailer_data = raw_file.get_trailer_extra_information(scan)

            for i in range(trailer_data.length):
                if trailer_data.labels[i] == 'Monoisotopic M/Z:':
                    monoisotopic_mass = float(trailer_data.values[i])
                if trailer_data.labels[i] == 'Master Scan Number:' or trailer_data.labels[i] == 'Master Index:':
                    master_scan = int(trailer_data.values[i])

            if output_data:
                print(f'Scan number {scan} @ time {time} - Master scan = {master_scan}, Ionization mode={ionization_mode}, MS Order={order}, Precursor mass={precursor_mass}, Monoisotopic Mass = {monoisotopic_mass}, Collision energy={collision_energy}, Isolation width={isolation_width}')
        elif scan_filter.ms_order == MsOrderType.Ms:
            scan_dependents = raw_file.get_scan_dependents(scan, 5)
            if scan_dependents is not None:
                print(f'Scan number {scan} @ time {time} - Instrument type={scan_dependents.raw_file_instrument_type}, Number dependent scans={len(scan_dependents.scan_dependent_detail_array)}')


def get_spectrum(raw_file: RawFileAccess, scan_number: int, output_data: bool):
    """
    Gets the spectrum from the RAW file.
    """
    # Get the scan statistics from the RAW file for this scan number
    scan_statistics = raw_file.get_scan_stats_for_scan_number(scan_number)

    # Check to see if the scan has centroid data or profile data.  Depending upon the
    # type of data, different methods will be used to read the data.  While the ReadAllSpectra
    # method demonstrates reading the data using the Scan.FromFile method, generating the
    # Scan object takes more time and memory to do, so that method isn't optimum.
    if scan_statistics.is_centroid_scan and scan_statistics.spectrum_packet_type == SpectrumPacketType.FtCentroid:
        # Get the centroid (label) data from the RAW file for this scan
        centroid_stream = raw_file.get_centroid_stream(scan_number, False)
        print(f'Spectrum (centroid/label) {scan_number} - {centroid_stream.length} points')

        # Print the spectral data (mass, intensity, charge values).  Not all of the information in the high resolution centroid 
        # (label data) object is reported in this example.  Please check the documentation for more information about what is
        # available in high resolution centroid (label) data.
        if output_data:
            for i in range(centroid_stream.length):
                print(f'  {i} - {centroid_stream.masses[i]}, {centroid_stream.intensities[i]}, {centroid_stream.charges[i]}')
        print('')
    else:
        # Get the segmented (low res and profile) scan data
        segmented_scan = raw_file.get_segmented_scan_from_scan_number(scan_number, scan_statistics)
        print(f'Spectrum (normal data) {scan_number} - {len(segmented_scan.positions)} points')

        # Print the spectral data (mass, intensity values)
        if output_data:
            for i in range(len(segmented_scan.positions)):
                print(f'  {i} - {segmented_scan.positions[i]}, {segmented_scan.intensities[i]}')
        print('')


def get_average_spectrum(raw_file: RawFileAccess, first_scan_number: int, last_scan_number: int, output_data: bool):
    """
    Gets the average spectrum from the RAW file.  
    """
    # Create the mass options object that will be used when averaging the scans
    options = raw_file.default_mass_options()
    options.tolerance_units = ToleranceUnits.ppm
    options.tolerance = 5.0

    # Get the scan filter for the first scan.  This scan filter will be used to located
    # scans within the given scan range of the same type
    scan_filter = raw_file.get_filter_for_scan_number(first_scan_number)

    # Get the average mass spectrum for the provided scan range. In addition to getting the
    # average scan using a scan range, the library also provides a similar method that takes
    # a time range.
    average_scan = raw_file.average_scans_in_scan_range(first_scan_number, last_scan_number, scan_filter, options)

    if average_scan.has_centroid_stream:
        print(f'Average spectrum ({average_scan.centroid_scan.length} points)')

        # Print the spectral data (mass, intensity values)
        if output_data:
            for i in range(average_scan.centroid_scan.length):
                print(f'  {average_scan.centroid_scan.masses[i]} {average_scan.centroid_scan.intensities[i]}')

    # This example uses a different method to get the same average spectrum that was calculated in the
    # previous portion of this method.  Instead of passing the start and end scan, a list of scans will
    # be passed to the GetAveragedMassSpectrum function.
    scans = [1, 6, 7, 9, 11, 12, 14]

    average_scan = raw_file.average_scans(scans, options)

    if average_scan.has_centroid_stream:
        print(f'Average spectrum ({average_scan.centroid_scan.length} points)')
        # Print the spectral data (mass, intensity values)
        if output_data:
            for i in range(average_scan.centroid_scan.length):
                print(f'  {average_scan.centroid_scan.masses[i]} {average_scan.centroid_scan.intensities[i]}')
    print('')


def read_all_spectra(raw_file: RawFileAccess, first_scan_number: int, last_scan_number: int, output_data: bool):
    """
    Read all spectra in the RAW file.
    """
    for scan_number in range(first_scan_number, last_scan_number + 1):
        try:
            # Get the scan filter for the spectrum
            scan_filter = raw_file.get_filter_for_scan_number(scan_number)

            if scan_filter is None or str(scan_filter) == '':
                continue

            # Get the scan from the RAW file.  This method uses the Scan.FromFile method which returns a
            # Scan object that contains both the segmented and centroid (label) data from an FTMS scan
            # or just the segmented data in non-FTMS scans.  The GetSpectrum method demonstrates an
            # alternative method for reading scans.
            scan = Scan.from_file(raw_file, scan_number)

            # If that scan contains FTMS data then Centroid stream will be populated so check to see if it is present.
            label_size = 0
            if scan.has_centroid_stream:
                label_size = scan.centroid_scan.length

            # For non-FTMS data, the preferred data will be populated
            data_size = len(scan.preferred_masses)
            if output_data:
                print(f'Spectrum {scan_number} - {scan_filter}: normal {data_size}, label {label_size} points')

        except Exception as ex:
            print(f'Error reading spectrum {scan_number} - {ex}')


def calculate_mass_precision(raw_file: RawFileAccess, scan_number: int):
    """
    Calculates the mass precision for a spectrum.  
    """
    # Get the scan from the RAW file
    scan = Scan.from_file(raw_file, scan_number)

    # Get the scan event and from the scan event get the analyzer type for this scan
    scan_event = raw_file.get_scan_event_for_scan_number(scan_number)

    # Get the trailer extra data to get the ion time for this file
    log_entry = raw_file.get_trailer_extra_information(scan_number)

    trailer_headings = list()
    trailer_values = list()
    for i in range(log_entry.length):
        trailer_headings.append(log_entry.labels[i])
        trailer_values.append(log_entry.values[i])

    # Create the mass precision estimate object
    precision_estimate = PrecisionEstimate()

    # Get the ion time from the trailer extra data values
    ion_time = precision_estimate.get_ion_time(scan_event.mass_analyzer, scan, trailer_headings, trailer_values)

    # Calculate the mass precision for the scan
    list_results = precision_estimate.get_mass_precision_estimate(scan, scan_event.mass_analyzer, ion_time, raw_file.run_header.mass_resolution)

    # Output the mass precision results
    if len(list_results) > 0:
        print('Mass Precision Results:')
        for result in list_results:
            print(f'Mass {result.mass}, mmu = {result.mass_accuracy_in_mmu}, ppm = {result.mass_accuracy_in_ppm}')


def analyze_all_scans(raw_file: RawFileAccess, first_scan_number: int, last_scan_number: int):
    """
    Reads all of the scans in the RAW and looks for out of order data
    """
    # Test the preferred (normal) data and centroid (high resolution/label) data
    failed_centroid = 0
    failed_preferred = 0

    for scan_number in range(first_scan_number, last_scan_number+1):
        # Get each scan from the RAW file
        scan = Scan.from_file(raw_file, scan_number)

        # Check to see if the RAW file contains label (high-res) data and if it is present
        # then look for any data that is out of order
        if scan.has_centroid_stream:
            if scan.centroid_scan.length:
                current_mass = scan.centroid_scan.masses[0]

                for index in range(1, scan.centroid_scan.length):
                    if scan.centroid_scan.masses[index] > current_mass:
                        current_mass = scan.centroid_scan.masses[index]
                    else:
                        if failed_centroid == 0:
                            print(f'First failure: Failed in scan data at: Scan: {scan_number} Mass: {current_mass}')
                        failed_centroid += 1

        # Check the normal (non-label) data in the RAW file for any out-of-order data
        if len(scan.preferred_masses) > 0:
            current_mass = scan.preferred_masses[0]
            for index in range(1, len(scan.preferred_masses)):
                if scan.preferred_masses[index] > current_mass:
                    current_mass = scan.preferred_masses[index]
                else:
                    if failed_preferred == 0:
                        print(f'First failure: Failed in scan data at: Scan: {scan_number} Mass: {current_mass}')
                    failed_preferred += 1

    # Display a message indicating if any of the scans had data that was "out of order"
    print('')
    if failed_preferred == 0 and failed_centroid == 0:
        print('Analysis completed: No out of order data found')
    else:
        print(f'Analysis completed: Preferred data failed: {failed_preferred} Centroid data failed: {failed_centroid}')


if __name__ == '__main__':
    # This local variables controls if certain operations are performed. Change any of them to true to read and output that
    # information section from the RAW file.
    analyze_scans = True#False
    average_scans = False
    do_calculate_mass_precision = False
    do_get_chromatogram = True
    do_get_inclusion_exclusion_list = True#False
    get_status_log = True
    get_trailer_extra = True
    read_all_scans = True
    do_read_scan_information = False
    read_spectrum = True

    try:
        # Check to see if the RAW file name was supplied as an argument to the program
        filename = 'my_file.raw'

        args = sys.argv[1:]
        if len(args) > 0:
            filename = args[0]

        if filename == '':
            print('No RAW file specified!')
            sys.exit(0)

        # Check to see if the specified RAW file exists
        if not os.path.exists(filename):
            print(f"The file doesn't exist in the specified location - {filename}")
            sys.exit(0)

        # Create the RawFileAccess object for accessing the RAW file
        raw_file = RawFileReaderAdapter.file_factory(filename)

        if not raw_file.is_open or raw_file.is_error:
            print('Unable to access the RAW file using the RawFileReader class!')
            sys.exit(0)

        # Check if the RAW file is being acquired
        if raw_file.in_acquisition:
            print(f'RAW file still being acquired - {filename}')
            sys.exit(0)

        # Get the number of instruments (controllers) present in the RAW file and set the 
        # selected instrument to the MS instrument, first instance of it
        print(f'The RAW file has data from {raw_file.instrument_count} instruments')

        raw_file.select_instrument(Device.MS, 1)

        # Get the first and last scan from the RAW file
        first_scan_number = raw_file.run_header_ex.first_spectrum
        last_scan_number = raw_file.run_header_ex.last_spectrum

        # get the start and end time from the RAW file
        start_time = raw_file.run_header_ex.start_time
        end_time = raw_file.run_header_ex.end_time

        # Get some information from the header portions of the RAW file and display that information.
        # The information is general information pertaining to the RAW file.
        print('General File Information:')
        print(f'   RAW file: {raw_file.file_name}')
        #print(f'   RAW file version: {raw_file.file_header.revision}')
        #print(f'   Creation date: {raw_file.file_header.creation_date}')
        #print(f'   Operator: {raw_file.file_header.who_created_id}')
        print(f'   Number of instruments: {raw_file.instrument_count}')
        #print(f'   Description: {raw_file.file_header.file_description}')
        print(f'   Instrument model: {raw_file.get_instrument_data().model}')
        print(f'   Instrument name: {raw_file.get_instrument_data().name}')
        print(f'   Serial number: {raw_file.get_instrument_data().serial_number}')
        print(f'   Software version: {raw_file.get_instrument_data().software_version}')
        print(f'   Firmware version: {raw_file.get_instrument_data().hardware_version}')
        print(f'   Units: {raw_file.get_instrument_data().units}')
        print(f'   Mass resolution: {raw_file.run_header_ex.mass_resolution}')
        print(f'   Number of scans: {raw_file.run_header_ex.spectra_count}')
        print(f'   Scan range: {first_scan_number} - {last_scan_number}')
        print(f'   Time range: {start_time} - {end_time}')
        print(f'   Mass range: {raw_file.run_header_ex.low_mass} - {raw_file.run_header_ex.high_mass}')
        print('')

        # Get information related to the sample that was processed
        print('Sample Information:')
        print(f'   Sample name: {raw_file.sample_information.sample_name}')
        print(f'   Sample id: {raw_file.sample_information.sample_id}')
        print(f'   Sample type: {raw_file.sample_information.sample_type}')
        print(f'   Sample comment: {raw_file.sample_information.comment}')
        print(f'   Sample vial: {raw_file.sample_information.vial}')
        print(f'   Sample volume: {raw_file.sample_information.sample_volume}')
        print(f'   Sample injection volume: {raw_file.sample_information.injection_volume}')
        print(f'   Sample row number: {raw_file.sample_information.row_number}')
        print(f'   Sample dilution factor: {raw_file.sample_information.dilution_factor}')
        print('')

        # Display all of the trailer extra data fields present in the RAW file
        if get_trailer_extra:
            list_trailer_extra_fields(raw_file)

        # Get the status log items
        if get_status_log:
            list_status_log(raw_file, first_scan_number, last_scan_number)

        # Get the inclusion/exclusion list
        if do_get_inclusion_exclusion_list:
            inclusion_list = get_inclusion_exclusion_list(raw_file, 1e-5)

            # Output the saved inclusion/exclusion list
            count = 0

            for item in inclusion_list:
                print(f'  {count} - {item.descriptor}, {item.mass}, {item.threshold}, {item.scan_number}')
                count += 1
            print('')

        # Get the number of filters present in the RAW file
        number_filters = len(raw_file.get_filters())

        # Get the scan filter for the first and last spectrum in the RAW file
        first_filter = raw_file.get_filter_for_scan_number(first_scan_number)
        last_filter = raw_file.get_filter_for_scan_number(last_scan_number)

        print('Filter Information:')
        print(f'   Scan filter (first scan): {str(first_filter)}')
        print(f'   Scan filter (last scan): {str(last_filter)}')
        print(f'   Total number of filters:{number_filters}')
        print('')

        # Get the BasePeak chromatogram for the MS data
        if do_get_chromatogram:
            get_chromatogram(raw_file, first_scan_number, last_scan_number, True)

        # Read the scan information for each scan in the RAW file
        if do_read_scan_information:
            read_scan_information(raw_file, first_scan_number, last_scan_number, True)

        # Get a spectrum from the RAW file.
        if read_spectrum:
            get_spectrum(raw_file, first_scan_number, False)

        # Get a average spectrum from the RAW file for the first 15 scans in the file.  
        if average_scans:
            get_average_spectrum(raw_file, 1, 15, True)

        # Read each spectrum
        if read_all_scans:
            read_all_spectra(raw_file, first_scan_number, last_scan_number, True)

        # Calculate the mass precision for a spectrum
        if do_calculate_mass_precision:
            calculate_mass_precision(raw_file, 1)

        # Check all of the scans for out of order data.  This method isn't enabled by
        # default because it is very, very time consuming.  If you would like to 
        # call this method change the value of _analyzeScans to true.
        if analyze_scans:
            analyze_all_scans(raw_file, first_scan_number, last_scan_number)

        # Close (dispose) the RAW file
        print('')
        print(f'Closing {filename}')
        raw_file.dispose()        

    except Exception as e:
        print(e)
        print(traceback.print_exc())
        pass
