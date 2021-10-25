from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data import ToleranceUnits


class RunHeader(NetWrapperBase):
    """
    The run header.
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.RunHeader

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def first_spectrum(self) -> int:
        """
        Gets or sets the number for the first scan in this stream (usually 1)
        """
        return self._get_wrapped_object_().FirstSpectrum

    @first_spectrum.setter
    def first_spectrum(self, value: int):
        """
        Gets or sets the number for the first scan in this stream (usually 1)
        """
        assert type(value) is int
        self._get_wrapped_object_().FirstSpectrum = value

    @property
    def last_spectrum(self) -> int:
        """
        Gets or sets the number for the last scan in this stream
        """
        return self._get_wrapped_object_().LastSpectrum

    @last_spectrum.setter
    def last_spectrum(self, value: int):
        """
        Gets or sets the number for the last scan in this stream
        """
        assert type(value) is int
        self._get_wrapped_object_().LastSpectrum = value

    @property
    def start_time(self) -> float:
        """
        Gets or sets the time of first scan in file
        """
        return self._get_wrapped_object_().StartTime

    @start_time.setter
    def start_time(self, value: float):
        """
        Gets or sets the time of first scan in file
        """
        assert type(value) is float
        self._get_wrapped_object_().StartTime = value

    @property
    def end_time(self) -> float:
        """
        Gets or sets the time of last scan in file
        """
        return self._get_wrapped_object_().EndTime

    @end_time.setter
    def end_time(self, value: float):
        """
        Gets or sets the time of last scan in file
        """
        assert type(value) is float
        self._get_wrapped_object_().EndTime = value

    @property
    def low_mass(self) -> float:
        """
        Gets or sets the lowest recorded mass in file
        """
        return self._get_wrapped_object_().LowMass

    @low_mass.setter
    def low_mass(self, value: float):
        """
        Gets or sets the lowest recorded mass in file
        """
        assert type(value) is float
        self._get_wrapped_object_().LowMass = value

    @property
    def high_mass(self) -> float:
        """
        Gets or sets the highest recorded mass in file
        """
        return self._get_wrapped_object_().HighMass

    @high_mass.setter
    def high_mass(self, value: float):
        """
        Gets or sets the highest recorded mass in file
        """
        assert type(value) is float
        self._get_wrapped_object_().HighMass = value

    @property
    def mass_resolution(self) -> float:
        """
        Gets or sets the mass resolution value recorded for the current instrument. The
        value is returned as one half of the mass resolution. For example, a unit resolution
        controller would return a value of 0.5.
        """
        return self._get_wrapped_object_().MassResolution

    @mass_resolution.setter
    def mass_resolution(self, value: float):
        """
        Gets or sets the mass resolution value recorded for the current instrument. The
        value is returned as one half of the mass resolution. For example, a unit resolution
        controller would return a value of 0.5.
        """
        assert type(value) is float
        self._get_wrapped_object_().MassResolution = value

    @property
    def expected_runtime(self) -> float:
        """
        Gets or sets the expected acquisition run time for the current instrument.
        """
        return self._get_wrapped_object_().ExpectedRuntime

    @expected_runtime.setter
    def expected_runtime(self, value: float):
        """
        Gets or sets the expected acquisition run time for the current instrument.
        """
        assert type(value) is float
        self._get_wrapped_object_().ExpectedRuntime = value

    @property
    def max_integrated_intensity(self) -> float:
        """
        Gets or sets the max integrated intensity.
        """
        return self._get_wrapped_object_().MaxIntegratedIntensity

    @max_integrated_intensity.setter
    def max_integrated_intensity(self, value: float):
        """
        Gets or sets the max integrated intensity.
        """
        assert type(value) is float
        self._get_wrapped_object_().MaxIntegratedIntensity = value

    @property
    def max_intensity(self) -> int:
        """
        Gets or sets the max intensity.
        """
        return self._get_wrapped_object_().MaxIntensity

    @max_intensity.setter
    def max_intensity(self, value: int):
        """
        Gets or sets the max intensity.
        """
        assert type(value) is int
        self._get_wrapped_object_().MaxIntensity = value

    @property
    def tolerance_unit(self) -> ToleranceUnits:
        """
        Gets or sets the tolerance unit.
        """
        return ToleranceUnits(self._get_wrapped_object_().ToleranceUnit)

    @tolerance_unit.setter
    def tolerance_unit(self, value: ToleranceUnits):
        """
        Gets or sets the tolerance unit.
        """
        assert type(value) is ToleranceUnits
        self._get_wrapped_object_().ToleranceUnit = value.value
