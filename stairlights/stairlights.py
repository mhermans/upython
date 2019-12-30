import time
import board
from analogio import AnalogIn
import neopixel

# PIR sensor on PIN A1
a_in_pir = AnalogIn(board.A1)

# Light sensor on PIN A2
a_in_light = AnalogIn(board.A2)

# Neopixel strip on PIN D5
pixel_pin = board.D5

LIGHT_CUTOFF = 1.0     # value 0-100
MOVEMENT_CUTOFF = 95.0 # value 0-100
LIGHT_ON_DELAY = 10    # time lights stays on in seconds


num_pixels = 30
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels,
    brightness=0.3, auto_write=False,
    pixel_order=ORDER)

def is_dark(light_sensor, cutoff=1.0):
    # analog pin max value is 65535 => ~1-100
    # [~4 is ambient room light, ~96 directly under lamp]
    light_pct = (light_sensor.value / 65535)*100
    if light_pct < cutoff:
        return(True)
    else:
        return(False)

def is_movement(pir_sensor, cutoff=95):
    #  analog pin max value is 65535 => range [~0.2 - 100]
    #  0.1-0.2 is no movement, 98-99 is movement
    movement_pct = (pir_sensor.value / 65535)*100
    print(movement_pct)
    if movement_pct > cutoff:
        return(True)
    else:
        return(False)


TS_BOOT = time.monotonic()
TS_LAST_MOVEMENT = 0

while True:
    if not is_dark(a_in_light, LIGHT_CUTOFF):
        # ambient light present -> turn of pixels
        pixels.fill((0, 0, 0))
        pixels.show()

    else:
        # dark and movement
        if is_movement(a_in_pir, MOVEMENT_CUTOFF) and not TS_LAST_MOVEMENT:
            # first movement -> activate pixels and set timestamp
            TS_LAST_MOVEMENT = time.monotonic()
            pixels.fill((255, 0, 0))
            pixels.show()
            
        elif is_movement(a_in_pir, MOVEMENT_CUTOFF) and  ( (time.monotonic() - TS_LAST_MOVEMENT) < LIGHT_ON_DELAY ):    
            # again movement -> reset timestamp
            TS_LAST_MOVEMENT = time.monotonic()
            pixels.fill((255, 0, 0))
            pixels.show()
            
        elif (time.monotonic() - TS_LAST_MOVEMENT) < LIGHT_ON_DELAY:
            pixels.fill((0, 0, 255))
            pixels.show()
        
        # dark and no movement
        else:
            TS_LAST_MOVEMENT = 0
            pixels.fill((0, 255, 0))
            pixels.show()
