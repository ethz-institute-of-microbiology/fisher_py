from fisher_py.net_wrapping import ThermoFisher
from fisher_py.utils import is_number
from fisher_py.data.business import Range, MassOptions

_range_factory = ThermoFisher.CommonCore.Data.Business.RangeFactory


class RangeFactor(object):
    """
    Factory to produce immutable ranges of double
    """

    @staticmethod
    def create(low: float, high: float) -> Range:
        """
        Create an immutable (constant) range from low and high.
        
        Parameters:
          low:
            The low.
        
          high:
            The high.
        
        Returns:
            The range.
        """
        assert is_number(low)
        assert is_number(high)
        return Range._get_wrapper_(_range_factory.Create(float(low), float(high)))

    @staticmethod
    def create_from_center_and_delta(center: float, delta: float) -> Range:
        """
        Create an immutable (constant) range from center and delta, such that the range
        is center +/- delta.
        
        Parameters:
          center:
            The center.
        
          delta:
            The delta.
        
        Returns:
            The ThermoFisher.CommonCore.Data.Business.Range.
        """
        assert is_number(center)
        assert is_number(delta)
        return Range._get_wrapper_(_range_factory.CreateFromCenterAndDelta(float(center), float(delta)))

    @staticmethod
    def create_from_range_and_tolerance(from_: Range, arg) -> Range:
        """
        Construct a range from another range, adding a tolerance if ends are the same
        """
        assert type(from_) is Range

        if type(arg) is MassOptions:
            return Range._get_wrapper_(_range_factory.CreateFromRangeAndTolerance(from_._get_wrapped_object_(), arg._get_wrapped_object_()))
        elif is_number(arg):
            return Range._get_wrapper_(_range_factory.CreateFromRangeAndTolerance(from_._get_wrapped_object_(), float(arg)))
        
        raise ValueError('Unable to create range.')
