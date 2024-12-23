from __future__ import annotations
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data import ToleranceUnits
from fisher_py.utils import is_number


class MassOptions(NetWrapperBase):
    """
    Contains the options for displaying and calculating the masses.
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.MassOptions

    def __init__(self, *args):
        super().__init__()

        if len(args) == 0:
            self._wrapped_object = self._wrapped_type()
        elif len(args) == 1:
            arg = args[0]
            if type(arg) is MassOptions:
                self._wrapped_object = self._wrapped_type(arg._get_wrapped_object())
            elif is_number(arg):
                self._wrapped_object = self._wrapped_type(float(arg))
            else:
                raise ValueError('Unable to create mass options.')                
        elif len(args) == 2:
            tolerance, tolerance_units = args
            assert is_number(tolerance)
            assert type(tolerance_units) is ToleranceUnits
            self._wrapped_object = self._wrapped_type(float(tolerance), tolerance_units.value)
        elif len(args) == 3:
            tolerance, tolerance_units, precision = args
            assert is_number(tolerance)
            assert type(tolerance_units) is ToleranceUnits
            assert type(precision) is int
            self._wrapped_object = self._wrapped_type(float(tolerance), tolerance_units.value, precision)
        else:
            raise ValueError('Unable to create mass options.')

    @property
    def tolerance(self) -> float:
        """
        Gets or sets the tolerance value.
        
        Value:
        The tolerance.
        """
        return self._get_wrapped_object_().Tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        """
        Gets or sets the tolerance value.
        
        Value:
        The tolerance.
        """
        assert type(value) is float
        self._get_wrapped_object_().Tolerance = value

    @property
    def precision(self) -> int:
        """
        Gets or sets the precision (decimal places).
        """
        return self._get_wrapped_object_().Precision

    @precision.setter
    def precision(self, value: int):
        """
        Gets or sets the precision (decimal places).
        """
        assert type(value) is int
        self._get_wrapped_object_().Precision = value

    @property
    def tolerance_units(self) -> ToleranceUnits:
        """
        Gets or sets the tolerance units.
        """
        return ToleranceUnits(self._get_wrapped_object_().ToleranceUnits)

    @tolerance_units.setter
    def tolerance_units(self, value: ToleranceUnits):
        """
        Gets or sets the tolerance units.
        """
        assert type(value) is ToleranceUnits
        self._get_wrapped_object_().ToleranceUnits = value.value

    @property
    def tolerance_string(self) -> str:
        """
        Gets the tolerance string of the current toleranceUnits setting.
        """
        return self._get_wrapped_object_().ToleranceString

    def get_tolerance_string(tolerance_units: ToleranceUnits) -> str:
        """
        Gets the tolerance string from the enumeration strings resource.
        
        Parameters:
        toleranceUnits:
        The tolerance units.
        
        Returns:
        The tolerance units as a string.
        """
        return MassOptions._wrapped_type.GetToleranceString(tolerance_units.value)

    def clone(self) -> MassOptions:
        """
        Implementation of ICloneable.Clone method. Creates deep copy of this instance.
        
        Returns:
        An exact copy of the current object.
        """
        return MassOptions._get_wrapper_(self._get_wrapped_object().Clone())

    def get_tolerance_at_mass(self, mass: float) -> float:
        """
        Get the tolerance window around a specific mass
        
        Parameters:
        mass:
        Mass about which window is needed
        
        Returns:
        The distance (in amu) from the mass which is within tolerance. For example: myWindow=GetToleranceAtMass(myMass);
        accept data between "myMass-myWindow" and "myMass+myWindow"
        """
        return self._get_wrapped_object().GetToleranceAtMass(mass)    
