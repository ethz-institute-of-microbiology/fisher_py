from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher


class CommonCoreDataObject(NetWrapperBase):
    """
    CommonCoreData object is an abstract class. It includes a deep equals feature
    """

    def __init__(self):
        super().__init__()

    def deep_equals(self, value_to_compare: object) -> bool:
        """
        Provides a custom deep equality operation when checking for equality.
        
        Parameters:
        valueToCompare:
        The value to compare.
        
        Returns:
        True if the items are equal, false if they are not.
        """
        return self._get_wrapped_object().DeepEquals(value_to_compare._get_wrapped_object_())

    def equals(self, obj: object) -> bool:
        """
        Compares this object with another. Traverse the set of member variables to compare
        against the object that was passed in. Determines whether the specified System.Object
        is equal to the current System.Object.
        
        Parameters:
        obj:
        The System.Object to compare with the current System.Object.
        
        Returns:
        true if the specified System.Object is equal to the current System.Object; otherwise,
        false.
        
        Exceptions:
        T:System.NullReferenceException:
        The obj parameter is null.
        """
        return self._get_wrapped_object().Equals(obj._get_wrapped_object_())

    def get_hash_code(self) -> int:
        """
        Serves as a hash function for a particular type.
        
        Returns:
        A hash code for the current System.Object.
        """
        return self._get_wrapped_object().GetHashCode()

    def perform_default_settings(self):
        """
        Performs the default settings for the data object. This can overridden in each
        data object that implements the interface to perform initialization settings.
        """
        self._get_wrapped_object().PerformDefaultSettings()
