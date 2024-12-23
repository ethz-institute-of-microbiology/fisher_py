from typing import List
from fisher_py.net_wrapping import NetWrapperBase
from fisher_py.data.business import BracketType


class SequenceInfo(NetWrapperBase):
    @property
    def column_width(self) -> List[int]:
        """
        Gets the display width of each sequence column
        """
        return self._get_wrapped_object_().ColumnWidth

    @property
    def type_to_column_position(self) -> List[int]:
        """
        Gets the column order (see home page?)
        """
        return self._get_wrapped_object_().TypeToColumnPosition

    @property
    def bracket(self) -> BracketType:
        """
        Gets the sequence bracket type. This determines which groups of samples use the
        same calibration curve.
        """
        return BracketType(self._get_wrapped_object_().Bracket)

    @property
    def user_private_label(self) -> List[str]:
        """
        Gets the set of column names for application specific columns
        """
        return self._get_wrapped_object_().UserPrivateLabel

    @property
    def tray_configuration(self) -> str:
        """
        Gets a description of the auto-sampler tray
        """
        return self._get_wrapped_object_().TrayConfiguration

    @property
    def user_label(self) -> List[str]:
        """
        Gets the user configurable column names
        """
        return self._get_wrapped_object_().UserLabel
