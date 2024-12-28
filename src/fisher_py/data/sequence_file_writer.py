from fisher_py.net_wrapping import NetWrapperBase
from fisher_py.data import FileHeader, FileError, SequenceInfo
from fisher_py.data.business import SampleInformation, BracketType
from typing import List


class SequenceFileWriter(NetWrapperBase):
    
    def __init__(self):
        super().__init__()
        self._file_header = None
        self._file_error = None
        self._sequence_info = None

    @property
    def file_header(self) -> FileHeader:
        """
        Gets the file header for the sequence
        """
        if self._file_header is None:
            self._file_header = FileHeader._get_wrapper_(self._get_wrapped_object_().FileHeader)

        return self._file_header

    @property
    def file_error(self) -> FileError:
        """
        Gets the file error state.
        """
        if self._file_error is None:
            self._file_error = FileError._get_wrapper_(self._get_wrapped_object_().FileError)

        return self._file_error

    @property
    def is_error(self) -> bool:
        """
        Gets a value indicating whether the last file operation caused an error
        """
        return self._get_wrapped_object_().IsError

    @property
    def info(self) -> SequenceInfo:
        """
        Gets or sets additional information about a sequence
        """
        if self._sequence_info is None:
            self._sequence_info = SequenceInfo._get_wrapper_(self._get_wrapped_object_().Info)
        return self._sequence_info

    @info.setter
    def info(self, value: SequenceInfo):
        """
        Gets or sets additional information about a sequence
        """
        assert type(value) is SequenceInfo
        self._sequence_info = value
        self._get_wrapped_object_().Info = value._get_wrapped_object_()

    @property
    def samples(self) -> List[SampleInformation]:
        """
        Gets the set of samples in the sequence
        """
        return [SampleInformation._get_wrapper_(s) for s in self._get_wrapped_object_().Samples]

    @property
    def file_name(self) -> str:
        """
        Gets the name of the sequence file.
        """
        return self._get_wrapped_object_().FileName

    @property
    def bracket(self) -> BracketType:
        """
        Gets or sets the sequence bracket type. This determines which groups of samples
        use the same calibration curve.
        """
        return BracketType(self._get_wrapped_object_().Bracket)

    @bracket.setter
    def bracket(self, value: BracketType):
        """
        Gets or sets the sequence bracket type. This determines which groups of samples
        use the same calibration curve.
        """
        assert type(value) is BracketType
        self._get_wrapped_object_().Bracket = value.value

    @property
    def tray_configuration(self) -> str:
        """
        Gets or sets a description of the auto-sampler tray
        """
        return self._get_wrapped_object_().TrayConfiguration

    @tray_configuration.setter
    def tray_configuration(self, value: str):
        """
        Gets or sets a description of the auto-sampler tray
        """
        assert type(value) is str
        self._get_wrapped_object_().TrayConfiguration = value

    def get_user_column_label(self, index: int) -> str:
        """
        Retrieves the user label at given 0-based label index.
        
        Parameters:
        index:
        Index of user label to be retrieved
        
        Returns:
        String containing the user label at given index
        
        Remarks:
        SampleInformation.MaxUserTextColumnCount determines the maximum number of user
        column labels.
        """
        return self._get_wrapped_object_().GetUserColumnLabel(index)

    def save(self) -> bool:
        """
        Saves Sequence data to disk.
        
        Returns:
        True saved data to disk; false otherwise.
        """
        return self._get_wrapped_object_().Save()

    def set_user_column_label(self, index: int, label: str) -> bool:
        """
        Sets the user label at given 0-based label index.
        
        Parameters:
        index:
        Index of user label to be set
        
        label:
        New string value for user label to be set
        
        Returns:
        true if successful; false otherwise
        
        Remarks:
        SampleInformation.MaxUserTextColumnCount determines the maximum number of user
        column labels.
        """
        return self._get_wrapped_object_().SetUserColumnLabel(index, label)

