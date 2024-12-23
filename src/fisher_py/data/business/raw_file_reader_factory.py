from fisher_py.data.raw_file_thread_accessor import RawFileThreadAccessor
from fisher_py.net_wrapping import ThermoFisher
from fisher_py.raw_file_reader.raw_file_access import RawFileAccess


class RawFileReaderFactory:

    @staticmethod
    def read_file(filename: str) -> RawFileAccess:
        """        
         Summary:
             Open a raw file for reading.
        
         Parameters:
           fileName:
             Name of file to read
        
         Returns:
             Access to the contents of the file.
        """
        assert type(filename) is str
        return RawFileAccess._get_wrapper_(ThermoFisher.CommonCore.Data.Business.RawFileReaderFactory.ReadFile(filename))

    @staticmethod
    def create_thread_manager(filename: str) -> RawFileThreadAccessor:
        """
         Summary:
             Open a raw file for reading, creating a manager tool, such that multiple threads
             can access the same open file.
        
         Parameters:
           fileName:
             Name of file to read
        
         Returns:
             Access to the contents of the file.
        """
        assert type(filename) is str
        return RawFileThreadAccessor._get_wrapper_(ThermoFisher.CommonCore.Data.Business.RawFileReaderFactory.CreateThreadManager(filename))
