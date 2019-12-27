# CircuitPython AnalogIn Demo
import time
import board
from analogio import AnalogIn
import neopixel

a_in = AnalogIn(board.A1)
pixel_pin = board.D12

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)

def get_voltage(pin):
    return (pin.value * 3.3) / 65536
     
while True:
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)
    
    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)
    
#    if a_in.value > 1000:
#        led[0] = (255, 0, 0)
#    if a_in.value < 1000:
#        led[0] = (0, 255, 0)
#    time.sleep(1)
