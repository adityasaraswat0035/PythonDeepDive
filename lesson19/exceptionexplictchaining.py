import math

class InclinationError(Exception):
    pass


def inclination(dx,dy):
    try:
        return math.degrees(math.atan(dy/dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e


def main():
    try:
        print(inclination(3, 5))
        print(inclination(0, 5))
    except InclinationError as e:
        print(e)
        print(e.__cause__)
        print(e.__context__)

if __name__=="__main__":
    main()