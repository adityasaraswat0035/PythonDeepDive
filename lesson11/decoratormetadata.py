from functools import wraps

def noop(f):
    
    @wraps(f)
    def noop_wrapper(*args,**kwargs):
        f(*args,**kwargs)
    # return noop_wrapper
    #Manual way of persisting metadata
    # noop_wrapper.__name__=f.__name__
    # noop_wrapper.__doc__=f.__doc__
    # return noop_wrapper
    return noop_wrapper



def hello():
    "Print a well-known message."
    print('Hello, world!')

print(hello.__name__)
print(hello.__doc__)


@noop
def helloV2():
    "Print a well-known message."
    print('Hello, world!')
    
print(helloV2.__name__)
print(helloV2.__doc__)