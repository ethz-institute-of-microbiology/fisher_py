from fisher_py.net_wrapping import NetWrapperBase
from fisher_py.data.tray_shape import TrayShape


class AutoSamplerInformation(NetWrapperBase):
    """
    The AutoSamplerInformation interface.
    """
    
    @property
    def tray_index(self) -> int:
        """Gets or sets the tray index, -1 for 'not recorded'"""
        return self._get_wrapped_object_().TrayIndex
    
    @tray_index.setter
    def tray_index(self, value: int):
        """Gets or sets the tray index, -1 for 'not recorded'"""
        assert type(value) is int
        self._get_wrapped_object_().TrayIndex = value
        
    @property
    def vial_index(self) -> int:
        """Gets or sets the vial index, -1 for 'not recorded'"""
        return self._get_wrapped_object_().VialIndex
    
    @vial_index.setter
    def vial_index(self, value: int):
        """Gets or sets the vial index, -1 for 'not recorded'"""
        assert type(value) is int
        self._get_wrapped_object_().VialIndex = value
        
    @property
    def vials_per_tray(self) -> int:
        """Gets or sets the number of vials (or wells) per tray. -1 for 'not recorded'"""
        return self._get_wrapped_object_().VialsPerTray
    
    @vials_per_tray.setter
    def vials_per_tray(self, value: int):
        """Gets or sets the number of vials (or wells) per tray. -1 for 'not recorded'"""
        assert type(value) is int
        self._get_wrapped_object_().VialsPerTray = value
        
    @property
    def vials_per_tray_x(self) -> int:
        """Gets or sets the number of vials (or wells) per tray, across the tray. -1 for 'not recorded'"""
        return self._get_wrapped_object_().VialsPerTrayX
    
    @vials_per_tray_x.setter
    def vials_per_tray_x(self, value: int):
        """Gets or sets the number of vials (or wells) per tray, across the tray. -1 for 'not recorded'"""
        assert type(value) is int
        self._get_wrapped_object_().VialsPerTrayX = value
        
    @property
    def vials_per_tray_y(self) -> int:
        """Gets or sets the number of vials (or wells) per tray, across the tray. -1 for 'not recorded'"""
        return self._get_wrapped_object_().VialsPerTrayY
    
    @vials_per_tray_y.setter
    def vials_per_tray_y(self, value: int):
        """Gets or sets the number of vials (or wells) per tray, across the tray. -1 for 'not recorded'"""
        assert type(value) is int
        self._get_wrapped_object_().VialsPerTrayY = value
        
    @property
    def tray_shape(self) -> TrayShape:
        """Gets or sets the shape. If this property returns "Invalid", no other values in
        this object contain usable information. Invalid data can occur for older raw
        file formats, before auto sampler data was added.
        """
        return TrayShape(self._get_wrapped_object_().TrayShape)
    
    @tray_shape.setter
    def tray_shape(self, value: TrayShape):
        """Gets or sets the shape. If this property returns "Invalid", no other values in
        this object contain usable information. Invalid data can occur for older raw
        file formats, before auto sampler data was added.
        """
        assert type(value) is TrayShape
        self._get_wrapped_object_().TrayShape = value.value
        
    @property
    def tray_shape_as_string(self) -> int:
        """Gets the tray shape as a string"""
        return self._get_wrapped_object_().TrayShapeAsString
    
    @property
    def tray_name(self) -> int:
        """Gets or sets the tray name."""
        return self._get_wrapped_object_().TrayName
    
    @tray_name.setter
    def tray_name(self, value: str):
        """Gets or sets the tray name."""
        assert type(value) is str
        self._get_wrapped_object_().TrayName = value
    