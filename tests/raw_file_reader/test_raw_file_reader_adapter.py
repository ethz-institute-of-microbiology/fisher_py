
from fisher_py.raw_file_reader.raw_file_reader_adapter import RawFileReaderAdapter
from tests import path_for


def test_raw_file_adapter_can_load_file():
    file = RawFileReaderAdapter.file_factory(path_for('Angiotensin_325-CID.raw'))