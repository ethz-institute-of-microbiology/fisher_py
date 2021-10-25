from fisher_py.net_wrapping import NetWrapperBase
from fisher_py.data.business import Range, Reaction
from fisher_py.data.filter_enums import (
    EventAccurateMass, FieldFreeRegionType, TriState, CompensationVoltageType, SectorScanType, ActivationType,
    PolarityType, MsOrderType, SourceFragmentationValueType, ScanModeType, ScanDataType, IonizationModeType,
    DetectorType, MassAnalyzerType, EnergyType
)


class ScanEvent(NetWrapperBase):
    """
    The ScanEvent interface. Determines how scans are done.
    """

    @property
    def field_free_region(self) -> FieldFreeRegionType:
        """
        Gets the field free region setting.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.FieldFreeRegionType for possible
        values
        """
        return FieldFreeRegionType(self._get_wrapped_object_().FieldFreeRegion)

    @property
    def enhanced(self) -> TriState:
        """
        Gets the enhanced scan setting.
        """
        return TriState(self._get_wrapped_object_().Enhanced)

    @property
    def multiple_photon_dissociation(self) -> TriState:
        """
        Gets the multi-photon dissociation setting.
        """
        return TriState(self._get_wrapped_object_().MultiplePhotonDissociation)

    @property
    def multiple_photon_dissociation_value(self) -> float:
        """
        Gets the multi-photon dissociation value.
        
        Value:
        Floating point multi-photon dissociation value
        """
        return self._get_wrapped_object_().MultiplePhotonDissociationValue

    @property
    def electron_capture_dissociation(self) -> TriState:
        """
        Gets the electron capture dissociation setting.
        """
        return TriState(self._get_wrapped_object_().ElectronCaptureDissociation)

    @property
    def electron_capture_dissociation_value(self) -> float:
        """
        Gets the electron capture dissociation value.
        
        Value:
        Floating point electron capture dissociation value
        """
        return self._get_wrapped_object_().ElectronCaptureDissociationValue

    @property
    def photo_ionization(self) -> TriState:
        """
        Gets the photo ionization setting.
        """
        return TriState(self._get_wrapped_object_().PhotoIonization)

    @property
    def pulsed_q_dissociation(self) -> TriState:
        """
        Gets pulsed dissociation setting.
        """
        return TriState(self._get_wrapped_object_().PulsedQDissociation)

    @property
    def pulsed_q_dissociation_value(self) -> float:
        """
        Gets the pulsed dissociation value.
        
        Value:
        Floating point pulsed dissociation value
        """
        return self._get_wrapped_object_().PulsedQDissociationValue

    @property
    def electron_transfer_dissociation(self) -> TriState:
        """
        Gets the electron transfer dissociation setting.
        """
        return TriState(self._get_wrapped_object_().ElectronTransferDissociation)

    @property
    def electron_transfer_dissociation_value(self) -> float:
        """
        Gets the electron transfer dissociation value.
        
        Value:
        Floating point electron transfer dissociation value
        """
        return self._get_wrapped_object_().ElectronTransferDissociationValue

    @property
    def higher_energy_ci_d(self) -> TriState:
        """
        Gets the higher energy CID setting.
        """
        return TriState(self._get_wrapped_object_().HigherEnergyCiD)

    @property
    def higher_energy_ci_d_value(self) -> float:
        """
        Gets the higher energy CID value.
        
        Value:
        Floating point higher energy CID value
        """
        return self._get_wrapped_object_().HigherEnergyCiDValue

    @property
    def ultra(self) -> TriState:
        """
        Gets the ultra scan setting.
        """
        return TriState(self._get_wrapped_object_().Ultra)

    @property
    def multiplex(self) -> TriState:
        """
        Gets the Multiplex type
        """
        return TriState(self._get_wrapped_object_().Multiplex)

    @property
    def param_b(self) -> TriState:
        """
        Gets the parameter b.
        """
        return TriState(self._get_wrapped_object_().ParamB)

    @property
    def param_f(self) -> TriState:
        """
        Gets the parameter f.
        """
        return TriState(self._get_wrapped_object_().ParamF)

    @property
    def multi_notch(self) -> TriState:
        """
        Gets the Multi notch (Synchronous Precursor Selection) type
        """
        return TriState(self._get_wrapped_object_().MultiNotch)

    @property
    def param_r(self) -> TriState:
        """
        Gets the parameter r.
        """
        return TriState(self._get_wrapped_object_().ParamR)

    @property
    def param_v(self) -> TriState:
        """
        Gets the parameter v.
        """
        return TriState(self._get_wrapped_object_().ParamV)

    @property
    def name(self) -> str:
        """
        Gets the event Name.
        """
        return self._get_wrapped_object_().Name

    @property
    def supplemental_activation(self) -> TriState:
        """
        Gets supplemental activation type setting.
        """
        return TriState(self._get_wrapped_object_().SupplementalActivation)

    @property
    def multi_state_activation(self) -> TriState:
        """
        Gets MultiStateActivation type setting.
        """
        return TriState(self._get_wrapped_object_().MultiStateActivation)

    @property
    def compensation_voltage(self) -> TriState:
        """
        Gets Compensation Voltage Option setting.
        """
        return TriState(self._get_wrapped_object_().CompensationVoltage)

    @property
    def compensation_volt_type(self) -> CompensationVoltageType:
        """
        Gets Compensation Voltage type setting.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.CompensationVoltageType for possible
        values
        """
        return CompensationVoltageType(self._get_wrapped_object_().CompensationVoltType)

    @property
    def scan_type_index(self) -> int:
        """
        Gets encoded form of segment and scan event number.
        
        Value:
        HIWORD == segment, LOWORD == scan type
        """
        return self._get_wrapped_object_().ScanTypeIndex

    @property
    def mass_count(self) -> int:
        """
        Gets number of (precursor) masses
        
        Value:
        The size of mass array
        """
        return self._get_wrapped_object_().MassCount

    @property
    def param_a(self) -> TriState:
        """
        Gets the parameter a.
        """
        return TriState(self._get_wrapped_object_().ParamA)

    @property
    def mass_range_count(self) -> int:
        """
        Gets the number of mass ranges for final scan
        
        Value:
        The size of mass range array
        """
        return self._get_wrapped_object_().MassRangeCount

    @property
    def source_fragmentation_info_count(self) -> int:
        """
        Gets the number of source fragmentation info values
        
        Value:
        The size of source fragmentation info array
        """
        return self._get_wrapped_object_().SourceFragmentationInfoCount

    @property
    def sector_scan(self) -> SectorScanType:
        """
        Gets the sector scan setting. Applies to 2 sector (Magnetic, electrostatic) Mass
        spectrometers, or hybrids.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.SectorScanType for possible values
        """
        return SectorScanType(self._get_wrapped_object_().SectorScan)

    @property
    def lock(self) -> TriState:
        """
        Gets the lock scan setting.
        """
        return TriState(self._get_wrapped_object_().Lock)

    @property
    def polarity(self) -> PolarityType:
        """
        Gets the polarity of the scan.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.PolarityType for possible values
        """
        return PolarityType(self._get_wrapped_object_().Polarity)

    @property
    def ms_order(self) -> MsOrderType:
        """
        Gets the scan MS/MS power setting.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.MSOrderType for possible values
        """
        return MsOrderType(self._get_wrapped_object_().MsOrder)

    @property
    def dependent(self) -> TriState:
        """
        Gets the dependent scan setting. A scan is "dependent" if the scanning method
        is based on analysis of data from a previous scan.
        """
        return TriState(self._get_wrapped_object_().Dependent)

    @property
    def source_fragmentation(self) -> TriState:
        """
        Gets source fragmentation scan setting.
        """
        return TriState(self._get_wrapped_object_().SourceFragmentation)

    @property
    def source_fragmentation_type(self) -> SourceFragmentationValueType:
        """
        Gets the source fragmentation type setting.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.SourceFragmentationValueType for
        possible values
        """
        return SourceFragmentationValueType(self._get_wrapped_object_().SourceFragmentationType)

    @property
    def scan_mode(self) -> ScanModeType:
        """
        Gets the scan type setting.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.ScanModeType for possible values
        """
        return ScanModeType(self._get_wrapped_object_().ScanMode)

    @property
    def scan_data(self) -> ScanDataType:
        """
        Gets the scan data format (profile or centroid).
        """
        return ScanDataType(self._get_wrapped_object_().ScanData)

    @property
    def ionization_mode(self) -> IonizationModeType:
        """
        Gets the ionization mode scan setting.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.IonizationModeType for possible
        values
        """
        return IonizationModeType(self._get_wrapped_object_().IonizationMode)

    @property
    def corona(self) -> TriState:
        """
        Gets the corona scan setting.
        """
        return TriState(self._get_wrapped_object_().Corona)

    @property
    def detector(self) -> DetectorType:
        """
        Gets the detector validity setting. The property ThermoFisher.CommonCore.Data.Interfaces.IScanEventBase.DetectorValue
        only contains valid information when this is set to "DetectorType.Valid"
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.DetectorType for possible values
        """
        return DetectorType(self._get_wrapped_object_().Detector)

    @property
    def detector_value(self) -> float:
        """
        Gets the detector value. This should only be used when valid. ThermoFisher.CommonCore.Data.Interfaces.IScanEventBase.Detector
        
        Value:
        Floating point detector value
        """
        return self._get_wrapped_object_().DetectorValue

    @property
    def wideband(self) -> TriState:
        """
        Gets the wideband scan setting.
        """
        return TriState(self._get_wrapped_object_().Wideband)

    @property
    def mass_analyzer(self) -> MassAnalyzerType:
        """
        Gets the mass analyzer scan setting.
        
        Value:
        See ThermoFisher.CommonCore.Data.FilterEnums.MassAnalyzerType for possible values
        """
        return MassAnalyzerType(self._get_wrapped_object_().MassAnalyzerType)

    @property
    def turbo_scan(self) -> TriState:
        """
        Gets the turbo scan setting.
        """
        return TriState(self._get_wrapped_object_().TurboScan)

    def get_activation(self, index: int) -> ActivationType:
        """
        Retrieves activation type at 0-based index.
        
        Parameters:
        index:
        Index of activation to be retrieved
        
        Returns:
        activation of MS step; See ThermoFisher.CommonCore.Data.FilterEnums.ActivationType
        for possible values
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Interfaces.IScanEventBase.MassCount to get the
        count of activations.
        """
        return ActivationType(self._get_wrapped_object_().GetActivation(index))

    def get_energy(self, index: int) -> float:
        """
        Retrieves precursor(collision) energy value for MS step at 0-based index.
        
        Parameters:
        index:
        Index of precursor(collision) energy to be retrieved
        
        Returns:
        precursor(collision) energy of MS step
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Interfaces.IScanEventBase.MassCount to get the
        count of energies.
        """
        return self._get_wrapped_object_().GetEnergy(index)

    def get_energy_valid(self, index: int) -> EnergyType:
        """
        Retrieves precursor(collision) energy validation flag at 0-based index.
        
        Parameters:
        index:
        Index of precursor(collision) energy validation to be retrieved
        
        Returns:
        precursor(collision) energy validation of MS step; See ThermoFisher.CommonCore.Data.FilterEnums.EnergyType
        for possible values
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Interfaces.IScanEventBase.MassCount to get the
        count of precursor(collision) energy validations.
        """
        return EnergyType(self._get_wrapped_object_().GetEnergyValid(index))

    def get_first_precursor_mass(self, index: int) -> float:
        """
        Gets the first precursor mass. This is only valid data where "GetPrecursorRangeValidity"
        returns true for the same index.
        
        Parameters:
        index:
        The index.
        
        Returns:
        The first mass
        """
        return self._get_wrapped_object_().GetFirstPrecursorMass(index)

    def get_is_multiple_activation(self, index: int) -> bool:
        """
        Retrieves multiple activations flag at 0-based index of masses.
        
        Parameters:
        index:
        Index of flag to be retrieved
        
        Returns:
        true if mass at given index has multiple activations; false otherwise
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Interfaces.IScanEventBase.MassCount to get the
        count of masses.
        """
        return self._get_wrapped_object_().GetIsMultipleActivation(index)

    def get_isolation_width(self, index: int) -> float:
        """
        Gets the isolation width.
        
        Parameters:
        index:
        The index.
        
        Returns:
        The isolation width
        """
        return self._get_wrapped_object_().GetIsolationWidth(index)

    def get_isolation_width_offset(self, index: int) -> float:
        """
        Gets the isolation width offset.
        
        Parameters:
        index:
        The index.
        
        Returns:
        The isolation width offset
        """
        return self._get_wrapped_object_().GetIsolationWidthOffset(index)

    def get_last_precursor_mass(self, index: int) -> float:
        """
        Gets the last precursor mass. This is only valid data where "GetPrecursorRangeValidity"
        returns true for the same index.
        
        Parameters:
        index:
        The index.
        
        Returns:
        The last mass
        """
        return self._get_wrapped_object_().GetLastPrecursorMass(index)

    def get_mass(self, index: int) -> float:
        """
        Retrieves mass value for MS step at 0-based index.
        
        Parameters:
        index:
        Index of mass value to be retrieved
        
        Returns:
        Mass value of MS step
        
        Exceptions:
        T:System.IndexOutOfRangeException:
        Will be thrown when index >= MassCount
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Interfaces.IScanEventBase.MassCount to get the
        count of mass values.
        """
        return self._get_wrapped_object_().GetMass(index)

    def get_mass_range(self, index: int) -> Range:
        """
        Retrieves mass range for final scan at 0-based index.
        
        Parameters:
        index:
        Index of mass range to be retrieved
        
        Returns:
        Mass range for final scan at 0-based index
        
        Exceptions:
        T:System.IndexOutOfRangeException:
        Will be thrown when index >= MassRangeCount
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Interfaces.IScanEventBase.MassRangeCount to
        get the count of mass ranges.
        """
        return Range._get_wrapper_(self._get_wrapped_object_().GetMassRange(index))

    def get_precursor_range_validity(self, index: int) -> bool:
        """
        Determine if a precursor range is valid.
        
        Parameters:
        index:
        The index.
        
        Returns:
        true if valid
        """
        return self._get_wrapped_object_().GetPrecursorRangeValidity(index)

    def get_reaction(self, index: int) -> Reaction:
        """
        Gets the reaction data for the mass at 0 based index. Descries how a particular
        MS/MS precursor mass is fragmented. Equivalent to calling GetMass, GetEnergy,
        GetPrecursorRangeValidity, GetFirstPrecursorMass GetLastPrecursorMass, GetIsolationWidth,
        GetIsolationWidthOffset, GetEnergyValid GetActivation, GetIsMultipleActivation.
        Depending on the implementation of the interface, this call may be more efficient
        than calling several of the methods listed.
        
        Parameters:
        index:
        index of reaction
        
        Returns:
        reaction details
        """
        return Reaction(self._get_wrapped_object_().Reactions[index])

    def get_source_fragmentation_info(self, index: int) -> float:
        """
        Retrieves a source fragmentation info value at 0-based index.
        
        Parameters:
        index:
        Index of source fragmentation info to be retrieved
        
        Returns:
        Source Fragmentation info value at 0-based index
        
        Exceptions:
        T:System.IndexOutOfRangeException:
        Will be thrown when index >= SourceFragmentationInfoCount
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Interfaces.IScanEventBase.SourceFragmentationInfoCount
        to get the count of source fragmentation info values.
        """
        return self._get_wrapped_object_().GetSourceFragmentationInfo(index)

    @property
    def accurate_mass(self) -> EventAccurateMass:
        """
        Gets the accurate mass setting.
        """
        return EventAccurateMass(self._get_wrapped_object_().AccurateMass)

    @property
    def is_valid(self) -> bool:
        """
        Gets a value indicating whether this event is valid.
        """
        return self._get_wrapped_object_().IsValid

    @property
    def is_custom(self) -> bool:
        """
        Gets a value indicating whether this is a custom event. A custom event implies
        that any scan derived from this event could be different. The scan type must
        be inspected to determine the scanning mode, and not the event.
        """
        return self._get_wrapped_object_().IsCustom

    @property
    def source_fragmentation_mass_range_count(self) -> int:
        """
        Gets the source fragmentation mass range count.
        """
        return self._get_wrapped_object_().SourceFragmentationMassRangeCount

    @property
    def mass_calibrator_count(self) -> int:
        """
        Gets the mass calibrator count.
        """
        return self._get_wrapped_object_().MassCalibratorCount

    def get_mass_calibrator(self, index: int) -> float:
        """
        Get the mass calibrator, at a given index.
        
        Parameters:
        index:
        The index, which should be from 0 to MassCalibratorCount -1
        
        Returns:
        The mass calibrator.
        
        Exceptions:
        T:System.IndexOutOfRangeException:
        Thrown when requesting calibrator above count
        """
        return self._get_wrapped_object_().GetMassCalibrator(index)

    def get_source_fragmentation_mass_range(self, index: int) -> Range:
        """
        Get the source fragmentation mass range, at a given index.
        
        Parameters:
        index:
        The index.
        
        Returns:
        The mass range.
        """
        return Range._get_wrapper_(self._get_wrapped_object_().GetSourceFragmentationMassRange(index))

    def __str__(self) -> str:
        """
        Convert to string.
        
        Returns:
        The converted scanning method.
        """
        return self._get_wrapped_object_().ToString()