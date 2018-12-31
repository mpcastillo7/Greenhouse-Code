"""
Test code for the DHT22 (Temperature/Humidity Sensor) to establish sense of
accuracy
"""

#libaries
from gpiozero import LED
from functions import *
from matplotlib import pyplot as graph

#hardware configuration
led = LED(22)
pin = 4
led.on() #indicates things good

#graph settings
graph.xlabel("Number of Intervals")
graph.ylabel("Humidity Values (%)")

#read DHT sensor for 2 minutes, 6 times a minute (every 10s) + graph data
results = readDHT(2, pin, frequency=6)
time = results[2]
temperature = results[0]
humidity = results[1]
valuePlot(humidity, time, graph)
