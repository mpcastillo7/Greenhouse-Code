"""
Test code for the DHT22 (Temperature/Humidity Sensor)
"""

#libaries
import AdafruitDHT
from matplotlib import pyplot as plt
from gpiozero import LED

#hardware
sensor = AdafruitDHT.DHT22
