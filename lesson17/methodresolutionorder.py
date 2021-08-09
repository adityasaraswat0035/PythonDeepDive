"""
when you call a method
on an object in Python, Python looks at the MRO for that object’s type. For each entry in the
MRO, starting at the front and working in order to the back, Python checks if that class has
the requested method. As soon as Python finds a class with a matching method, it uses that
method and the search stops.
That’s all that there really is to it. MRO is an ordering of a class’s inheritance graph that
Python calculates for you. 
MRO Calculation
1. A C3 MRO ensures that subclasses come before their base-classes.
2. C3 ensures that the base-class order as defined in a class definition is also preserved.
3. C3 preserves the first two qualities independent of where in an inheritance graph you
calculate the MRO. In other words, the MROs for all classes in a graph agree with
respect to relative class order.
violation of above rule
>>> class A: pass
...
>>> class B(A): pass
...
>>> class C(A): pass
...
>>> class D(B, A, C): pass
...
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, C
"""
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
    print(SortedIntList.__mro__) #(<class '__main__.SortedIntList'>, <class '__main__.IntList'>, <class '__main__.SortedList'>, <class '__main__.SimpleList'>, <class 'object'>)
    print(super(SortedList,SortedIntList)) # Here first it will find the mro of SortedIntList(Drived class) and the get a proxy containing list from SortedList ie. SimpleList and Object
    # then it will search for the method on these list to call the method when we used super
    print(super(SortedList,SortedIntList).add) #<function SimpleList.add at 0x000001C12C2FC820>
    try:
        print(super(SortedList, SortedIntList).add(4))
    except TypeError as ex:
        print(str(ex)) #add() missing 1 required positional argument: 'item
        #This failed because our proxy is bound to a class, not an instance, so we can’t invoke it. if we used the proxy to look up a staticmethod or classmethod, however, we could invoke it directly.
    super(SortedIntList, SortedIntList)._validate(5)
    #super(SortedIntList, SortedIntList)._validate('hello') #TypeError: IntList only supports integer values.
    #super(int, IntList) #Python will raise an exception if the second argument is not a subclass of thefirs
    """Instance-bound super proxies work very much like class-bound proxies, but instead of
    binding to a class object they bind to an instance. To create an instance-bound proxy, call
    super() like this:
    super(class, instance-of-class)
    Here, the first argument must be a class object, and the second argument must be an instance
    of that class or any class derived from it.
    The behavior of the super proxy in this case is like this:
    1. Python finds the MRO for the type of the second argument.
    2. Then Python finds the location of the first argument to super() in that MRO;
    remember that the instance must be derived from the class, so the class must be in
    the MRO.

    """
    sil = SortedIntList([5, 15, 10])
    print(super(SortedList, sil)) #The proxy is bound to aSortedIntList and will start method resolution from SortedIntList’s MRO at the entry after SortedList
    super(SortedList,sil).add(20)
    print(sil._items)
    """
    It turns out that you can call super() in a method with no arguments, and Python will sort out the arguments for you.
    If you’re in an instance method:
        callsuper() without arguments, that’s the same as callingsuper() with the method’s class as the first argument andself as the second.
    If you’re in an Class method:   
        callingsuper() with the method’s class as the first argument and the classmethods first argument (that is, the “class” argument) as the second. 
    """


if __name__=="__main__":
    """
    Super():
        Given a method resolution order and a class C in that MRO,super() gives you 
        an object which resolves methods using only the part of the MRO which comes
        after C.
    super() doesn’t work with the base-classes of a class, but instead it works
        with the MRO of the type of the object on which a method was originally invoked
        Super call returne a super proxy object and when we call a method on it, it will route the call to correct method imple if exsts based on MRO

    Two Type if Proxy:
    bound and unbound. Bound proxies, as the name suggests, are bound to instances or class objects. On the other hand, unbound proxies aren’t connected to any instance
    To create a class-bound proxy, you use this form:
        super(base-class, derived-class)
    you invoke a method on the proxy, 
    1. Python finds the MRO forderived-class
    2. It then finds base-class in that MRO
    3. It takes everything after base-class in the MRO and finds the first class in that sequence with a method name matching the request.
    """
    main()