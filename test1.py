import board
import neopixel

#hardware
pin = board.D18
pixel = neopixel.NeoPixel(pin, 30, brightness=0.2)

#environment start
pixel.fill((255, 0, 255))
