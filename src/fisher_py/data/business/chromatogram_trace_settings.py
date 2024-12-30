from __future__ import annotations
from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from typing import List
from fisher_py.data.business import Range, TraceType
from fisher_py.utils import to_net_list


class ChromatogramTraceSettings(NetWrapperBase):
    """
    Setting to define a chromatogram Trace.
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.ChromatogramTraceSettings

    def __init__(self, *args):
        super().__init__()

        if len(args) == 0:
            self._wrapped_object = self._wrapped_type()
        elif len(args) == 1:
            arg = args[0]
            if type(arg) is ChromatogramTraceSettings:
                self._wrapped_object = self._wrapped_type(arg._get_wrapped_object_())
            elif type(arg) is TraceType:
                self._wrapped_object = self._wrapped_type(arg.value)
            else:
                raise ValueError('Unable to create chromatogram trace settings')
        elif len(args) == 2:
            filter_, range_ = args
            assert type(filter_) is str
            assert type(range_) is Range
            self._wrapped_object = self._wrapped_type(filter_, range_._get_wrapped_object_())

    @property
    def mass_range_count(self) -> int:
        """
        Gets or sets the number of mass ranges, or wavelength ranges for PDA.
        
        Value:
        Numeric count of mass ranges
        
        Remarks:
        If ThermoFisher.CommonCore.Data.Business.ChromatogramTraceSettings.Trace is MassRange
        then mass range values are used to build trace.
        """
        return self._get_wrapped_object_().MassRangeCount

    @mass_range_count.setter
    def mass_range_count(self, value: int):
        """
        Gets or sets the number of mass ranges, or wavelength ranges for PDA.
        
        Value:
        Numeric count of mass ranges
        
        Remarks:
        If ThermoFisher.CommonCore.Data.Business.ChromatogramTraceSettings.Trace is MassRange
        then mass range values are used to build trace.
        """
        assert type(value) is int
        self._get_wrapped_object_().MassRangeCount = value

    @property
    def include_reference(self) -> bool:
        """
        Gets or sets a value indicating whether reference and exception peaks are included
        in this chromatogram trace
        """
        return self._get_wrapped_object_().IncludeReference

    @include_reference.setter
    def include_reference(self, value: bool):
        """
        Gets or sets a value indicating whether reference and exception peaks are included
        in this chromatogram trace
        """
        assert type(value) is bool
        self._get_wrapped_object_().IncludeReference = value

    @property
    def fragment_mass(self) -> float:
        """
        Gets or sets the fragment mass for neutral fragment filters.
        
        Value:
        Floating point fragment mass for neutral fragment filters
        """
        return self._get_wrapped_object_().FragmentMass

    @fragment_mass.setter
    def fragment_mass(self, value: float):
        """
        Gets or sets the fragment mass for neutral fragment filters.
        
        Value:
        Floating point fragment mass for neutral fragment filters
        """
        assert type(value) is float
        self._get_wrapped_object_().FragmentMass = value

    @property
    def filter(self) -> str:
        """
        Gets or sets the filter used in searching scans during trace build
        """
        return self._get_wrapped_object_().Filter

    @filter.setter
    def filter(self, value: str):
        """
        Gets or sets the filter used in searching scans during trace build
        """
        assert type(value) is str
        self._get_wrapped_object_().Filter = value

    @property
    def delay_in_min(self) -> float:
        """
        Gets or sets the delay in minutes.
        
        Value:
        Floating point delay in minutes
        """
        return self._get_wrapped_object_().DelayInMin

    @delay_in_min.setter
    def delay_in_min(self, value: float):
        """
        Gets or sets the delay in minutes.
        
        Value:
        Floating point delay in minutes
        """
        assert type(value) is float
        self._get_wrapped_object_().DelayInMin = value

    @property
    def trace(self) -> TraceType:
        """
        Gets or sets the type of trace to construct
        
        Value:
        see ThermoFisher.CommonCore.Data.Business.TraceType for more details
        """
        return TraceType(self._get_wrapped_object_().Trace)

    @trace.setter
    def trace(self, value: TraceType):
        """
        Gets or sets the type of trace to construct
        
        Value:
        see ThermoFisher.CommonCore.Data.Business.TraceType for more details
        """
        assert type(value) is TraceType
        self._get_wrapped_object_().Trace = value.value

    @property
    def mass_ranges(self) -> List[Range]:
        """
        Gets or sets the mass ranges.
        
        Value:
        Array of mass ranges
        
        Remarks:
        If ThermoFisher.CommonCore.Data.Business.ChromatogramTraceSettings.Trace is MassRange
        then mass range values are used to build trace.
        """
        return [Range._get_wrapper_(r) for r in self._get_wrapped_object_().MassRanges]

    @mass_ranges.setter
    def mass_ranges(self, value: List[Range]):
        """
        Gets or sets the mass ranges.
        
        Value:
        Array of mass ranges
        
        Remarks:
        If ThermoFisher.CommonCore.Data.Business.ChromatogramTraceSettings.Trace is MassRange
        then mass range values are used to build trace.
        """
        assert type(value) is list
        #value = to_net_list([r._get_wrapped_object_() for r in value], Range._wrapped_type)
        value = [r._get_wrapped_object_() for r in value]
        self._get_wrapped_object_().MassRanges = value

    @property
    def compound_names(self) -> List[str]:
        """
        Gets or sets the compound names.
        """
        return self._get_wrapped_object_().CompoundNames

    @compound_names.setter
    def compound_names(self, value: List[str]):
        """
        Gets or sets the compound names.
        """
        assert type(value) is list
        value = to_net_list(value, str)
        self._get_wrapped_object_().CompoundNames = value

    def clone(self) -> ChromatogramTraceSettings:
        """
        Copies all of the items to from this object into the returned object.
        
        Returns:
        The clone.
        """
        return ChromatogramTraceSettings._get_wrapper_(self._get_wrapped_object().Clone())

    def get_mass_range(self, index: int) -> Range:
        """
        Gets a range value at 0-based index.
        
        Parameters:
        index:
        Index at which to retrieve the range
        
        Returns:
        ThermoFisher.CommonCore.Data.Business.Range value at give index
        
        Remarks:
        Use ThermoFisher.CommonCore.Data.Business.ChromatogramTraceSettings.MassRangeCount
        to find out the count of mass ranges.
        If ThermoFisher.CommonCore.Data.Business.ChromatogramTraceSettings.Trace is MassRange
        then mass range values are used to build trace.
        """
        assert type(index) is int
        return Range._get_wrapper_(self._get_wrapped_object().GetMassRange(index))

    def set_mass_range(self, index: int, range: Range):
        """
        Sets a range value at 0-based index.
        
        Parameters:
        index:
        Index at which new range value is to be set
        
        range:
        New ThermoFisher.CommonCore.Data.Business.Range value to be set
        
        Remarks:
        Set count of mass ranges using ThermoFisher.CommonCore.Data.Business.ChromatogramTraceSettings.MassRangeCount
        before setting any mass ranges.
        If ThermoFisher.CommonCore.Data.Business.ChromatogramTraceSettings.Trace is MassRange
        then mass range values are used to build trace.
        """
        assert type(index) is int
        assert type(range) is Range
        self._get_wrapped_object().SetMassRange(index, range._get_wrapped_object_())

