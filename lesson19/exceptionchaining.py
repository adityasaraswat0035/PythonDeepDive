import math
import sys
import io


class TriangleError(Exception):
    def __init__(self, text,sides) -> None:
        super().__init__(text)
        self._sides=tuple(sides)
    @property
    def sides(self):
        return self._sides
    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)
    def __repr__(self):
        return "TriangleError({!r}, {!r}".format(self.args[0], self._sides)


def triangle_area(a,b,c):
    sides=sorted((a,b,c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle",sides=sides)
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a

def main():
    try:
        a=triangle_area(3,4,10)
    except TriangleError as e:
        try:
            print(e,file=sys.stdin)
        except io.UnsupportedOperation as f:
            print(e) #'Illegal triangle' for sides (3, 4, 10)
            print(f) #not writable
            print(f.__context__ ) #'Illegal triangle' for sides (3, 4, 10)
            print(f.__context__ is e)

if __name__=="__main__":
    main()