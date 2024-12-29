from typing import TypeVar, Generic, Union
import clr

clr.AddReference('System')
import System
import System.Collections.Generic as generic

T = TypeVar('T')

class WrappedNetList(Generic[T], list):

    def __getitem__(self, index: Union[int, slice]) -> T:
        if type(index) is slice:
            start, step, stop = index.start, index.step, index.stop
            if step is None:
                step = 1
            start, step, stop = map(self.__ensure_positive_index__, [start, step, stop])
            sublist = []
            for i in range(start, stop, step):
                sublist.append(self.__wrapped_iterable[i])            
            return sublist
        index = self.__ensure_positive_index__(index)
        return self.__wrapped_iterable[index]
    
    def __setitem__(self, index: int, value: T):
        index = self.__ensure_positive_index__(index)
        super().__setitem__(index, value)
        self.__wrapped_iterable[index] = value

    def append(self, obj):
        super().append(obj)
        self.__wrapped_iterable.Add(obj)
    
    def insert(self, index, obj):
        index = self.__ensure_positive_index__(index)
        super().insert(index, obj)
        self.__wrapped_iterable.Insert(index, obj)
    
    def remove(self, value):
        super().remove(value)
        self.__wrapped_iterable.Remove(value)

    def __init__(self, net_iterable):
        super().__init__([i for i in net_iterable])
        self.__wrapped_iterable = net_iterable
    
    def __ensure_positive_index__(self, index: int) -> int:
        if index < 0:
            index = len(self.__wrapped_iterable) + index
        return index
