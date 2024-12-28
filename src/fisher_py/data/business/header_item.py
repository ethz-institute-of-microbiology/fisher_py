from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher
from fisher_py.data.business import GenericDataTypes


class HeaderItem(NetWrapperBase):
    """
    Defines the format of a log entry, including label (name of the field), data
    type, and numeric formatting.
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Business.HeaderItem

    def __init__(self, *args):
        super().__init__()

        if len(args) == 0:
            self._wrapped_object = self._wrapped_type()
        else:
            label, data_type, string_length_or_precision = args[0], args[1], args[2]
            assert type(label) is str
            assert type(data_type) is GenericDataTypes
            assert type(string_length_or_precision) is int

            if len(args) == 3:
                is_scientific_notation = False
            elif len(args) == 4:
                is_scientific_notation = args[3]
                assert type(is_scientific_notation) is bool
            else:
                raise ValueError('Unable to create header item.')

            self._wrapped_object = self._wrapped_type(label, data_type.value, string_length_or_precision, is_scientific_notation)

    @property
    def label(self) -> str:
        """
        Gets or sets the display label for the field. For example: If this a temperature,
        this label may be "Temperature" and the DataType may be "GenericDataTypes.FLOAT"
        """
        return self._get_wrapped_object_().Label

    @label.setter
    def label(self, value: str):
        """
        Gets or sets the display label for the field. For example: If this a temperature,
        this label may be "Temperature" and the DataType may be "GenericDataTypes.FLOAT"
        """
        assert type(value) is str
        self._get_wrapped_object_().Label = value

    @property
    def data_type(self) -> GenericDataTypes:
        """
        Gets or sets the data type for the field
        """
        return GenericDataTypes(self._get_wrapped_object_().DataType)

    @data_type.setter
    def data_type(self, value: GenericDataTypes):
        """
        Gets or sets the data type for the field
        """
        assert type(value) is GenericDataTypes
        self._get_wrapped_object_().DataType = value.value

    @property
    def string_length_or_precision(self) -> int:
        """
        Gets or sets the precision, if the data type is float or double, or string length
        of string fields.
        """
        return self._get_wrapped_object_().StringLengthOrPrecision

    @string_length_or_precision.setter
    def string_length_or_precision(self, value: int):
        """
        Gets or sets the precision, if the data type is float or double, or string length
        of string fields.
        """
        assert type(value) is int
        self._get_wrapped_object_().StringLengthOrPrecision = value

    @property
    def is_scientific_notation(self) -> bool:
        """
        Gets or sets a value indicating whether a number should be displayed in scientific
        notation
        """
        return self._get_wrapped_object_().IsScientificNotation

    @is_scientific_notation.setter
    def is_scientific_notation(self, value: bool):
        """
        Gets or sets a value indicating whether a number should be displayed in scientific
        notation
        """
        assert type(value) is bool
        self._get_wrapped_object_().IsScientificNotation = value

    @property
    def is_numeric(self) -> bool:
        """
        Gets a value indicating whether this is considered numeric data. This is the
        same test as performed for StatusLogPlottableData". Integer types: short and
        long (signed and unsigned) and floating types: float and double are defined as
        numeric.
        """
        return self._get_wrapped_object_().IsNumeric

    def format_value(self, value: str) -> str:
        """
        Re-formats the specified value per the current header's settings.
        
        Parameters:
        value:
        The value, as a string.
        
        Returns:
        The formatted value.
        """
        return self._get_wrapped_object().FormatValue(value)

    def is_variable_header(self, fields: int) -> bool:
        """
        Tests whether this is a variable header. A "variable header", if present as the
        first field in a table of headers, defines that each record has a variable number
        of valid fields. The first field in each data record will then be converted to
        "validity flags" which determine which of the fields in a data record have valid
        values.
        
        Parameters:
        fields:
        The number of fields in the header.
        
        Returns:
        True if this specifies that "variable length" records are used.
        """
        return self._get_wrapped_object().IsVariableHeader(fields)


