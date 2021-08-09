def median(iterable):
    """Obtain the central value of a series.
    Sorts the iterable and returns the middle value if there is an even
    number of elements, or the arithmetic mean of the middle two elements
    if there is an even number of elements.
    Args:
        iterable: A series of orderable items.
    Returns:
        The median value.
"""
    items = sorted(iterable)
    if len(items)==0:
        raise ValueError("Medium() arg is an empty series")
    median_index = (len(items) - 1) // 2
    if len(items) % 2 != 0:
        return items[median_index]
    return (items[median_index] + items[median_index + 1]) / 2.0


def main():
    print(median([5, 2, 1, 4, 3]))
    print(median([5, 2, 1, 4, 3, 6]))
    try:
        print(median([]))
    except ValueError as e:
        print("Payload",e.args) #Payload ('Medium() arg is an empty series',)
        print(str(e)) #Another way to retrive Medium() arg is an empty series
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print("encoding",e.encoding)
        print("reason",e.reason)
        print('object',e.object)
        print('start',e.start)
        print('end',e.end)

if __name__=="__main__":
    main()

