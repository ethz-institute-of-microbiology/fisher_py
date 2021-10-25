from __future__ import annotations
from typing import Any
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data.business import MassOptions
from fisher_py.utils import is_number


class Range(NetWrapperBase):

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.Range

    def __init__(self, *args):
        super().__init__()

        if len(args) == 0:
            self._wrapped_object = self._wrapped_type()
        elif len(args) == 1:
            from_ = args[0]
            assert type(from_) is Range
            self._wrapped_object = self._wrapped_type(from_._wrapped_object)
        elif len(args) == 2:
            arg1, arg2 = args
            if is_number(arg1) and is_number(arg2):
                self._wrapped_object = self._wrapped_type(float(arg1), float(arg2))
            elif type(arg1) is Range and is_number(arg2):
                self._wrapped_object = self._wrapped_type(arg1._wrapped_object, float(arg2))
            elif type(arg1) is Range and type(arg2) is MassOptions:
                self._wrapped_object = self._wrapped_type(arg1._wrapped_object, arg2._wrapped_object)
    
    @property
    def low(self) -> float:
        """
        Gets or sets the low end of range
        """
        return self._get_wrapped_object_().Low

    @low.setter
    def low(self, value: float):
        """
        Gets or sets the low end of range
        """
        assert type(value) is float
        self._get_wrapped_object_().Low = value

    @property
    def high(self) -> float:
        """
        Gets or sets the high end of range
        """
        return self._get_wrapped_object_().High

    @high.setter
    def high(self, value: float):
        """
        Gets or sets the high end of range
        """
        assert type(value) is float
        self._get_wrapped_object_().High = value

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
        return Range._get_wrapper_(Range._wrapped_type.Create(float(low), float(high)))

    def create_from_cetner_and_delta(center: float, delta: float) -> Range:
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
        return Range._get_wrapper_(Range._wrapped_type.CreateFromCenterAndDelta(float(center), float(delta)))

    def compare_to(self, other: Range) -> int:
        """
        Compares the current object with another object of the same type.
        
        Parameters:
        other:
        An object to compare with this object.
        
        Returns:
        A 32-bit signed integer that indicates the relative order of the objects being
        compared. The return value has the following meanings: Value Meaning Less than
        zero This object is less than the other parameter. Zero This object is equal
        to other. Greater than zero This object is greater than other.
        """
        return self._get_wrapped_object().CompareTo(other._get_wrapped_object_())

    def equals(self, obj: object) -> bool:
        """
        Indicates whether this instance and a specified object are equal.
        
        Parameters:
        obj:
        Another object to compare to.
        
        Returns:
        true if obj and this instance are the same type and represent the same value;
        otherwise, false.
        """
        return self._get_wrapped_object().Equals(obj)

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        Returns:
        A 32-bit signed integer that is the hash code for this instance.
        """
        return self._get_wrapped_object().GetHashCode()

    def includes(self, value: float) -> bool:
        """
        Test for inclusion.
        
        Parameters:
        value:
        The value.
        
        Returns:
        True if in range
        """
        assert is_number(value)
        return self._get_wrapped_object().Includes(float(value))

    def __eq__(self, o: Range) -> bool:
        return self._get_wrapped_object_() == o._get_wrapped_object_()

    def __ne__(self, o: Range) -> bool:
        return not self == o
