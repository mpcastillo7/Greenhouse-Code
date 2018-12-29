"""some test functions for stuff"""

def average(a, b):
    return a/2 + b/2

def splice(lst1, lst2):
    """
    combines two lists into one list of ordered pairs
    >>> lst1 = [1, 1, 1, 1]
    >>> lst2 = [2, 2, 2, 2]
    >>> spliced = splice(lst1, lst2)
    >>> spliced
    [(1, 2), (1, 2), (1, 2), (1, 2)]
    >>> spliced2 = splice(lst2, lst1)
    >>> spliced2
    [(2, 1), (2, 1), (2, 1), (2, 1)]

    >>> lst1 = [1, 1]
    >>> lst2 = [1]
    >>> splice(lst1, lst2)
    Traceback (most recent call last):
    ...
    ValueError: Lists are not the same size
    """
    if len(lst1) != len(lst2):
        raise ValueError("Lists are not the same size")
    return list(zip(lst1, lst2))

def averagedList(lst):
    """
    reduces the list to averaged intermediate values
    >>> lst = [1, 1, 1]
    >>> averagedList(lst)
    [1.0, 1.0]
    >>> averagedList([1, 2, 3, 4])
    [1.5, 2.5, 3.5]
    """
    newLst = []
    for i in range(0, len(lst)-1):
        newLst += [average(lst[i], lst[i+1])]
    return newLst



if __name__ == "__main__":
    import doctest
    doctest.testmod()
