"""
Test code for the DHT22 (Temperature/Humidity Sensor)
"""

#libaries
import Adafruit_DHT
from matplotlib import pyplot as plt
from gpiozero import LED
import time
import functions

#hardware configuration
led = LED(22)
sensor = Adafruit_DHT.DHT22
pin = 4
led.on()

#graph settings
plt.xlabel("Number of 15s Intervals")
plt.ylabel("Humidity Values (%)")

def hreadFor(mins, humidityVals=[], tempVals=[], t=[]):
    minutes = 4*mins
    return humidityVals, tempVals, t


read = AdafruitDHT.read_retry
