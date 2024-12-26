from typing import TypeVar, Generic
import clr

clr.AddReference('System')
import System
import System.Collections.Generic as generic

T = TypeVar('T')

class WrappedNetList(Generic[T], list):

    def __getitem__(self, index: int) -> T:
        return self.__wrapped_iterable[index]
    
    def __setitem__(self, index: int, value: T):
        super().__setitem__(index, value)
        self.__wrapped_iterable[index] = value

    def append(self, obj):
        super().append(obj)
        self.__wrapped_iterable.Add(obj)
    
    def remove(self, value):
        super().remove(value)
        self.__wrapped_iterable.Remove(value)

    def __init__(self, net_iterable):
        super().__init__([i for i in net_iterable])
        self.__wrapped_iterable = net_iterable
