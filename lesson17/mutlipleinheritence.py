class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

class Base1:
    def __init__(self):
        print('Base1.__init__')
class Base2:
    def __init__(self):
        print('Base2.__init__')
class Sub(Base1, Base2):
    pass

class NoBaseClass:pass
s = Sub()
print(Sub.__bases__)
print(Sub.__mro__)
print(NoBaseClass.__mro__) #(<class '__main__.NoBaseClass'>, <class 'object'>)
print(NoBaseClass.__bases__)#(<class 'object'>,)
print(int.__bases__) #(<class 'object'>,)
print(dir(object))