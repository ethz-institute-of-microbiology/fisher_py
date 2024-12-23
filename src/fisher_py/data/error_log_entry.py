from fisher_py.net_wrapping import NetWrapperBase


class ErrorLogEntry(NetWrapperBase):
    """
    The ErrorLogEntry interface.
    """
    
    @property
    def retention_time(self) -> float:
        """Gets the retention time."""
        return self._get_wrapped_object_().RetentionTime
    
    @property
    def message(self) -> str:
        """Gets the error message."""
        return self._get_wrapped_object_().Message
