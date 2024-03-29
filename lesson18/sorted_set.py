from collections.abc import Sequence
from bisect import bisect_left
from itertools import chain
class SortedSet(Sequence):
    def __init__(self,items=None) :
        self._items=sorted(set(items)) if items is not None else []
    def __contains__(self,item):
        return item in self._items # item in self._items._contains__(item) don't do like this

        # index = bisect_left(self._items, item)
        # return (index != len(self._items)) and self._items[index] == item

        # try:
        #     self.index(item)
        #     return True
        # except ValueError:
        #     return False
    Sequence
    def __len__(self):
        return len(self._items)
    def __iter__(self):
        # return iter(self._items)
        # for item in self._items:
        #     yield item
        yield from self._items #3.3
    
    def __getitem__(self,index):
        result=self._items[index]
        return SortedSet((result)) if isinstance(index,slice) else result
        # return self._items[index]
    def __repr__(self):
        return 'SortedSet({})'.format(repr(self._items) if self._items else '')
    def __eq__(self, rhs):
        if not isinstance(rhs,SortedSet):
            return NotImplemented
        return self._items==rhs._items   
    def count(self, item):
        index=bisect_left(self._items,item)
        found=(index!=len(self._items)) and (self._items[index]==item)
        return int(found)
    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and self._items[index] == item:
            return index
        raise ValueError("{} not found".format(repr(item)))
    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))
    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()
