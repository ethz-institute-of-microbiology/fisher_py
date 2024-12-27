import pytest
from fisher_py.data.device import Device
from fisher_py.exceptions import RawFileException
from fisher_py.exceptions.raw_file_exception import NoSelectedDeviceException, NoSelectedMsDeviceException
from fisher_py.raw_file_reader import RawFileAccess
from tests import assert_attributes, path_for

REFERENCE_RAW_FILE = 'Angiotensin_325-CID.raw'

def test_raw_file_import_fails_for_invalid_path():
    try:
        RawFileAccess('does-not-exist.raw')
        assert False, 'FileNotFoundError should have been thrown'
    except FileNotFoundError:
        pass

def test_raw_file_import_fails_for_invalid_file():
    try:
        RawFileAccess(path_for('invalid.raw'))
        assert False, 'RawFileException should have been thrown'
    except RawFileException:
        pass

def test_raw_file_import_succeeds_with_valid_file():
    access = RawFileAccess(path_for(REFERENCE_RAW_FILE))
    assert access.file_error.has_error == False, 'Import should succeed'

@pytest.mark.parametrize('attribute', ['run_header', 'run_header_ex', 'scan_events', 'status_log_plottable_data'])
def test_access_to_instrument_dependent_attributes_fails_without_instrument_selection(attribute: str):
    access = RawFileAccess(path_for(REFERENCE_RAW_FILE))
    try:
        getattr(access, attribute)
        assert False, 'Access should fail'
    except (NoSelectedDeviceException, NoSelectedMsDeviceException):
        pass

@pytest.mark.parametrize('attribute', ['file_header', 'sample_information'])
def test_attribute_available_without_instrument_selection_is_as_expected(attribute: str):
    access = RawFileAccess(path_for(REFERENCE_RAW_FILE))
    assert_attributes(access, attribute)

def test_device_selection_works():
    access = RawFileAccess(path_for(REFERENCE_RAW_FILE))
    assert access.selected_instrument.device_type == Device.none

    access.select_instrument(Device.MS, 1)
    assert access.selected_instrument.device_type == Device.MS
    assert access.selected_instrument.instrument_index == 1

@pytest.mark.parametrize('attribute', ['run_header', 'run_header_ex'])
def test_instrument_dependent_attribute_matches_expected_data(attribute: str):
    access = RawFileAccess(path_for(REFERENCE_RAW_FILE))
    access.select_instrument(Device.MS, 1)
    assert_attributes(access, attribute)
    