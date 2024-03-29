import sys

def sqrt(x):
    """Compute square roots using the method of Heron of Alexandria.
    Args:
        x: The number for which the square root is to be computed.
    Returns:
        The square root of x.
"""
    if x < 0:
        raise ValueError("Cannot compute square root of negative number {}".format(x))
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x / guess) / 2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as ex:
        print(ex,file=sys.stderr)
    print("Program execution continues normally here.")

if __name__ == '__main__':
    main()
