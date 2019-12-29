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
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels,
    brightness=0.3, auto_write=False,
    pixel_order=ORDER)

def is_dark(light_sensor, cutoff=0.3):
    # analog pin max value is 65535
    light_pct = (light_sensor.value / 65535)*100
    if light_pct < cutoff:
        return(True)
    else:
        return(False)

def is_movement(pir_sensor, cutoff=0.9):
    #  analog pin max value is 65535
    movement_pct = (pir_sensor.value / 65535)*100
    if movement_pct > cutoff:
        return(True)
    else:
        return(False)

while True:
    if is_dark(a_in_light, 0.30):
        if is_movement(a_in_pir, 0.90):
            pixels.fill((255, 0, 0))
            pixels.show()
        else:
            pixels.fill((0, 255, 0))
            pixels.show()
    else:
        pixels.fill((0, 0, 255))
        pixels.show()

    #print(is_movement(a_in_pir, 0.90))
    #print(is_dark(a_in_light, 0.30))
    #time.sleep(0.1)
