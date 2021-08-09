from pprint import pprint as pp
if __name__=="__main__":
    l=[i*2 for i in range(10)]
    print(l)
    d={i:i*2 for i in range(10)}
    print(d)
    s={i for i in range(10)}
    print(s)
    g=(i for i in range(10))
    print(g)
    pp([(x,y) for x in range(10) for y in range(x)])
    values=[x/(x-y) 
            for x in range(100) 
                if x>50 
                    for y in range(100) 
                        if x-y!=0]
    print(values)
    vals=[[y*3 for y in range(x)] for x in range(10)]
    print(vals)
    print({x*y for x in range(10) for y in range(10)})
    g=(x*y for x in range(10) for y in range(10))
    print(type(g))
    print(list(g))