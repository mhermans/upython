# Setup mu-editor

download: https://codewith.mu/en/download
source ~/lib/virtualenvs/espenv/bin/activate
pip3 install mu-editor
sudo adduser mhermans uucp
mu-editor


download ItsyBitsy M0 Express CircuitPython 4.1.2 firmware

https://circuitpython.org/board/itsybitsy_m0_express/
https://github.com/adafruit/circuitpython/releases/download/4.1.2/adafruit-circuitpython-itsybitsy_m0_express-en_US-4.1.2.uf2

double-tap reset button, drag UF2 firmware
https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython


# corrupted FS after unplugging

https://learn.adafruit.com/introducing-itsy-bitsy-m0/troubleshooting

screen /dev/ttyACM0 115200

Adafruit CircuitPython 4.1.2 on 2019-12-18; Adafruit ItsyBitsy M0 Express with samd21g18

    >>> import storage
    >>> storage.erase_filesystem()

# Add libraries

https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries

https://circuitpython.org/libraries

version for 4.x https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20191223/adafruit-circuitpython-bundle-4.x-mpy-20191223.zip 

cp lib/neopixel.py to lib/
cp examples/neopixel_simpletest.py to /main.py


# R/G neopixel strip
import time
import board
import neopixel

pixel_pin = board.D12
num_pixels = 30
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False,
                           pixel_order=ORDER)

while True:
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)

    


# Example neopixel

import time
import board
import neopixel


# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
#pixel_pin = board.NEOPIXEL
pixel_pin = board.D13

# On a Raspberry pi, use this instead, not all pins are supported
#pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step

