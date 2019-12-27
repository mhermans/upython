import time
import board
from analogio import AnalogIn
import neopixel

# PIR sensor on PIN A1
a_in_pir = AnalogIn(board.A1)

# Light sensor on PIN A2
a_in_light = AnalogIn(board.A2)

# Neopixel strip on PIN D12
pixel_pin = board.D12

num_pixels = 30
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)

while True:
    print(a_in_light.value)
    print(a_in_pir.value)
    
    if a_in_light.value < 1000: 
        if a_in_pir.value < 1000:
            pixels.fill((0, 255, 0))
            pixels.show()
        if a_in_pir.value > 1000:
            pixels.fill((255, 0, 0))
            pixels.show()        
    time.sleep(0.1)
