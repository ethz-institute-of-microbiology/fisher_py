
from fisher_py.net_wrapping.wrapped_net_list import WrappedNetList
from fisher_py.utils import to_net_array, to_net_list
import json


def test_wrapped_lists_can_be_created():
    # net_array = to_net_array([1, 2, 3], int)
    net_array = to_net_list([1, 2, 3], int)
    wrapped_list = WrappedNetList[int](net_array)

    print(wrapped_list[1])
    wrapped_list.append(6)

    for i in wrapped_list:
        print(i)

    json.dumps(wrapped_list)
