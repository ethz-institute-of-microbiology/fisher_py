from fisher_py.raw_file_reader import RawFileAccess


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
