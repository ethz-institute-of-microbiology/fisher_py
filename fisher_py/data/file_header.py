from fisher_py.net_wrapping import NetWrapperBase
from fisher_py.data import FileType
from fisher_py.utils import datetime_net_to_py, datetime_py_to_net
from datetime import datetime


class FileHeader(NetWrapperBase):
    @property
    def who_created_id(self) -> str:
        """
        Gets or sets the creator Id. The creator Id is the full text user name of the
        user when the file is created.
        """
        return self._get_wrapped_object_().WhoCreatedId

    @who_created_id.setter
    def who_created_id(self, value: str):
        """
        Gets or sets the creator Id. The creator Id is the full text user name of the
        user when the file is created.
        """
        assert type(value) is str
        self._get_wrapped_object_().WhoCreatedId = value

    @property
    def who_created_logon(self) -> str:
        """
        Gets or sets the creator Login name. The creator login name is the user name
        of the user when the file is created, as entered at the "user name, password"
        screen in windows.
        """
        return self._get_wrapped_object_().WhoCreatedLogon

    @who_created_logon.setter
    def who_created_logon(self, value: str):
        """
        Gets or sets the creator Login name. The creator login name is the user name
        of the user when the file is created, as entered at the "user name, password"
        screen in windows.
        """
        assert type(value) is str
        self._get_wrapped_object_().WhoCreatedLogon = value

    @property
    def who_modified_id(self) -> str:
        """
        Gets or sets the creator Id. The creator Id is the full text user name of the
        user when the file is created.
        """
        return self._get_wrapped_object_().WhoModifiedId

    @who_modified_id.setter
    def who_modified_id(self, value: str):
        """
        Gets or sets the creator Id. The creator Id is the full text user name of the
        user when the file is created.
        """
        assert type(value) is str
        self._get_wrapped_object_().WhoModifiedId = value

    @property
    def who_modified_logon(self) -> str:
        """
        Gets or sets the creator Login name. The creator login name is the user name
        of the user when the file is created, as entered at the "user name, password"
        screen in windows.
        """
        return self._get_wrapped_object_().WhoModifiedLogon

    @who_modified_logon.setter
    def who_modified_logon(self, value: str):
        """
        Gets or sets the creator Login name. The creator login name is the user name
        of the user when the file is created, as entered at the "user name, password"
        screen in windows.
        """
        assert type(value) is str
        self._get_wrapped_object_().WhoModifiedLogon = value

    @property
    def file_type(self) -> FileType:
        """
        Gets or sets the type of the file. If the file is not recognized, the value of
        the FileType will be set to "Not Supported"
        """
        return FileType(self._get_wrapped_object_().FileType)

    @file_type.setter
    def file_type(self, value: FileType):
        """
        Gets or sets the type of the file. If the file is not recognized, the value of
        the FileType will be set to "Not Supported"
        """
        assert type(value) is FileType
        self._get_wrapped_object_().FileType = value.value

    @property
    def revision(self) -> int:
        """
        Gets or sets the file format revision Note: this does not refer to revisions
        of the content. It defines revisions of the binary files structure.
        """
        return self._get_wrapped_object_().Revision

    @revision.setter
    def revision(self, value: int):
        """
        Gets or sets the file format revision Note: this does not refer to revisions
        of the content. It defines revisions of the binary files structure.
        """
        assert type(value) is int
        self._get_wrapped_object_().Revision = value

    @property
    def creation_date(self) -> datetime:
        """
        Gets or sets the file creation date.
        """
        return datetime_net_to_py(self._get_wrapped_object_().CreationDate)

    @creation_date.setter
    def creation_date(self, value: datetime):
        """
        Gets or sets the file creation date.
        """
        assert type(value) is datetime
        self._get_wrapped_object_().CreationDate = datetime_py_to_net(value)

    @property
    def modified_date(self) -> datetime:
        """
        Gets or sets the modified date. File changed audit information (most recent change)
        
        Value:
        The modified date.
        """
        return datetime_net_to_py(self._get_wrapped_object_().ModifiedDate)

    @modified_date.setter
    def modified_date(self, value: datetime):
        """
        Gets or sets the modified date. File changed audit information (most recent change)
        
        Value:
        The modified date.
        """
        assert type(value) is datetime
        self._get_wrapped_object_().ModifiedDate = datetime_py_to_net(value)

    @property
    def number_of_times_modified(self) -> int:
        """
        Gets or sets the number of times modified.
        
        Value:
        The number of times the file has been modified.
        """
        return self._get_wrapped_object_().NumberOfTimesModified

    @number_of_times_modified.setter
    def number_of_times_modified(self, value: int):
        """
        Gets or sets the number of times modified.
        
        Value:
        The number of times the file has been modified.
        """
        assert type(value) is int
        self._get_wrapped_object_().NumberOfTimesModified = value

    @property
    def number_of_times_calibrated(self) -> int:
        """
        Gets or sets the number of times calibrated.
        
        Value:
        The number of times calibrated.
        """
        return self._get_wrapped_object_().NumberOfTimesCalibrated

    @number_of_times_calibrated.setter
    def number_of_times_calibrated(self, value: int):
        """
        Gets or sets the number of times calibrated.
        
        Value:
        The number of times calibrated.
        """
        assert type(value) is int
        self._get_wrapped_object_().NumberOfTimesCalibrated = value

    @property
    def file_description(self) -> str:
        """
        Gets or sets the file description. User's narrative description of the file,
        512 unicode characters (1024 bytes)
        
        Value:
        The file description.
        """
        return self._get_wrapped_object_().FileDescription

    @file_description.setter
    def file_description(self, value: str):
        """
        Gets or sets the file description. User's narrative description of the file,
        512 unicode characters (1024 bytes)
        
        Value:
        The file description.
        """
        assert type(value) is str
        self._get_wrapped_object_().FileDescription = value

