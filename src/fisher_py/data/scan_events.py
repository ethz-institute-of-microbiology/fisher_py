from fisher_py.data.scan_event import ScanEvent
from fisher_py.net_wrapping import NetWrapperBase


class ScanEvents(NetWrapperBase):
    """
    The ScanEvents interface.
    """

    @property
    def segments(self) -> int:
        """Gets the number segments."""
        return self._get_wrapped_object_().Segments
    
    @property
    def scan_events(self) -> int:
        """Gets the total number of scan events, in all segments"""
        return self._get_wrapped_object_().ScanEvents
    
    def get_event_by_segment(self, segment: int, event_number: int) -> ScanEvent:
        """Get an event, indexed by the segment and event numbers (zero based).

        Args:
            segment (int): The segment.
            event_number (int): The event number.

        Returns:
            ScanEvent: The event.
        """
        assert type(event_number) is int
        assert type(segment) is int
            
        net_type = self._get_wrapped_object_().GetEvent(segment, event_number)
            
        return ScanEvent._get_wrapper_(net_type)
    
    def get_event(self, event_number: int) -> ScanEvent:
        """Get an event, using indexed event number (zero based). This gets events from
        all segments in order, use "ScanEvents" to get the total count of events.

        Args:
            event_number (int): The event number.

        Returns:
            ScanEvent: The event.
        """
        assert type(event_number) is int
            
        net_type = self._get_wrapped_object_().GetEvent(event_number)
            
        return ScanEvent._get_wrapper_(net_type)
    
    def get_event_count(self, segment: int) -> int:
        """Gets the number of events in a specific segment (0 based)

        Args:
            segment (int): The segment number

        Returns:
            int: The number of events in this segment
        """
        assert type(segment) is int
        self._get_wrapped_object_().GetEventCount(segment)
