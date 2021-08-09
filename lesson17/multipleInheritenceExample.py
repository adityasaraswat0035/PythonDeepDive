class SimpleList:
    def __init__(self,items):
        self._items=items
    def add(self,item):
        self._items.append(item)
    def __getitem__(self,index):
        return self._items[index]
    def sort(self):
        self._items.sort()
    def __len__(self):
        return len(self._items)
    def __repr__(self):
        return "SimpleList ({!r})".format(self._items)
    
class SortedList(SimpleList):
    def __init__(self, items):
        super().__init__(items)
        self.sort()
    def add(self,item):
        super().add(item)
        self.sort()
    def __repr__(self):
        return "SortedList ({!r})".format(self._items)

class IntList(SimpleList):
    def __init__(self,items=()):
        for x in items:
            self._validate(x)
        super().__init__(items)
    

    def add(self,item):
        self._validate(item)
        super().add(item)
    
    def __repr__(self):
        return "IntList({!r})".format(list(self))
    

    @staticmethod
    def _validate(item):
        if not isinstance(item,int):
            raise TypeError('IntList only supports integer values.')

class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))


def main():
    sil = SortedIntList([42, 23, 2])
    print(sil)
    print(sil.__base__)


if __name__=="__main__":
    sil = SortedIntList([42, 23, 2])
    print(sil)
    print(SortedIntList.__bases__)
    print(SortedIntList.__mro__)
    print(SimpleList.__bases__)
    print(SimpleList.__mro__)