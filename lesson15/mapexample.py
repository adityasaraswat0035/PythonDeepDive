def TraceV1(f):
    def wrap(item):
        print("called for {}".format(item))
        rslt= f(item)
        print("called done for item {}".format(item))
        return rslt
    return wrap
class Trace:
    def __call__(self, *args, **kwds):
        def wrap(item):
            print("calling ",args)
            return args[0](item)
        return wrap
def combine(size,color,animal):
    return '{} {} {}'.format(size,color,animal)


if __name__=="__main__":
    g=map(ord,'The quick brown fox')
    print(g)
    print(list(g))
    print(isinstance(g,map))
    m=map(TraceV1(ord),'The quick brown fox')
    print(list(m))
    m=map(Trace()(ord),'The quick brown fox')
    print(next(m))
    print(next(m))
    print(next(m))
    for i in m:
        print(i)
    sizes = ['small', 'medium', 'large']
    colors = ['lavender', 'teal', 'burnt orange',]
    animals = ['koala', 'platypus', 'salamander']
    print(list(map(combine,sizes,colors,animals))) #To account for this,map()will terminate as soon as any of the input sequences is exhausted. 
    print([str(i) for i in range(5)])
    print(list(map(str,range(5))))