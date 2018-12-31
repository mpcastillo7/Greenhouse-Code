#functions useful for later stuff

#libraries used
import Adafruit_DHT
from matplotlib import pyplot as plt
from time import sleep

#generic functions
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

#specific functions
read = Adafruit_DHT.read_retry
def readDHT(time, pin, temps=[], humid=[], t=[], frequency=4):
    """
    reads the Adafruit_DHT over some period of time expressed in integer minutes
    with an integer frequency of times/minute and returns the measured values in
    lists
    """
    if frequency > 30:
        raise ValueError("Too frequent, sensor will be damaged")
    if not pin:
        raise ValueError("No pin specified")
    sensor = Adafruit_DHT.DHT22
    minutes = int(frequency*mins)
    for i in range(0, minutes):
        humidity, temperature = read(sensor, pin)
        humid += [humidity]
        temps += [temperature]
        t += [i]
        sleep(int(mins))
    return [temps, humid, t]

#originally built to go with readDHT
def valuePlot(values, t, graph):
    averagedValues = averagedList(values)
    averagedTime = averagedList(t)
    graph.plot(t, humidity, label="data")
    graph.plot(averagedTime, averagedValues, label="average")
    graph.show()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
