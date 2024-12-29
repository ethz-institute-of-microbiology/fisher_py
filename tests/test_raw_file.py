
from fisher_py.exceptions.raw_file_exception import RawFileException
from fisher_py.raw_file import RawFile
from tests import path_for

TEST_FILE = 'Angiotensin_325-CID.raw'
PRECURSOR_MZ = 325
TOLERANCE = 1e-6
TIMES = [0.00213759, 0.00539962, 0.00867493, 0.01190376, 0.01514103, 0.0183659 , 0.02165696, 0.02493226, 0.02813163, 0.0314831]

def test_raw_file_initialization_fails_on_nonexisting_path():
    try:
        RawFile('non-existent.raw')
        assert False, 'Expected error when trying to load nonexistent file'
    except FileNotFoundError:
        pass

def test_raw_file_initialization_fails_on_invalid_file():
    try:
        RawFile(path_for('invalid.raw'))
        assert False, 'Expected error when trying to load invalid file'
    except RawFileException:
        pass

def test_raw_file_initialization_succeeds_on_valid_file():
    RawFile(path_for(TEST_FILE))

def test_raw_file_number_of_scans_matches_expected_value():
    file = RawFile(path_for(TEST_FILE))
    assert file.number_of_scans == 10

def test_raw_file_first_scan_matches_expected_value():
    file = RawFile(path_for(TEST_FILE))
    assert file.first_scan == 1

def test_raw_file_last_scan_matches_expected_value():
    file = RawFile(path_for(TEST_FILE))
    assert file.last_scan == 10

def test_raw_file_total_time_min_matches_expected_value():
    file = RawFile(path_for(TEST_FILE))
    assert abs(file.total_time_min - 0.031483095733333334) < TOLERANCE

def test_raw_file_ms2_filter_masses_matches_expected_value():
    file = RawFile(path_for(TEST_FILE))
    assert len(file.ms2_filter_masses) == 1
    assert abs(file.ms2_filter_masses[0] - PRECURSOR_MZ) < TOLERANCE

def test_raw_file_chromatogram_can_be_retrieved():
    file = RawFile(path_for(TEST_FILE))
    t, c = file.get_chromatogram(PRECURSOR_MZ, TOLERANCE)
    assert len(t) == 0
    assert len(c) == 0

def test_raw_file_tic_ms2_can_be_retrieved():
    file = RawFile(path_for(TEST_FILE))
    times, total_ion_current = file.get_tic_ms2(PRECURSOR_MZ, TOLERANCE)

    expected_ion_currents = [37451832.53613281, 37663065.91699219, 45855594.28125, 30816050.90820312, 41055303.14746094, 34280428.34375, 35895350.90429688, 33482430.11523438, 36745244.81738281, 35045496.85644531]
    for t_actual, t_expected, tic_actual, tic_expected in zip(times, TIMES, total_ion_current, expected_ion_currents):
        assert abs(t_actual - t_expected) < TOLERANCE
        assert abs(tic_actual - tic_expected) < TOLERANCE

def test_raw_file_scan_ms2_can_be_retrieved():
    file = RawFile(path_for(TEST_FILE))
    lenths = [175, 199, 163, 150, 142, 186, 174, 114, 203]

    for rt, l in zip(TIMES, lenths):
        masses, charges, intensities, _ = file.get_scan_ms2(rt)
        assert len(masses) == l
        assert len(charges) == l
        assert len(intensities) == l

def test_raw_file_getting_scan_from_number_works_as_expected():
    file = RawFile(path_for(TEST_FILE))
    lenths = [175, 199, 163, 150, 142, 186, 174, 114, 203]

    for i, l in zip(range(1, 11), lenths):
        masses, charges, intensities, _ = file.get_scan_from_scan_number(i)
        assert len(masses) == l
        assert len(charges) == l
        assert len(intensities) == l

def test_raw_file_getting_scan_number_from_retention_time_works_as_expected():
    file = RawFile(path_for(TEST_FILE))

    for i, rt in enumerate(TIMES[:-1]):
        sn = file.get_scan_number_from_retention_time(rt)
        assert sn == i + 1

def test_raw_file_ms2_getting_scan_number_from_retention_time_works_as_expected():
    file = RawFile(path_for(TEST_FILE))

    for i, rt in enumerate(TIMES[:-1]):
        sn, _ = file.get_ms2_scan_number_from_retention_time(rt)
        assert sn == i + 1

def test_raw_file_get_scan_event_str_from_scan_number_works_as_expected():
    file = RawFile(path_for(TEST_FILE))
    desc = file.get_scan_event_str_from_scan_number(1)
    assert desc == 'FTMS + p ESI Full ms2 325.0000@cid35.00 [150.0000-2000.0000]'