import enum


class TrayShape(enum.Enum):
    """The auto sampler tray shape."""
    
    """Vials or wells are arranged in a rectangle on the tray"""
    Rectangular = 0
    
    """Vials are arranged in a circle."""
    Circular = 1
    
    """Vials are staggered on odd numbered positions on the tray."""
    StaggeredOdd = 2
    
    """Vials are staggered on even numbered positions on the tray."""
    StaggeredEven = 3
    
    """The layout is unknown."""
    Unknown = 4
    
    """The layout information is invalid. No other tray layout data should be displayed."""
    Invalid = 5
