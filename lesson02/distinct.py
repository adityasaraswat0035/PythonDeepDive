def distinct(iterable):
    """Return unique item by eliminating duplicates
        Args:
            iterable: The source of items.
        Yields:
            unique element in order from iterable
    """
    seen=set()
    for item in iterable:
        if item in seen:
            continue
        seen.add(item)
        yield item
       
def run_distinct():
    items=[5,7,7,6,5,5]
    for item in distinct(items):
        print(item)

if __name__=="__main__":
    run_distinct()