from __future__ import annotations
from typing import Any
from fisher_py.exceptions import CoreException


class NetWrapperBase(object):

    _wrapped_type = None

    def __init__(self):
        self._wrapped_object = None

    def _get_wrapped_object_(self) -> Any:
        if self._wrapped_object is None:
            raise CoreException('This object was not initialized properly.')

        return self._wrapped_object
    
    @classmethod
    def _get_wrapper_(cls: type, net_obj: Any) -> NetWrapperBase:
        wrapper_obj = cls()
        wrapper_obj._wrapped_object = net_obj
        return wrapper_obj
