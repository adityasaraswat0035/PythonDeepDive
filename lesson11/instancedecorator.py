class Trace:
    def __init__(self):
        self._enabled=True
    
    def __call__(self,f):
        def wrap(*args,**kwargs):
            if self._enabled:
                print('Calling {}'.format(f))
            return f(*args,**kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]
