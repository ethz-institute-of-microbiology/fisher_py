from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data import PeakOptions


class LabelPeak(NetWrapperBase):

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.LabelPeak

    def __init__(self):
        super().__init__()
        self._mass_options = None

    @property
    def mass(self) -> float:
        """
        Gets or sets mass.
        """
        return self._get_wrapped_object_().Mass

    @mass.setter
    def mass(self, value: float):
        """
        Gets or sets mass.
        """
        assert type(value) is float
        self._get_wrapped_object_().Mass = value

    @property
    def intensity(self) -> float:
        """
        Gets or sets intensity.
        """
        return self._get_wrapped_object_().Intensity

    @intensity.setter
    def intensity(self, value: float):
        """
        Gets or sets intensity.
        """
        assert type(value) is float
        self._get_wrapped_object_().Intensity = value

    @property
    def resolution(self) -> float:
        """
        Gets or sets resolution.
        """
        return self._get_wrapped_object_().Resolution

    @resolution.setter
    def resolution(self, value: float):
        """
        Gets or sets resolution.
        """
        assert type(value) is float
        self._get_wrapped_object_().Resolution = value

    @property
    def baseline(self) -> float:
        """
        Gets or sets base Line.
        """
        return self._get_wrapped_object_().Baseline

    @baseline.setter
    def baseline(self, value: float):
        """
        Gets or sets base Line.
        """
        assert type(value) is float
        self._get_wrapped_object_().Baseline = value

    @property
    def noise(self) -> float:
        """
        Gets or sets noise.
        """
        return self._get_wrapped_object_().Noise

    @noise.setter
    def noise(self, value: float):
        """
        Gets or sets noise.
        """
        assert type(value) is float
        self._get_wrapped_object_().Noise = value

    @property
    def charge(self) -> float:
        """
        Gets or sets charge.
        """
        return self._get_wrapped_object_().Charge

    @charge.setter
    def charge(self, value: float):
        """
        Gets or sets charge.
        """
        assert type(value) is float
        self._get_wrapped_object_().Charge = value

    @property
    def flag(self) -> PeakOptions:
        """
        Gets or sets Peak Options Flag.
        """
        return PeakOptions(self._get_wrapped_object_().Flag)

    @flag.setter
    def flag(self, value: PeakOptions):
        """
        Gets or sets Peak Options Flag.
        """
        assert type(value) is PeakOptions
        self._get_wrapped_object_().Flag = value.value

    @property
    def signal_to_noise(self) -> float:
        """
        Gets or sets the signal to noise.
        """
        return self._get_wrapped_object_().SignalToNoise

    @signal_to_noise.setter
    def signal_to_noise(self, value: float):
        """
        Gets or sets the signal to noise.
        """
        assert type(value) is float
        self._get_wrapped_object_().SignalToNoise = value
