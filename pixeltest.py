import time
import board
import neopixel

#hardware configuration
pin = board.D18
pixels = 30
pixel = neopixel.NeoPixel(pin, pixels, brightness=0.2)

#test
pixel[0]= (255, 0, 0)
pixel.show()
time.sleep(5)
