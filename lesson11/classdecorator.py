import sys
class CallCount:
    def __init__(self,f):
        self.f=f
        self.count=0
    def __call__(self, *args, **kwds ):
        self.count+=1
        return self.f(*args,**kwds)


@CallCount
def hello(name):
    print('Hello {}'.format(name))


if __name__=="__main__":
    print(hello(sys.argv[1]))