
from fisher_py.net_wrapping.wrapped_net_array import WrappedNetArray
from fisher_py.utils import to_net_array
import json

EPS = 1e-16

def test_wrapped_arrays_can_be_created():
    net_list = to_net_array([1, 2, 3], int)
    wrapped_list = WrappedNetArray[int](net_list)
    assert len(wrapped_list) == 3    

def test_wrapped_arrays_support_floats():
    values = [6.4, 7.7, 34.23, 1e-9, 13e12]
    net_list = to_net_array(values, float)
    wrapped_list = WrappedNetArray[float](net_list)

    for actual, expected in zip(values, wrapped_list):
        assert abs(actual - expected) < EPS, f'Expected value "{expected}" but actual value was "{actual}"'

def test_wrapped_arrays_support_strings():
    values = ['This is a string', 'another string', 'still more strings']
    net_list = to_net_array(values, str)
    wrapped_list = WrappedNetArray[str](net_list)

    for actual, expected in zip(values, wrapped_list):
        assert actual == expected, f'Expected value "{expected}" but actual value was "{actual}"'

def test_wrapped_arrays_can_be_serialized():
    values = [3, 6, 8, 2]
    net_list = to_net_array(values, int)
    wrapped_list = WrappedNetArray[int](net_list)
    json_str = json.dumps(wrapped_list)
    assert json_str == '[3, 6, 8, 2]'

def test_wrapped_arrays_items_cannot_be_added():
    values = [3, 6, 8, 2]
    net_list = to_net_array(values, int)
    wrapped_list = WrappedNetArray[int](net_list)

    try:
        wrapped_list.append(77)
        assert False, 'Adding items should not be possible'
    except NotImplementedError:
        pass

def test_wrapped_arrays_items_cannot_be_inserted():
    values = [3, 6, 8, 2]
    net_list = to_net_array(values, int)
    wrapped_list = WrappedNetArray[int](net_list)

    try:
        wrapped_list.insert(2, 77)
        assert False, 'Inserting items should not be possible'
    except NotImplementedError:
        pass

def test_wrapped_arrays_items_cannot_be_removed():
    values = [3, 6, 8, 2]
    net_list = to_net_array(values, int)
    wrapped_list = WrappedNetArray[int](net_list)

    try:
        wrapped_list.remove(8)
        assert False, 'Removing items should not be possible'
    except NotImplementedError:
        pass

def test_wrapped_arrays_cannot_be_cleared():
    values = [3, 6, 8, 2]
    net_list = to_net_array(values, int)
    wrapped_list = WrappedNetArray[int](net_list)

    try:
        wrapped_list.clear()
        assert False, 'Removing items should not be possible'
    except NotImplementedError:
        pass

def test_wrapped_arrays_can_use_python_indexing():
    values = [3, 6, 8, 2]
    net_list = to_net_array(values, int)
    wrapped_list = WrappedNetArray[int](net_list)
    result = wrapped_list[1:4]
    assert result[0] == 6
    assert result[1] == 8
    assert result[2] == 2
