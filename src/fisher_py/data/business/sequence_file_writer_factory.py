from fisher_py.net_wrapping import ThermoFisher
from fisher_py.data.sequence_file_writer import SequenceFileWriter


class SequenceFileWriterFactory(object):
    """
    This static factory class provides methods to create and open existing sequence
    file.
    """
    
    @staticmethod
    def create_sequence_file_writer(file_name: str, open_existing: bool) -> SequenceFileWriter:
        """
        Summary:
            Creates the sequence file writer.
        
        Parameters:
          fileName:
            Name of the file.
        
          openExisting:
            True open an existing sequence file with read/write privilege; false to create
            a new unique sequence file
        
        Returns:
            Sequence file writer object
        """
        assert type(file_name) is str
        assert type(open_existing) is bool
        net_writer = ThermoFisher.CommonCore.Data.Business.SequenceFileWriterFactory.CreateSequenceFileWriter(file_name, open_existing)
        return SequenceFileWriter._get_wrapper_(net_writer)