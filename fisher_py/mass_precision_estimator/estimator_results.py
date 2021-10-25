from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.utils import is_number


class EstimatorResults(NetWrapperBase):
    """
    Class to hold mass precision estimator results for individual mass/intensity
    points in a scan.
    """

    _wrapped_type = ThermoFisher.CommonCore.MassPrecisionEstimator.EstimatorResults

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_object()

    @property
    def intensity(self) -> float:
        """
        Gets or sets the intensity value
        """
        return self._get_wrapped_object_().Intensity

    @intensity.setter
    def intensity(self, value: float):
        """
        Gets or sets the intensity value
        """
        assert type(value) is float
        self._get_wrapped_object_().Intensity = value

    @property
    def mass(self) -> float:
        """
        Gets or sets the mass value
        """
        return self._get_wrapped_object_().Mass

    @mass.setter
    def mass(self, value: float):
        """
        Gets or sets the mass value
        """
        assert is_number(value)
        self._get_wrapped_object_().Mass = float(value)

    @property
    def mass_accuracy_in_mmu(self) -> float:
        """
        Gets or sets the mass accuracy in MMU value
        """
        return self._get_wrapped_object_().MassAccuracyInMmu

    @mass_accuracy_in_mmu.setter
    def mass_accuracy_in_mmu(self, value: float):
        """
        Gets or sets the mass accuracy in MMU value
        """
        assert is_number(value)
        self._get_wrapped_object_().MassAccuracyInMmu = float(value)

    @property
    def mass_accuracy_in_ppm(self) -> float:
        """
        Gets or sets the mass accuracy in PPM value
        """
        return self._get_wrapped_object_().MassAccuracyInPpm

    @mass_accuracy_in_ppm.setter
    def mass_accuracy_in_ppm(self, value: float):
        """
        Gets or sets the mass accuracy in PPM value
        """
        assert is_number(value)
        self._get_wrapped_object_().MassAccuracyInPpm = float(value)

    @property
    def resolution(self) -> float:
        """
        Gets or sets the resolution value
        """
        return self._get_wrapped_object_().Resolution

    @resolution.setter
    def resolution(self, value: float):
        """
        Gets or sets the resolution value
        """
        assert is_number(value)
        self._get_wrapped_object_().Resolution = float(value)
