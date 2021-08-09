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

    


def main():
    sl=SortedList([4,3,78,1])
    print(sl)
    sl.add(-42)
    print(sl)
    sl.add(7)
    print(sl)
    il=IntList([1,2,3,4])
    il.add(19)
    print(il)
    #il.add('5')
    print(issubclass(IntList,SimpleList))



if __name__=="__main__":
    main()
    s=SortedList([])
    print(isinstance(s,SortedList))
    print(isinstance(s,SimpleList))
    print(isinstance(s,(int,float)))
    print(issubclass(SortedList,(SimpleList,)))
    print(issubclass(SimpleList,(SortedList,)))