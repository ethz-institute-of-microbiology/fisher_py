from typing import List
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.utils import is_number, to_net_list
from fisher_py.data.filter_enums import (
    SectorScanType, FieldFreeRegionType, TriState, CompensationVoltageType, ScanDataType, 
    PolarityType, SourceFragmentationValueType, ScanModeType, MassAnalyzerType, DetectorType,
    IonizationModeType, MsOrderType
)
from fisher_py.data import FilterAccurateMass, SourceFragmentationInfoValidType


class ScanFilter(NetWrapperBase):
    """
    The ScanFilter interface defines a set of rules for selecting scans. For example:
    Testing if a scan should be included in a chromatogram. Many if the rules include
    an "Any" choice, which implies that this rule will not be tested. Testing logic
    is included in the class ThermoFisher.CommonCore.Data.Business.ScanFilterHelper
    The class ThermoFisher.CommonCore.Data.Extensions contains methods related to
    filters, the filter helper and raw data.
    """

    def __init__(self, scan_filter_net):
        super().__init__()
        self._wrapped_object = scan_filter_net

    @property
    def sector_scan(self) -> SectorScanType:
        """
        Gets or sets the sector scan filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.SectorScanType for possible values
        """
        return SectorScanType(self._get_wrapped_object_().SectorScan)

    @sector_scan.setter
    def sector_scan(self, value: SectorScanType):
        """
        Gets or sets the sector scan filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.SectorScanType for possible values
        """
        assert type(value) is SectorScanType
        self._get_wrapped_object_().SectorScan = value.value

    @property
    def field_free_region(self) -> FieldFreeRegionType:
        """
        Gets or sets the field free region filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.FieldFreeRegionType for possible
        values
        """
        return FieldFreeRegionType(self._get_wrapped_object_().FieldFreeRegion)

    @field_free_region.setter
    def field_free_region(self, value: FieldFreeRegionType):
        """
        Gets or sets the field free region filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.FieldFreeRegionType for possible
        values
        """
        assert type(value) is FieldFreeRegionType
        self._get_wrapped_object_().FieldFreeRegion = value.value

    @property
    def ultra(self) -> TriState:
        """
        Gets or sets the ultra scan filtering rule.
        """
        return TriState(self._get_wrapped_object_().Ultra)

    @ultra.setter
    def ultra(self, value: TriState):
        """
        Gets or sets the ultra scan filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().Ultra = value.value

    @property
    def enhanced(self) -> TriState:
        """
        Gets or sets the enhanced scan filtering rule.
        """
        return TriState(self._get_wrapped_object_().Enhanced)

    @enhanced.setter
    def enhanced(self, value: TriState):
        """
        Gets or sets the enhanced scan filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().Enhanced = value.value

    @property
    def multiple_photon_dissociation(self) -> TriState:
        """
        Gets or sets the multi-photon dissociation filtering rule.
        """
        return TriState(self._get_wrapped_object_().MultiplePhotonDissociation)

    @multiple_photon_dissociation.setter
    def multiple_photon_dissociation(self, value: TriState):
        """
        Gets or sets the multi-photon dissociation filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().MultiplePhotonDissociation = value.value

    @property
    def multiple_photon_dissociation_value(self) -> float:
        """
        Gets or sets the multi-photon dissociation value.
        
        Value:
        Floating point multi-photon dissociation value
        """
        return self._get_wrapped_object_().MultiplePhotonDissociationValue

    @multiple_photon_dissociation_value.setter
    def multiple_photon_dissociation_value(self, value: float):
        """
        Gets or sets the multi-photon dissociation value.
        
        Value:
        Floating point multi-photon dissociation value
        """
        assert is_number(value)
        self._get_wrapped_object_().MultiplePhotonDissociationValue = float(value)

    @property
    def electron_capture_dissociation(self) -> TriState:
        """
        Gets or sets the electron capture dissociation filtering rule.
        """
        return TriState(self._get_wrapped_object_().ElectronCaptureDissociation)

    @electron_capture_dissociation.setter
    def electron_capture_dissociation(self, value: TriState):
        """
        Gets or sets the electron capture dissociation filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().ElectronCaptureDissociation = value.value

    @property
    def electron_capture_dissociation_value(self) -> float:
        """
        Gets or sets the electron capture dissociation value.
        
        Value:
        Floating point electron capture dissociation value
        """
        return self._get_wrapped_object_().ElectronCaptureDissociationValue

    @electron_capture_dissociation_value.setter
    def electron_capture_dissociation_value(self, value: float):
        """
        Gets or sets the electron capture dissociation value.
        
        Value:
        Floating point electron capture dissociation value
        """
        assert is_number(value)
        self._get_wrapped_object_().ElectronCaptureDissociationValue = float(value)

    @property
    def photo_ionization(self) -> TriState:
        """
        Gets or sets the photo ionization filtering rule.
        """
        return TriState(self._get_wrapped_object_().PhotoIonization)

    @photo_ionization.setter
    def photo_ionization(self, value: TriState):
        """
        Gets or sets the photo ionization filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().PhotoIonization = value.value

    @property
    def pulsed_q_dissociation(self) -> TriState:
        """
        Gets or sets pulsed dissociation filtering rule.
        """
        return TriState(self._get_wrapped_object_().PulsedQDissociation)

    @pulsed_q_dissociation.setter
    def pulsed_q_dissociation(self, value: TriState):
        """
        Gets or sets pulsed dissociation filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().PulsedQDissociation = value.value

    @property
    def pulsed_q_dissociation_value(self) -> float:
        """
        Gets or sets the pulsed dissociation value. Only applies when the PulsedQDissociation
        rule is used.
        
        Value:
        Floating point pulsed dissociation value
        """
        return self._get_wrapped_object_().PulsedQDissociationValue

    @pulsed_q_dissociation_value.setter
    def pulsed_q_dissociation_value(self, value: float):
        """
        Gets or sets the pulsed dissociation value. Only applies when the PulsedQDissociation
        rule is used.
        
        Value:
        Floating point pulsed dissociation value
        """
        assert is_number(value)
        self._get_wrapped_object_().PulsedQDissociationValue = float(value)

    @property
    def electron_transfer_dissociation(self) -> TriState:
        """
        Gets or sets the electron transfer dissociation filtering rule.
        """
        return TriState(self._get_wrapped_object_().ElectronTransferDissociation)

    @electron_transfer_dissociation.setter
    def electron_transfer_dissociation(self, value: TriState):
        """
        Gets or sets the electron transfer dissociation filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().ElectronTransferDissociation = value.value

    @property
    def lock(self) -> TriState:
        """
        Gets or sets the lock scan filtering rule.
        """
        return TriState(self._get_wrapped_object_().Lock)

    @lock.setter
    def lock(self, value: TriState):
        """
        Gets or sets the lock scan filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().Lock = value.value

    @property
    def electron_transfer_dissociation_value(self) -> float:
        """
        Gets or sets the electron transfer dissociation value. Only used when the "ElectronTransferDissociation"
        rule is used.
        
        Value:
        Floating point electron transfer dissociation value
        """
        return self._get_wrapped_object_().ElectronTransferDissociationValue

    @electron_transfer_dissociation_value.setter
    def electron_transfer_dissociation_value(self, value: float):
        """
        Gets or sets the electron transfer dissociation value. Only used when the "ElectronTransferDissociation"
        rule is used.
        
        Value:
        Floating point electron transfer dissociation value
        """
        assert is_number(value)
        self._get_wrapped_object_().ElectronTransferDissociationValue = float(value)

    @property
    def higher_energy_ci_d_value(self) -> float:
        """
        Gets or sets the higher energy CID value. Only applies when the "HigherEnergyCiD"
        rule is used.
        """
        return self._get_wrapped_object_().HigherEnergyCiDValue

    @higher_energy_ci_d_value.setter
    def higher_energy_ci_d_value(self, value: float):
        """
        Gets or sets the higher energy CID value. Only applies when the "HigherEnergyCiD"
        rule is used.
        """
        assert is_number(value)
        self._get_wrapped_object_().HigherEnergyCiDValue = float(value)

    @property
    def multiplex(self) -> TriState:
        """
        Gets or sets the Multiplex type filtering rule.
        """
        return TriState(self._get_wrapped_object_().Multiplex)

    @multiplex.setter
    def multiplex(self, value: TriState):
        """
        Gets or sets the Multiplex type filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().Multiplex = value.value

    @property
    def param_a(self) -> TriState:
        """
        Gets or sets the parameter a filtering rule..
        """
        return TriState(self._get_wrapped_object_().ParamA)

    @param_a.setter
    def param_a(self, value: TriState):
        """
        Gets or sets the parameter a filtering rule..
        """
        assert type(value) is TriState
        self._get_wrapped_object_().ParamA = value.value

    @property
    def param_b(self) -> TriState:
        """
        Gets or sets the parameter b filtering rule..
        """
        return TriState(self._get_wrapped_object_().ParamB)

    @param_b.setter
    def param_b(self, value: TriState):
        """
        Gets or sets the parameter b filtering rule..
        """
        assert type(value) is TriState
        self._get_wrapped_object_().ParamB = value.value

    @property
    def param_f(self) -> TriState:
        """
        Gets or sets the parameter f filtering rule..
        """
        return TriState(self._get_wrapped_object_().ParamF)

    @param_f.setter
    def param_f(self, value: TriState):
        """
        Gets or sets the parameter f filtering rule..
        """
        assert type(value) is TriState
        self._get_wrapped_object_().ParamF = value.value

    @property
    def multi_notch(self) -> TriState:
        """
        Gets or sets the SPS (Synchronous Precursor Selection) Multi notch filtering
        rule.
        """
        return TriState(self._get_wrapped_object_().MultiNotch)

    @multi_notch.setter
    def multi_notch(self, value: TriState):
        """
        Gets or sets the SPS (Synchronous Precursor Selection) Multi notch filtering
        rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().MultiNotch = value.value

    @property
    def param_r(self) -> TriState:
        """
        Gets or sets the parameter r filtering rule..
        """
        return TriState(self._get_wrapped_object_().ParamR)

    @param_r.setter
    def param_r(self, value: TriState):
        """
        Gets or sets the parameter r filtering rule..
        """
        assert type(value) is TriState
        self._get_wrapped_object_().ParamR = value.value

    @property
    def param_v(self) -> TriState:
        """
        Gets or sets the parameter v filtering rule..
        """
        return TriState(self._get_wrapped_object_().ParamV)

    @param_v.setter
    def param_v(self, value: TriState):
        """
        Gets or sets the parameter v filtering rule..
        """
        assert type(value) is TriState
        self._get_wrapped_object_().ParamV = value.value

    @property
    def name(self) -> str:
        """
        Gets or sets the event Name. Used for "compound name" filtering.
        """
        return self._get_wrapped_object_().Name

    @name.setter
    def name(self, value: str):
        """
        Gets or sets the event Name. Used for "compound name" filtering.
        """
        assert type(value) is str
        self._get_wrapped_object_().Name = value

    @property
    def supplemental_activation(self) -> TriState:
        """
        Gets or sets supplemental activation type filter rule.
        """
        return TriState(self._get_wrapped_object_().SupplementalActivation)

    @supplemental_activation.setter
    def supplemental_activation(self, value: TriState):
        """
        Gets or sets supplemental activation type filter rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().SupplementalActivation = value.value

    @property
    def multi_state_activation(self) -> TriState:
        """
        Gets or sets MultiStateActivation type filtering rule.
        """
        return TriState(self._get_wrapped_object_().MultiStateActivation)

    @multi_state_activation.setter
    def multi_state_activation(self, value: TriState):
        """
        Gets or sets MultiStateActivation type filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().MultiStateActivation = value.value

    @property
    def higher_energy_ci_d(self) -> TriState:
        """
        Gets or sets the higher energy CID filtering rule.
        """
        return TriState(self._get_wrapped_object_().HigherEnergyCiD)

    @higher_energy_ci_d.setter
    def higher_energy_ci_d(self, value: TriState):
        """
        Gets or sets the higher energy CID filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().HigherEnergyCiD = value.value

    @property
    def compensation_voltage(self) -> TriState:
        """
        Gets or sets Compensation Voltage filtering rule.
        """
        return TriState(self._get_wrapped_object_().CompensationVoltage)

    @compensation_voltage.setter
    def compensation_voltage(self, value: TriState):
        """
        Gets or sets Compensation Voltage filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().CompensationVoltage = value.value

    @property
    def compensation_volt_type(self) -> CompensationVoltageType:
        """
        Gets or sets Compensation Voltage type filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.CompensationVoltageType for possible
        values
        """
        return CompensationVoltageType(self._get_wrapped_object_().CompensationVoltType)

    @compensation_volt_type.setter
    def compensation_volt_type(self, value: CompensationVoltageType):
        """
        Gets or sets Compensation Voltage type filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.CompensationVoltageType for possible
        values
        """
        assert type(value) is CompensationVoltageType
        self._get_wrapped_object_().CompensationVoltType = value.value

    @property
    def detector_value(self) -> float:
        """
        Gets or sets the detector value. This is used for filtering when the Detector
        filter is enabled.
        
        Value:
        Floating point detector value
        """
        return self._get_wrapped_object_().DetectorValue

    @detector_value.setter
    def detector_value(self, value: float):
        """
        Gets or sets the detector value. This is used for filtering when the Detector
        filter is enabled.
        
        Value:
        Floating point detector value
        """
        assert is_number(value)
        self._get_wrapped_object_().DetectorValue = float(value)

    @property
    def accurate_mass(self) -> FilterAccurateMass:
        """
        Gets the accurate mass filter rule.
        """
        return FilterAccurateMass(self._get_wrapped_object_().AccurateMass)

    @property
    def mass_precision(self) -> int:
        """
        Gets or sets the mass precision, which is used to format the filter (in ToString).
        """
        return self._get_wrapped_object_().MassPrecision

    @mass_precision.setter
    def mass_precision(self, value: int):
        """
        Gets or sets the mass precision, which is used to format the filter (in ToString).
        """
        assert type(value) is int
        self._get_wrapped_object_().MassPrecision = value

    @property
    def meta_filters(self) -> int:
        """
        Gets or sets additional instrument defined filters (these are bit flags). See
        enum MetaFilterType.
        """
        return self._get_wrapped_object_().MetaFilters

    @meta_filters.setter
    def meta_filters(self, value: int):
        """
        Gets or sets additional instrument defined filters (these are bit flags). See
        enum MetaFilterType.
        """
        assert type(value) is int
        self._get_wrapped_object_().MetaFilters = value

    @property
    def unique_mass_count(self) -> int:
        """
        Gets the number of unique masses, taking into account multiple activations. For
        example: If this is MS3 data, there are two "parent masses", but they may have
        multiple reactions applied. If the first stage has two reactions, then there
        are a total of 3 reactions, for the 2 "unique masses"
        """
        return self._get_wrapped_object_().UniqueMassCount

    @property
    def source_fragmentation_info_valid(self) -> List[SourceFragmentationInfoValidType]:
        """
        Gets or sets an array of values which determines if the source fragmentation
        values are valid.
        """
        return [SourceFragmentationInfoValidType(i) for i in self._get_wrapped_object_().SourceFragmentationInfoValid]

    @source_fragmentation_info_valid.setter
    def source_fragmentation_info_valid(self, value: List[SourceFragmentationInfoValidType]):
        """
        Gets or sets an array of values which determines if the source fragmentation
        values are valid.
        """
        assert type(value) is list
        value = to_net_list([i._get_wrapped_object_() for i in value], type(value[0]._get_wrapped_object_()))
        self._get_wrapped_object_().SourceFragmentationInfoValid = value

    @property
    def locale_name(self) -> str:
        """
        Gets or sets the locale name. This can be used to affect string conversion.
        """
        return self._get_wrapped_object_().LocaleName

    @locale_name.setter
    def locale_name(self, value: str):
        """
        Gets or sets the locale name. This can be used to affect string conversion.
        """
        assert type(value) is str
        self._get_wrapped_object_().LocaleName = value

    @property
    def compensation_voltage_count(self) -> int:
        """
        Gets the number of compensation voltage values. This is the number of values
        related to cv mode. 1 for "single value", 2 for "ramp" and 1 per mass range for
        "SIM".
        """
        return self._get_wrapped_object_().CompensationVoltageCount

    @property
    def wideband(self) -> TriState:
        """
        Gets or sets the wideband filtering rule.
        """
        return TriState(self._get_wrapped_object_().Wideband)

    @wideband.setter
    def wideband(self, value: TriState):
        """
        Gets or sets the wideband filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().Wideband = value.value

    @property
    def scan_data(self) -> ScanDataType:
        """
        Gets or sets the scan data type (centroid or profile) filtering rule.
        """
        return ScanDataType(self._get_wrapped_object_().ScanData)

    @scan_data.setter
    def scan_data(self, value: ScanDataType):
        """
        Gets or sets the scan data type (centroid or profile) filtering rule.
        """
        assert type(value) is ScanDataType
        self._get_wrapped_object_().ScanData = value.value

    @property
    def polarity(self) -> PolarityType:
        """
        Gets or sets the polarity (+/-) filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.PolarityType for possible values
        """
        return PolarityType(self._get_wrapped_object_().Polarity)

    @polarity.setter
    def polarity(self, value: PolarityType):
        """
        Gets or sets the polarity (+/-) filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.PolarityType for possible values
        """
        assert type(value) is PolarityType
        self._get_wrapped_object_().Polarity = value.value

    @property
    def souce_fragmentaion_value_count(self) -> int:
        """
        Gets the number of Source Fragmentation values. This is the number of values
        related to sid mode. 1 for "single value", 2 for "ramp" and 1 per mass range
        for "SIM".
        """
        return self._get_wrapped_object_().SouceFragmentaionValueCount

    @property
    def dependent(self) -> TriState:
        """
        Gets or sets the dependent scan filtering rule.
        """
        return TriState(self._get_wrapped_object_().Dependent)

    @dependent.setter
    def dependent(self, value: TriState):
        """
        Gets or sets the dependent scan filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().Dependent = value.value

    @property
    def source_fragmentation(self) -> TriState:
        """
        Gets or sets source fragmentation scan filtering rule.
        """
        return TriState(self._get_wrapped_object_().SourceFragmentation)

    @source_fragmentation.setter
    def source_fragmentation(self, value: TriState):
        """
        Gets or sets source fragmentation scan filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().SourceFragmentation = value.value

    @property
    def source_fragmentation_type(self) -> SourceFragmentationValueType:
        """
        Gets or sets the source fragmentation type filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.SourceFragmentationValueType for
        possible values
        """
        return SourceFragmentationInfoValidType(self._get_wrapped_object_().SourceFragmentationType)

    @source_fragmentation_type.setter
    def source_fragmentation_type(self, value: SourceFragmentationValueType):
        """
        Gets or sets the source fragmentation type filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.SourceFragmentationValueType for
        possible values
        """
        assert type(value) is SourceFragmentationValueType
        self._get_wrapped_object_().SourceFragmentationType = value.value

    @property
    def scan_mode(self) -> ScanModeType:
        """
        Gets or sets the scan type filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.ScanModeType for possible values
        """
        return ScanModeType(self._get_wrapped_object_().ScanMode)

    @scan_mode.setter
    def scan_mode(self, value: ScanModeType):
        """
        Gets or sets the scan type filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.ScanModeType for possible values
        """
        assert type(value) is ScanModeType
        self._get_wrapped_object_().ScanMode = value.value

    @property
    def mass_analyzer(self) -> MassAnalyzerType:
        """
        Gets or sets the mass analyzer scan filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.MassAnalyzerType for possible values
        """
        return MassAnalyzerType(self._get_wrapped_object_().MassAnalyzer)

    @mass_analyzer.setter
    def mass_analyzer(self, value: MassAnalyzerType):
        """
        Gets or sets the mass analyzer scan filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.MassAnalyzerType for possible values
        """
        assert type(value) is MassAnalyzerType
        self._get_wrapped_object_().MassAnalyzer = value.value

    @property
    def detector(self) -> DetectorType:
        """
        Gets or sets the detector scan filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.DetectorType for possible values
        """
        return DetectorType(self._get_wrapped_object_().Detector)

    @detector.setter
    def detector(self, value: DetectorType):
        """
        Gets or sets the detector scan filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.DetectorType for possible values
        """
        assert type(value) is DetectorType
        self._get_wrapped_object_().Detector = value.value

    @property
    def turbo_scan(self) -> TriState:
        """
        Gets or sets the turbo scan filtering rule.
        """
        return TriState(self._get_wrapped_object_().TurboScan)

    @turbo_scan.setter
    def turbo_scan(self, value: TriState):
        """
        Gets or sets the turbo scan filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().TurboScan = value.value

    @property
    def ionization_mode(self) -> IonizationModeType:
        """
        Gets or sets the ionization mode filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.IonizationModeType for possible
        values
        """
        return IonizationModeType(self._get_wrapped_object_().IonizationMode)

    @ionization_mode.setter
    def ionization_mode(self, value: IonizationModeType):
        """
        Gets or sets the ionization mode filtering rule.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.IonizationModeType for possible
        values
        """
        assert type(value) is IonizationModeType
        self._get_wrapped_object_().IonizationMode = value.value

    @property
    def corona(self) -> TriState:
        """
        Gets or sets the corona scan filtering rule.
        """
        return TriState(self._get_wrapped_object_().Corona)

    @corona.setter
    def corona(self, value: TriState):
        """
        Gets or sets the corona scan filtering rule.
        """
        assert type(value) is TriState
        self._get_wrapped_object_().Corona = value.value

    @property
    def ms_order(self) -> MsOrderType:
        """
        Gets or sets the scan power or MS/MS mode filtering rule, such as MS3 or Parent
        scan.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.MSOrderType for possible values
        """
        return MsOrderType(self._get_wrapped_object_().MSOrder)

    @ms_order.setter
    def ms_order(self, value: MsOrderType):
        """
        Gets or sets the scan power or MS/MS mode filtering rule, such as MS3 or Parent
        scan.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.MSOrderType for possible values
        """
        assert type(value) is MsOrderType
        self._get_wrapped_object_().MSOrder = value.value

    def compensation_voltage_value(self, index: int) -> float:
        """
        Retrieves a compensation voltage (cv) value at 0-based index.
        
        Parameters:
        index:
        Index of compensation voltage to be retrieved
        
        Returns:
        Compensation voltage value (cv) at 0-based index
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Interfaces.IScanFilter.CompensationVoltageCount
        to get the count of compensation voltage values.
        """
        return self._get_wrapped_object_().CompensationVoltageValue(index)

    def get_source_fragmentation_info_valid(self, index: int) -> SourceFragmentationInfoValidType:
        """
        Get source fragmentation info valid, at zero based index.
        
        Parameters:
        index:
        The index.
        
        Returns:
        The ThermoFisher.CommonCore.Data.Interfaces.SourceFragmentationInfoValidType.
        """
        return self._get_wrapped_object_().GetSourceFragmentationInfoValid(index)

    def index_to_multiple_activation_index(self, index: int) -> int:
        """
        Convert an index to multiple activation index. Converts a simple mass index to
        the index to the unique mass, taking into account multiple activations.
        
        Parameters:
        index:
        The index to convert.
        
        Returns:
        The index of the unique mass.
        """
        return self._get_wrapped_object_().IndexToMultipleActivationIndex(index)

    def source_fragmentation_value(self, index: int) -> float:
        """
        Retrieves a source fragmentation value (sid) at 0-based index.
        
        Parameters:
        index:
        Index of source fragmentation value to be retrieved
        
        Returns:
        Source Fragmentation Value (sid) at 0-based index
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Interfaces.IScanFilter.SouceFragmentaionValueCount
        to get the count of source fragmentation values.
        """
        return self._get_wrapped_object_().SourceFragmentationValue(index)

    def __str__(self) -> str:
        """
        Convert to string. Mass values are converted as per the precision.
        
        Returns:
        The System.String.
        """
        return self._get_wrapped_object_().ToString()
