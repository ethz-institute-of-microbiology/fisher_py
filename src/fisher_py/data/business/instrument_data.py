from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data.business import DataUnits
from fisher_py.utils import to_net_list
from typing import List


class InstrumentData(NetWrapperBase):

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.InstrumentData

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def name(self) -> str:
        """
        Gets or sets the name of the instrument
        """
        return self._get_wrapped_object_().Name

    @name.setter
    def name(self, value: str):
        """
        Gets or sets the name of the instrument
        """
        assert type(value) is str
        self._get_wrapped_object_().Name = value

    @property
    def model(self) -> str:
        """
        Gets or sets the model of instrument
        """
        return self._get_wrapped_object_().Model

    @model.setter
    def model(self, value: str):
        """
        Gets or sets the model of instrument
        """
        assert type(value) is str
        self._get_wrapped_object_().Model = value

    @property
    def serial_number(self) -> str:
        """
        Gets or sets the serial number of instrument
        """
        return self._get_wrapped_object_().SerialNumber

    @serial_number.setter
    def serial_number(self, value: str):
        """
        Gets or sets the serial number of instrument
        """
        assert type(value) is str
        self._get_wrapped_object_().SerialNumber = value

    @property
    def software_version(self) -> str:
        """
        Gets or sets the software version of instrument
        """
        return self._get_wrapped_object_().SoftwareVersion

    @software_version.setter
    def software_version(self, value: str):
        """
        Gets or sets the software version of instrument
        """
        assert type(value) is str
        self._get_wrapped_object_().SoftwareVersion = value

    @property
    def hardware_version(self) -> str:
        """
        Gets or sets the hardware version of instrument
        """
        return self._get_wrapped_object_().HardwareVersion

    @hardware_version.setter
    def hardware_version(self, value: str):
        """
        Gets or sets the hardware version of instrument
        """
        assert type(value) is str
        self._get_wrapped_object_().HardwareVersion = value

    @property
    def channel_labels(self) -> List[str]:
        """
        Gets or sets the Names for the channels, for UV or analog data:
        """
        return self._get_wrapped_object_().ChannelLabels

    @channel_labels.setter
    def channel_labels(self, value: List[str]):
        """
        Gets or sets the Names for the channels, for UV or analog data:
        """
        assert type(value) is list
        value = to_net_list(value, str)
        self._get_wrapped_object_().ChannelLabels = value

    @property
    def units(self) -> DataUnits:
        """
        Gets or sets the units of the Signal, for UV or analog
        """
        return DataUnits(self._get_wrapped_object_().Units)

    @units.setter
    def units(self, value: DataUnits):
        """
        Gets or sets the units of the Signal, for UV or analog
        """
        assert type(value) is DataUnits
        self._get_wrapped_object_().Units = value.value

    @property
    def flags(self) -> str:
        """
        Gets or sets additional information about this instrument.
        """
        return self._get_wrapped_object_().Flags

    @flags.setter
    def flags(self, value: str):
        """
        Gets or sets additional information about this instrument.
        """
        assert type(value) is str
        self._get_wrapped_object_().Flags = value

    @property
    def axis_label_x(self) -> str:
        """
        Gets or sets Device suggested label of X axis
        """
        return self._get_wrapped_object_().AxisLabelX

    @axis_label_x.setter
    def axis_label_x(self, value: str):
        """
        Gets or sets Device suggested label of X axis
        """
        assert type(value) is str
        self._get_wrapped_object_().AxisLabelX = value

    @property
    def axis_label_y(self) -> str:
        """
        Gets or sets Device suggested label of Y axis (name for units of data, such as
        "�C")
        """
        return self._get_wrapped_object_().AxisLabelY

    @axis_label_y.setter
    def axis_label_y(self, value: str):
        """
        Gets or sets Device suggested label of Y axis
        """
        assert type(value) is str
        self._get_wrapped_object_().AxisLabelY = value

    @property
    def is_valid(self) -> bool:
        """
        Gets or sets a value indicating whether the instrument is valid.
        """
        return self._get_wrapped_object_().IsValid

    @is_valid.setter
    def is_valid(self, value: bool):
        """
        Gets or sets a value indicating whether the instrument is valid.
        """
        assert type(value) is bool
        self._get_wrapped_object_().IsValid = value

    @property
    def has_accurate_mass_precursors(self) -> bool:
        """
        Gets a value indicating whether this file has accurate mass precursors
        """
        return self._get_wrapped_object_().HasAccurateMassPrecursors

    def clone(self) -> object:
        """
        Creates a new object that is a copy of the current instance.
        
        Returns:
        A new object that is a copy of this instance.
        """
        return self._get_wrapped_object().Clone()

    def is_tsq_quantum_file(self) -> bool:
        """
        Test if this is a TSQ quantum series file. Such files may have more accurate
        precursor mass selection.
        
        Returns:
        True if this is a raw file from a TSQ Quantum
        """
        return self._get_wrapped_object().IsTsqQuantumFile()
