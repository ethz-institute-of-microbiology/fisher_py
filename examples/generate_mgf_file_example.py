"""
A Python example program showing how to use RAWFileReader. More information on the RAWFileReader methods used
in this example and the other methods available in RAWFileReader can be found in the RAWFileReader user
documentation, that is installed with the RAWFileReader software.

The code of this example is based on the following GitHub repository: https://github.com/compomics/ThermoRawFileParser
It was added to provide users a way of doing what ThermoRawFileParser does in Python.
"""

from typing import List, Union

from numpy import float64
from fisher_py.data import Device
from fisher_py.data import ScanEvent
from fisher_py.data.filter_enums import MsOrderType, PolarityType, ScanDataType
from fisher_py.raw_file_reader import RawFileReaderAdapter
from fisher_py.data.business import Scan, Reaction, LogEntry
import os
import re


## Configuration (Use this section to select the input file and the output folder as well as setting other parameters)
RAW_FILE_PATH = r"my_file.raw"
OUTPUT_FOLDER = r"output_folder"
MS_LEVEL = { MsOrderType.Ms2 }
DISABLE_NATIVE_PEAK_SEARCHING = True
INCLUDE_REF_AND_EX_DATA = True
#--

# Constants
PROGRESS_STEP = 10
ZERO_DELTA = 0.0001
PRECURSOR_MZ_DELTA = 0.0001
DEFAULT_ISOLATION_WINDOW_LOWER_OFFSET = 1.5
DEFAULT_ISOLATION_WINDOW_UPPER_OFFSET = 2.5
FILTER_STRING_ISOLATION_MZ_PATTERN = 'ms2 (.*?)@'
_isolation_mz_to_precursor_scan_number_mapping = dict()
_precursor_ms1_scan_number = 0
_last_scan_progress = 0


def construct_spectrum_title(instrument_type: int, instrument_number: int, scan_number: int) -> str:
    return f'controllerType={instrument_type} controllerNumber={instrument_number} scan={scan_number}'


def construct_precursor_reference(ms_order: MsOrderType, scan_number: int, scan_event: ScanEvent) -> str:
    global _isolation_mz_to_precursor_scan_number_mapping, _precursor_ms1_scan_number
    
    if ms_order == MsOrderType.Ms2:
        # Keep track of the MS2 scan number and isolation m/z for precursor reference
        result = re.match(str(scan_event), FILTER_STRING_ISOLATION_MZ_PATTERN) 
        if result:
            res = result.groups()[0]
            if res in _isolation_mz_to_precursor_scan_number_mapping:
                del _isolation_mz_to_precursor_scan_number_mapping[res]
            _isolation_mz_to_precursor_scan_number_mapping[res] = scan_number
            
        precursor_reference = construct_spectrum_title(Device.MS.value, 1, _precursor_ms1_scan_number)
    
    elif ms_order == MsOrderType.Ms3:
        precursor_scan_number = next(filter(lambda isolation_mz: isolation_mz in str(scan_event),  _isolation_mz_to_precursor_scan_number_mapping.keys()), None)
        if precursor_scan_number:
            precursor_reference = construct_precursor_reference(Device.MS.value, 1, _isolation_mz_to_precursor_scan_number_mapping[precursor_scan_number])
        else:
            raise ValueError(f"Couldn't find a MS2 precursor scan for MS3 scan {scan_event}")
        
    return precursor_reference


def get_reaction(scan_event: ScanEvent, scan_number: int) -> Reaction:
    try:
        order = scan_event.ms_order.value
        return scan_event.get_reaction(order - 2)
    except:
        print(f'No reaction found for scan {scan_number}')
        return None
    
    
class ScanTrailer(object):
    
    @property
    def length(self) -> int:
        return len(self._data)
    
    @property
    def labels(self) -> List[str]:
        return list(self._data.keys())
    
    @property
    def values(self) -> List[str]:
        return list(self._data.values())
    
    def as_bool(self, key: str) -> Union[bool, None]:
        if key in self._data:
            str_value = self._data[key].lower()
            
            if str_value in { 'on', 'true', 'yes' }:
                return True
            return False
        return None
    
    def as_double(self, key: str) -> float64:
        if key in self._data:
            try:
                return float64(self._data[key])
            except:
                pass
        return None
    
    def as_int(self, key: str) -> int:
        if key in self._data:
            try:
                return int(self._data[key])
            except:
                pass
        return None
    
    def as_positive_int(self, key: str) -> int:
        if key in self._data:
            try:
                result = int(self._data[key])
                return result if result >= 0 else None
            except:
                pass
        return None 
    
    def as_string(self, key: str) -> str:
        return self.get(key)
    
    def get(self, key: str) -> str:
        if key in self._data:
            try:
                return self._data[key]
            except:
                pass
        return None
    
    def has(self, key: str) -> bool:
        return key in self._data
    
    def __init__(self, trailer_data: LogEntry):
        self._data = {trailer_data.labels[i]: trailer_data.values[i] for i in range(trailer_data.length)}


def calculate_selected_ion_mz(reaction: Reaction, monoisotopic_mz: float64, isolation_width: float64) -> float64:
    selected_ion_mz = reaction.precursor_mass
    
    # take the isolation width from the reaction if no value was found in the trailer data
    if isolation_width is None or isolation_width < ZERO_DELTA:
        isolation_width = reaction.isolation_width
        
    isolation_width *= 0.5
    
    if monoisotopic_mz and monoisotopic_mz > ZERO_DELTA and abs(reaction.precursor_mass - monoisotopic_mz) > PRECURSOR_MZ_DELTA:
        selected_ion_mz = monoisotopic_mz
        
        # check if the monoisotopic mass lies in the precursor mass isolation window
        # otherwise take the precursor mass
        if isolation_width <= 2:
            if (selected_ion_mz < (reaction.precursor_mass - DEFAULT_ISOLATION_WINDOW_LOWER_OFFSET * 2)) or (selected_ion_mz > (reaction.precursor_mass + DEFAULT_ISOLATION_WINDOW_UPPER_OFFSET)):
                selected_ion_mz = reaction.precursor_mass
        elif (selected_ion_mz < (reaction.precursor_mass - isolation_width)) or (selected_ion_mz > (reaction.precursor_mass + isolation_width)):
            selected_ion_mz = reaction.precursor_mass
            
    return selected_ion_mz


if __name__ == '__main__':
    raw_file = RawFileReaderAdapter.file_factory(RAW_FILE_PATH)
    raw_file.select_instrument(Device.MS, 1)
    raw_file.include_reference_and_exception_data = INCLUDE_REF_AND_EX_DATA
    
    file_name = os.path.splitext(os.path.split(RAW_FILE_PATH)[-1])[0]
    OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, f'{file_name}.mgf')

    # Get the first and last scan from the RAW file
    first_scan_number = raw_file.run_header_ex.first_spectrum
    last_scan_number = raw_file.run_header_ex.last_spectrum
    
    
    with open(OUTPUT_FILE, 'w') as mgf_file:
        for scan_number in range(first_scan_number, last_scan_number + 1):
            
            # report progress
            scan_progress = int(scan_number / (last_scan_number - first_scan_number + 1) * 100)
            if scan_progress % PROGRESS_STEP == 0:
                if scan_progress != _last_scan_progress:
                    print(f'{scan_progress} %')
                    _last_scan_progress = scan_progress
            
            # Get the scan from the RAW file
            scan: Scan = Scan.from_file(raw_file, scan_number)

            # Get the retention time
            retention_time = raw_file.retention_time_from_scan_number(scan_number)

            # Get the scan filter for this scan number
            scan_filter = raw_file.get_filter_for_scan_number(scan_number)
            
            # Get the scan event for this scan number
            scan_event = raw_file.get_scan_event_for_scan_number(scan_number)
            
            # Don't include MS1 spectra
            if scan_filter.ms_order in MS_LEVEL:
                reaction = get_reaction(scan_event, scan_number)
                
                mgf_file.write(f'BEGIN IONS\n')
                mgf_file.write(f'TITLE={construct_spectrum_title(Device.MS.value, 1, scan_number)}\n')
                
                mgf_file.write(f'SCANS={scan_number}\n')
                mgf_file.write(f'RTINSECONDS={(retention_time * 60)}\n')
                
                # Trailer extra data list
                trailer_data = ScanTrailer(raw_file.get_trailer_extra_information(scan_number))
                charge = trailer_data.as_positive_int('Charge State:')
                monoisotopic_mz = trailer_data.as_double('Monoisotopic M/Z:')
                isolation_width = trailer_data.as_double(f'MS{scan_filter.ms_order.value} Isolation Width:')
                
                if reaction:
                    selected_ion_mz = calculate_selected_ion_mz(reaction, monoisotopic_mz, isolation_width)
                    mgf_file.write(f'PEPMASS={selected_ion_mz}\n')
                    
                # Charge
                if charge:
                    # Scan polarity
                    polarity = '+' if scan_filter.polarity == PolarityType.Positive else '-'
                    mgf_file.write(f'CHARGE={charge}{polarity}\n')
                
                if not DISABLE_NATIVE_PEAK_SEARCHING:
                    # Check if the scan has a centroid stream
                    if scan.has_centroid_stream:
                        masses = scan.centroid_scan.masses
                        intensities = scan.centroid_scan.intensities
                    else:    # Otherwise take segmented (low res) scan data
                        segmented_scan = Scan.to_centroid(scan) if scan_event.scan_data == ScanDataType.Profile else scan.segmented_scan
                        masses = segmented_scan.positions
                        intensities = segmented_scan.intensities
                else:    # Use the segmented data as is
                    masses = scan.segmented_scan.positions
                    intensities = scan.segmented_scan.intensities
                    
                if masses and len(masses):
                    masses, intensities = [l for l in zip(*sorted(zip(masses, intensities)))]                    
                    
                    for i in range(len(masses)):
                        mgf_file.write(f'{masses[i]:.5f} {intensities[i]:.3f}\n')
                        
                    mgf_file.write('END IONS\n')
                    
