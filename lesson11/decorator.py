def escape_unicode(f):
    def wrap(*args,**kwargs):
        x=f(*args,**kwargs)
        return ascii(x)
    return wrap


@escape_unicode
def northen_city():
    return 'Tromsø'

if __name__=="__main__":
    x=northen_city
    print(type(x))
    print(x())
