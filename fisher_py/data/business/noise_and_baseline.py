from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.utils import is_number


class NoiseAndBaseline(NetWrapperBase):
    """
    Defines noise and baseline at a given mass (Part of support for reading orbitrap data)
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.NoiseAndBaseline

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def mass(self) -> float:
        """
        Gets or sets the mass.
        """
        return self._get_wrapped_object_().Mass

    @mass.setter
    def mass(self, value: float):
        """
        Gets or sets the mass.
        """
        assert is_number(value)
        self._get_wrapped_object_().Mass = float(value)

    @property
    def noise(self) -> float:
        """
        Gets or sets the noise.
        """
        return self._get_wrapped_object_().Noise

    @noise.setter
    def noise(self, value: float):
        """
        Gets or sets the noise.
        """
        assert is_number(value)
        self._get_wrapped_object_().Noise = float(value)

    @property
    def baseline(self) -> float:
        """
        Gets or sets the baseline.
        """
        return self._get_wrapped_object_().Baseline

    @baseline.setter
    def baseline(self, value: float):
        """
        Gets or sets the baseline.
        """
        assert is_number(value)
        self._get_wrapped_object_().Baseline = float(value)

