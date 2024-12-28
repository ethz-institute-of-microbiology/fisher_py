from fisher_py.utils import is_number
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data.business import Range


class MassToFrequencyConverter(NetWrapperBase):
    """
    Class which includes the coefficients for mass calibration from a particular
    scan, and means to convert between mass and frequency
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.MassToFrequencyConverter

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def coefficient_1(self) -> float:
        """
        Gets or sets the coefficient 1.
        """
        return self._get_wrapped_object_().Coefficient1

    @coefficient_1.setter
    def coefficient_1(self, value: float):
        """
        Gets or sets the coefficient 1.
        """
        assert is_number(value)
        self._get_wrapped_object_().Coefficient1 = float(value)

    @property
    def coefficient_2(self) -> float:
        """
        Gets or sets the coefficient 2.
        """
        return self._get_wrapped_object_().Coefficient2

    @coefficient_2.setter
    def coefficient_2(self, value: float):
        """
        Gets or sets the coefficient 2.
        """
        assert is_number(value)
        self._get_wrapped_object_().Coefficient2 = float(value)

    @property
    def coefficient_3(self) -> float:
        """
        Gets or sets the coefficient 3.
        """
        return self._get_wrapped_object_().Coefficient3

    @coefficient_3.setter
    def coefficient_3(self, value: float):
        """
        Gets or sets the coefficient 3.
        """
        assert is_number(value)
        self._get_wrapped_object_().Coefficient3 = float(value)

    @property
    def base_frequency(self) -> float:
        """
        Gets or sets the base frequency.
        """
        return self._get_wrapped_object_().BaseFrequency

    @base_frequency.setter
    def base_frequency(self, value: float):
        """
        Gets or sets the base frequency.
        """
        assert is_number(value)
        self._get_wrapped_object_().BaseFrequency = float(value)

    @property
    def delta_frequency(self) -> float:
        """
        Gets or sets the delta frequency.
        """
        return self._get_wrapped_object_().DeltaFrequency

    @delta_frequency.setter
    def delta_frequency(self, value: float):
        """
        Gets or sets the delta frequency.
        """
        assert is_number(value)
        self._get_wrapped_object_().DeltaFrequency = float(value)

    @property
    def highest_mass(self) -> float:
        """
        Gets or sets the highest mass.
        """
        return self._get_wrapped_object_().HighestMass

    @highest_mass.setter
    def highest_mass(self, value: float):
        """
        Gets or sets the highest mass.
        """
        assert is_number(value)
        self._get_wrapped_object_().HighestMass = float(value)

    @property
    def segment_range(self) -> Range:
        """
        Gets or sets the (largest) segment range of the scans processed.
        """
        return self._get_wrapped_object_().SegmentRange

    @segment_range.setter
    def segment_range(self, value: Range):
        """
        Gets or sets the (largest) segment range of the scans processed.
        """
        assert is_number(value)
        self._get_wrapped_object_().SegmentRange = float(value)

    def convert_frequence_to_mass(self, sample: int) -> float:
        """
        Converts the given frequency to it's corresponding mass.
        
        Parameters:
        sample:
        sample number to convert
        
        Returns:
        converted mass.
        """
        assert type(sample) is int
        return self._get_wrapped_object().ConvertFrequenceToMass(sample)

    def convert_mass_to_frequency(self, mass: float) -> float:
        """
        Converts the given mass to frequency.
        
        Parameters:
        mass:
        The mass to convert
        
        Returns:
        converted frequency
        """
        assert is_number(mass)
        return self._get_wrapped_object().ConvertMassToFrequency(float(mass))

