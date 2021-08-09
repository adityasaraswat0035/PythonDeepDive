import math
from traceback import print_tb

class InclinationError(Exception):
    pass


def inclination(dx,dy):
    try:
        return math.degrees(math.atan(dy/dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e

def main():
    try:
        inclination(0,5)
    except InclinationError as e:
        print(e.__traceback__)
        print_tb(e.__traceback__)

if __name__=="__main__":
    main()
    #assert False, "The condition was false."
    #assert 5 > 2, "You are in a defective universe!"
    print("Finished")