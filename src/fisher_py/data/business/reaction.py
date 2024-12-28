from fisher_py.net_wrapping import NetWrapperBase
from fisher_py.data.filter_enums import ActivationType


class Reaction(NetWrapperBase):
    """
    The Reaction interface. Defines a reaction for fragmenting an ion (an MS/MS stage).
    """

    def __init__(self, reaction_net):
        super().__init__()
        self._wrapped_object = reaction_net

    @property
    def precursor_mass(self) -> float:
        """
        Gets the precursor mass (mass acted on)
        """
        return self._get_wrapped_object_().PrecursorMass

    @property
    def collision_energy(self) -> float:
        """
        Gets the collision energy of this reaction
        """
        return self._get_wrapped_object_().CollisionEnergy

    @property
    def isolation_width(self) -> float:
        """
        Gets the isolation width of the precursor mass
        """
        return self._get_wrapped_object_().IsolationWidth

    @property
    def precursor_range_is_valid(self) -> bool:
        """
        Gets a value indicating whether precursor range is valid. If this is true, then
        ThermoFisher.CommonCore.Data.Business.IReaction.PrecursorMass is still the center
        of the range, but the values ThermoFisher.CommonCore.Data.Business.IReaction.FirstPrecursorMass
        and ThermoFisher.CommonCore.Data.Business.IReaction.LastPrecursorMass define
        the limits of the precursor mass range
        """
        return self._get_wrapped_object_().PrecursorRangeIsValid

    @property
    def first_precursor_mass(self) -> float:
        """
        Gets the start of the precursor mass range (only if ThermoFisher.CommonCore.Data.Business.IReaction.PrecursorRangeIsValid)
        """
        return self._get_wrapped_object_().FirstPrecursorMass

    @property
    def last_precursor_mass(self) -> float:
        """
        Gets the end of the precursor mass range (only if ThermoFisher.CommonCore.Data.Business.IReaction.PrecursorRangeIsValid)
        """
        return self._get_wrapped_object_().LastPrecursorMass

    @property
    def collision_energy_valid(self) -> bool:
        """
        Gets a value indicating whether collision energy is valid.
        """
        return self._get_wrapped_object_().CollisionEnergyValid

    @property
    def activation_type(self) -> ActivationType:
        """
        Gets the activation type.
        """
        return ActivationType(self._get_wrapped_object_().ActivationType)

    @property
    def multiple_activation(self) -> bool:
        """
        Gets a value indicating whether this is a multiple activation. In a table of
        reactions, a multiple activation is a second, or further, activation (fragmentation
        method) applied to the same precursor mass. Precursor mass values should be obtained
        from the original activation, and may not be returned by subsequent multiple
        activations.
        """
        return self._get_wrapped_object_().MultipleActivation

    @property
    def isolation_width_offset(self) -> float:
        """
        Gets the isolation width offset.
        """
        return self._get_wrapped_object_().IsolationWidthOffset

