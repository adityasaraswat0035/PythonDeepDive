import sys
def escape_unicode(f):
    print("calling escape_unicode")
    def wrap(*args,**kwargs):
        x=f(*args,**kwargs)
        return x.encode('unicode-escape').decode('ascii')
    return wrap

class Trace:
    def __init__(self):
        self.enabled=True
    def __call__(self,f):
        print("calling Trace")
        def wrap(*args,**kwargs):
            if self.enabled:
                print("Calling {}".format(f))
            return f(*args,**kwargs)
        return wrap
        
tracer = Trace()

class IslandMaker:
    def __init__(self,suffix):
        self.suffix=suffix
    
    @tracer
    def make_island(self,name):
        return name+self.suffix 




@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + 'øy'





if __name__=="__main__":
    print(norwegian_island_maker(sys.argv[1]))
