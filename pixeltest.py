import time
import board
import neopixel

#hardware configuration
pixel_pin = board.D18
num_pixels = 30
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

#test
pixels[0] = (255, 0, 0)
