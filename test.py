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

read = Adafruit_DHT.read_retry
def readFor(mins, temps=[], humid=[], t=[]):
    minutes = 4*mins
    for i in range(0, minutes):
        humidity, temperature = read(sensor, pin)
        humid += [humidity]
        temps += [temperature]
        t += [i]
        led.off()
        sleep(15)
        led.on()
    return [temps, humid, t]

def hPlot(humidity, t):
    averagedHumidity = averagedList(humidity)
    averagedTime = averagedList(t)
    plt.plot(t, humidity, label="data")
    plt.plot(averagedTime, averagedHumidity, label="average")
    plt.show()
