import operator
from functools import reduce


def reduction():
    numbers=[1,2,3,4,5]
    accumulator=numbers[0]
    for item in numbers[1:]:
        accumulator=operator.add(accumulator,item)
    return accumulator


def mul(x,y):
    print("mul {} {}".format(x,y))
    return x*y


if __name__=="__main__":
    x=reduce(operator.add,[1,2,3,4,5])
    print(x)
    x=reduce(mul,[1,2,3,4,5])
    print(x)
    try:
        reduce(mul,[])
    except TypeError as ex:
        print(ex)
    
    print(reduce(operator.add,[1,2,3,4,5],0))