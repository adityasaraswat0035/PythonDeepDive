from math import exp
from random import randrange

def main():
    number=randrange(100)
    while True:
        try:
            guess=int(input("?"))
        except ValueError:
            continue
        if guess==number:
                print("You Win!")
                break    

def lookups():
    s=[1,4,6]
    try:
            item=s[5]
    except IndexError:
        print("Handled IndexErrorr")
    d=dict(a=65,b=66,c=67)
    try:
        value = d['x']
    except KeyError:
        print("Handled Expection")


def lookupsV1():
    s=[1,4,6]
    try:
            item=s[5]
    except LookupError:
        print("Handled LookupError")
    d=dict(a=65,b=66,c=67)
    try:
        value = d['x']
    except LookupError:
        print("Handled LookupError")


if __name__=="__main__":
    #main()
    print(IndexError.__mro__) #<class 'IndexError'>, <class 'LookupError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
    print(KeyError.__mro__) #(<class 'KeyError'>, <class 'LookupError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
    lookups()
    lookupsV1()