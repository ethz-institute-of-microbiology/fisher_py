from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data import Device


class InstrumentSelection(NetWrapperBase):
    """
    Defines which instrument is selected in a file.
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.InstrumentSelection

    def __init__(self, instrument_index: int, device_type: Device):
        super().__init__()
        assert type(instrument_index) is int
        assert type(device_type) is Device
        self._wrapped_object = self._wrapped_type(instrument_index, device_type.value)

    @property
    def instrument_index(self) -> int:
        """
        Gets the Stream number (instance of this instrument type). Stream numbers start
        from 1
        """
        return self._get_wrapped_object_().InstrumentIndex

    @property
    def device_type(self) -> Device:
        """
        Gets the Category of instrument
        """
        return Device(self._get_wrapped_object_().DeviceType)