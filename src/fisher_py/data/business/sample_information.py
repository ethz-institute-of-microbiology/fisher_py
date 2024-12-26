from __future__ import annotations
from typing import List
from fisher_py.net_wrapping import ThermoFisher
from fisher_py.data import CommonCoreDataObject
from fisher_py.data.business import SampleType, BarcodeStatusType
from fisher_py.net_wrapping.wrapped_net_array import WrappedNetArray
from fisher_py.utils import to_net_array, to_net_list


class SampleInformation(CommonCoreDataObject):
    """
    Encapsulates various information about sample.
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.SampleInformation

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()
        self._user_text = None

    max_user_text_column_count = 20

    @property
    def sample_volume(self) -> float:
        """
        Gets or sets the sample volume of this sequence row.
        """
        return self._get_wrapped_object_().SampleVolume

    @sample_volume.setter
    def sample_volume(self, value: float):
        """
        Gets or sets the sample volume of this sequence row.
        """
        assert type(value) is float
        self._get_wrapped_object_().SampleVolume = value

    @property
    def sample_type(self) -> SampleType:
        """
        Gets or sets the type of the sample.
        """
        return SampleType(self._get_wrapped_object_().SampleType)

    @sample_type.setter
    def sample_type(self, value: SampleType):
        """
        Gets or sets the type of the sample.
        """
        assert type(value) is SampleType
        self._get_wrapped_object_().SampleType = value.value

    @property
    def processing_method_file(self) -> str:
        """
        Gets or sets the processing method filename of this sequence row.
        """
        return self._get_wrapped_object_().ProcessingMethodFile

    @processing_method_file.setter
    def processing_method_file(self, value: str):
        """
        Gets or sets the processing method filename of this sequence row.
        """
        assert type(value) is str
        self._get_wrapped_object_().ProcessingMethodFile = value

    @property
    def path(self) -> str:
        """
        Gets or sets the path to original data.
        """
        return self._get_wrapped_object_().Path

    @path.setter
    def path(self, value: str):
        """
        Gets or sets the path to original data.
        """
        assert type(value) is str
        self._get_wrapped_object_().Path = value

    @property
    def row_number(self) -> int:
        """
        Gets or sets the row number.
        """
        return self._get_wrapped_object_().RowNumber

    @row_number.setter
    def row_number(self, value: int):
        """
        Gets or sets the row number.
        """
        assert type(value) is int
        self._get_wrapped_object_().RowNumber = value

    @property
    def istd_amount(self) -> float:
        """
        Gets or sets the ISTD amount of this sequence row.
        """
        return self._get_wrapped_object_().IstdAmount

    @istd_amount.setter
    def istd_amount(self, value: float):
        """
        Gets or sets the ISTD amount of this sequence row.
        """
        assert type(value) is float
        self._get_wrapped_object_().IstdAmount = value

    @property
    def calibration_file(self) -> str:
        """
        Gets or sets the name of calibration file.
        """
        return self._get_wrapped_object_().CalibrationFile

    @calibration_file.setter
    def calibration_file(self, value: str):
        """
        Gets or sets the name of calibration file.
        """
        assert type(value) is str
        self._get_wrapped_object_().CalibrationFile = value

    @property
    def raw_file_name(self) -> str:
        """
        Gets or sets the name of acquired file (excluding path).
        """
        return self._get_wrapped_object_().RawFileName

    @raw_file_name.setter
    def raw_file_name(self, value: str):
        """
        Gets or sets the name of acquired file (excluding path).
        """
        assert type(value) is str
        self._get_wrapped_object_().RawFileName = value

    @property
    def instrument_method_file(self) -> str:
        """
        Gets or sets the instrument method filename of this sequence row.
        """
        return self._get_wrapped_object_().InstrumentMethodFile

    @instrument_method_file.setter
    def instrument_method_file(self, value: str):
        """
        Gets or sets the instrument method filename of this sequence row.
        """
        assert type(value) is str
        self._get_wrapped_object_().InstrumentMethodFile = value

    @property
    def dilution_factor(self) -> float:
        """
        Gets or sets the bulk dilution factor (volume correction) of this sequence row.
        """
        return self._get_wrapped_object_().DilutionFactor

    @dilution_factor.setter
    def dilution_factor(self, value: float):
        """
        Gets or sets the bulk dilution factor (volume correction) of this sequence row.
        """
        assert type(value) is float
        self._get_wrapped_object_().DilutionFactor = value

    @property
    def calibration_level(self) -> str:
        """
        Gets or sets a name to identify the Calibration or QC level associated with this
        sample. Empty if this sample does not contain any calibration compound.
        """
        return self._get_wrapped_object_().CalibrationLevel

    @calibration_level.setter
    def calibration_level(self, value: str):
        """
        Gets or sets a name to identify the Calibration or QC level associated with this
        sample. Empty if this sample does not contain any calibration compound.
        """
        assert type(value) is str
        self._get_wrapped_object_().CalibrationLevel = value

    @property
    def barcode_status(self) -> BarcodeStatusType:
        """
        Gets or sets the bar code status.
        """
        return BarcodeStatusType(self._get_wrapped_object_().BarcodeStatus)

    @barcode_status.setter
    def barcode_status(self, value: BarcodeStatusType):
        """
        Gets or sets the bar code status.
        """
        assert type(value) is BarcodeStatusType
        self._get_wrapped_object_().BarcodeStatus = value.value

    @property
    def barcode(self) -> str:
        """
        Gets or sets bar code from scanner (if attached).
        """
        return self._get_wrapped_object_().Barcode

    @barcode.setter
    def barcode(self, value: str):
        """
        Gets or sets bar code from scanner (if attached).
        """
        assert type(value) is str
        self._get_wrapped_object_().Barcode = value

    @property
    def injection_volume(self) -> float:
        """
        Gets or sets the amount of sample injected.
        """
        return self._get_wrapped_object_().InjectionVolume

    @injection_volume.setter
    def injection_volume(self, value: float):
        """
        Gets or sets the amount of sample injected.
        """
        assert type(value) is float
        self._get_wrapped_object_().InjectionVolume = value

    @property
    def vial(self) -> str:
        """
        Gets or sets the vial or well form auto sampler.
        """
        return self._get_wrapped_object_().Vial

    @vial.setter
    def vial(self, value: str):
        """
        Gets or sets the vial or well form auto sampler.
        """
        assert type(value) is str
        self._get_wrapped_object_().Vial = value

    @property
    def sample_name(self) -> str:
        """
        Gets or sets the description of sample.
        """
        return self._get_wrapped_object_().SampleName

    @sample_name.setter
    def sample_name(self, value: str):
        """
        Gets or sets the description of sample.
        """
        assert type(value) is str
        self._get_wrapped_object_().SampleName = value

    @property
    def sample_id(self) -> str:
        """
        Gets or sets the Code to identify sample.
        """
        return self._get_wrapped_object_().SampleId

    @sample_id.setter
    def sample_id(self, value: str):
        """
        Gets or sets the Code to identify sample.
        """
        assert type(value) is str
        self._get_wrapped_object_().SampleId = value

    @property
    def comment(self) -> str:
        """
        Gets or sets the comment about sample (from user).
        """
        return self._get_wrapped_object_().Comment

    @comment.setter
    def comment(self, value: str):
        """
        Gets or sets the comment about sample (from user).
        """
        assert type(value) is str
        self._get_wrapped_object_().Comment = value

    @property
    def sample_weight(self) -> float:
        """
        Gets or sets the sample weight of this sequence row.
        """
        return self._get_wrapped_object_().SampleWeight

    @sample_weight.setter
    def sample_weight(self, value: float):
        """
        Gets or sets the sample weight of this sequence row.
        """
        assert type(value) is float
        self._get_wrapped_object_().SampleWeight = value

    @property
    def user_text(self) -> List[str]:
        """
        Gets or sets the collection of user text.
        """
        if self._user_text is None:
            self._user_text = WrappedNetArray[str](self._get_wrapped_object_().UserText)        
        return self._user_text

    @user_text.setter
    def user_text(self, value: List[str]):
        """
        Gets or sets the collection of user text.
        """
        assert type(value) is list
        value = to_net_array(value, str)
        self._get_wrapped_object_().UserText = value

    def deep_copy(self) -> SampleInformation:
        """
        Create a deep copy of the current object.
        
        Returns:
        A deep copy of the current object.
        """
        return SampleInformation._get_wrapper_(self._get_wrapped_object().DeepCopy())
