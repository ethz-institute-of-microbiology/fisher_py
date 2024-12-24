import pytest
from fisher_py.exceptions import RawFileException
from fisher_py.exceptions.raw_file_exception import NoSelectedDeviceException, NoSelectedMsDeviceException
from fisher_py.raw_file_reader import RawFileAccess
from tests import assert_attributes, path_for


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
    access = RawFileAccess(path_for('ACE_0793-01_MK13.raw'))
    assert access.file_error.has_error == False, 'Import should succeed'

@pytest.mark.parametrize('attribute', ['run_header', 'run_header_ex', 'scan_events', 'status_log_plottable_data'])
def test_access_to_instrument_dependent_attributes_fails_without_instrument_selection(attribute: str):
    access = RawFileAccess(path_for('ACE_0793-01_MK13.raw'))
    try:
        getattr(access, attribute)
        assert False, 'Access should fail'
    except (NoSelectedDeviceException, NoSelectedMsDeviceException):
        pass

@pytest.mark.parametrize('attribute', ['file_header', 'sample_information'])
def test_attribute_available_without_instrument_selection_is_as_expected(attribute: str):
    access = RawFileAccess(path_for('ACE_0793-01_MK13.raw'))
    assert_attributes(access, attribute)

def test_debug():
    from tests import capture_attribute
    access = RawFileAccess(path_for('ACE_0793-01_MK13.raw'))
    capture_attribute(access, 'sample_information')

    