
from fisher_py.net_wrapping.wrapped_net_list import WrappedNetList
from fisher_py.utils import to_net_list
import json

EPS = 1e-16

def test_wrapped_lists_can_be_created():
    net_list = to_net_list([1, 2, 3], int)
    wrapped_list = WrappedNetList[int](net_list)
    assert len(wrapped_list) == 3    

def test_wrapped_lists_support_floats():
    values = [6.4, 7.7, 34.23, 1e-9, 13e12]
    net_list = to_net_list(values, float)
    wrapped_list = WrappedNetList[float](net_list)

    for actual, expected in zip(values, wrapped_list):
        assert abs(actual - expected) < EPS, f'Expected value "{expected}" but actual value was "{actual}"'

def test_wrapped_lists_support_strings():
    values = ['This is a string', 'another string', 'still more strings']
    net_list = to_net_list(values, str)
    wrapped_list = WrappedNetList[str](net_list)

    for actual, expected in zip(values, wrapped_list):
        assert actual == expected, f'Expected value "{expected}" but actual value was "{actual}"'

def test_wrapped_lists_can_be_serialized():
    values = [3, 6, 8, 2]
    net_list = to_net_list(values, int)
    wrapped_list = WrappedNetList[int](net_list)
    json_str = json.dumps(wrapped_list)
    assert json_str == '[3, 6, 8, 2]'

def test_wrapped_lists_items_can_be_added():
    values = [3, 6, 8, 2]
    net_list = to_net_list(values, int)
    wrapped_list = WrappedNetList[int](net_list)
    wrapped_list.append(77)
    wrapped_list.append(80)
    assert wrapped_list[-2] == 77
    assert wrapped_list[-1] == 80

def test_wrapped_lists_items_can_be_inserted():
    values = [3, 6, 8, 2]
    net_list = to_net_list(values, int)
    wrapped_list = WrappedNetList[int](net_list)
    wrapped_list.insert(1, 10)
    wrapped_list.insert(-2, 7)
    assert wrapped_list[1] == 10
    assert wrapped_list[3] == 7

def test_wrapped_lists_items_can_be_removed():
    values = [3, 6, 8, 2]
    net_list = to_net_list(values, int)
    wrapped_list = WrappedNetList[int](net_list)
    wrapped_list.remove(8)
    wrapped_list.remove(3)
    assert len(wrapped_list) == len(values) - 2
    assert 8 not in wrapped_list
    assert 3 not in wrapped_list

def test_wrapped_lists_can_be_cleared():
    values = [3, 6, 8, 2]
    net_list = to_net_list(values, int)
    wrapped_list = WrappedNetList[int](net_list)
    wrapped_list.clear()
    assert len(wrapped_list) == 0

def test_wrapped_lists_can_use_python_indexing():
    values = [3, 6, 8, 2]
    net_list = to_net_list(values, int)
    wrapped_list = WrappedNetList[int](net_list)
    result = wrapped_list[1:4]
    assert result[0] == 6
    assert result[1] == 8
    assert result[2] == 2
