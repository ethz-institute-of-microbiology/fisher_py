from fisher_py.net_wrapping import NetWrapperBase


class FileError(NetWrapperBase):
    
    @property
    def has_error(self) -> bool:
        """
        Gets a value indicating whether this file has detected an error. If this is false:
        Other error properties in this interface have no meaning. Applications should
        not continue with processing data from any file which indicates an error.
        """
        return self._get_wrapped_object_().HasError

    @property
    def has_warning(self) -> bool:
        """
        Gets a value indicating whether this file has detected a warning. If this is
        false: Other warning properties in this interface have no meaning.
        """
        return self._get_wrapped_object_().HasWarning

    @property
    def error_code(self) -> int:
        """
        Gets the error code number. Typically this is a windows system error number.
        The lowest valid windows error is: 0x00030200 Errors detected within our files
        will have codes below 100.
        """
        return self._get_wrapped_object_().ErrorCode

    @property
    def error_message(self) -> str:
        """
        Gets the error message. For "unknown exceptions" this may include a stack trace.
        """
        return self._get_wrapped_object_().ErrorMessage

    @property
    def warning_message(self) -> str:
        """
        Gets the warning message.
        """
        return self._get_wrapped_object_().WarningMessage

