class Base:
    def __init__(self):
        print('Base initializer')
    
    def f(self):
        print('Base.f()')

class Sub(Base):
    def __init__(self):
        super().__init__()
        print("Sub Intializer")
    def f(self):
        print('Sub.f()')

def main():
    b=Base()
    b.f()
    s=Sub()
    s.f()

if __name__=="__main__":
    main()