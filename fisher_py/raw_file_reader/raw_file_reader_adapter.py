from fisher_py.net_wrapping import ThermoFisher
from fisher_py.raw_file_reader import RawFileAccess
from fisher_py.exceptions import RawFileException


_net_raw_file_reader_adapter = ThermoFisher.CommonCore.RawFileReader.RawFileReaderAdapter

class RawFileReaderAdapter(object):
    """
    Utility to load raw files
    """

    @staticmethod
    def file_factory(raw_file: str):
        """
        Create an IRawDataExtended interface to read data from a raw file

        :param raw_file: Path to raw file
        :return: Returns raw file
        """
        return RawFileAccess(raw_file)


if __name__ == '__main__':
    raw_file_path = r"D:\Nextcloud\Shared\MS\data\00_raw\00_corrected_ion_mass\20210407_15mer_bleomycin.raw"
    raw_file = RawFileReaderAdapter.file_factory(raw_file_path)
    print(raw_file)