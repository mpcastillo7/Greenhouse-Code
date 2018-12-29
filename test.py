"""some test functions for stuff"""

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
    for i in range(0, len(lst)-1):
        lst[i] = 



if __name__ == "__main__":
    import doctest
    doctest.testmod()
