"""
Test code for the DHT22 (Temperature/Humidity Sensor)
"""

#libaries
from gpiozero import LED
import functions

#hardware configuration
led = LED(22)
pin = 4
led.on()

#graph settings
plt.xlabel("Number of 15s Intervals")
plt.ylabel("Humidity Values (%)")
