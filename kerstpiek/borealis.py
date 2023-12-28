import time
import board
import neopixel
import random
import adafruit_fancyled.adafruit_fancyled as fancy

pixel_pin = board.D7
num_pixels = 16

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

ring = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

palette = [
    #fancy.CRGB(186, 37, 179), # dark violet => te dominant
    fancy.CRGB(228, 252, 36), # bright yellow
    fancy.CRGB(20,232,30),  # light green
    fancy.CRGB(20,232,30),  # light green
    fancy.CRGB(20,232,30),  # light green
    fancy.CRGB(124, 252, 36), # greenish
    fancy.CRGB(0,234,141),  # light blue
    fancy.CRGB(0,234,141),  # light blue
    fancy.CRGB(63, 103, 86), # dark green
    fancy.CRGB(63, 103, 86), # dark green
    fancy.CRGB(0,0,0) # Black
    ]          
 
offset = 0  # Position offset into palette to make it "spin"
random_brightness = 0.25

while True:
    for i in range(num_pixels):
        color = fancy.palette_lookup(palette, offset + i / num_pixels)
        random_brightness = abs(random_brightness + random.randint(-6, 6)/1000)
        print(random_brightness)
        color = fancy.gamma_adjust(color, brightness = random_brightness )
        ring[i] = color.pack()
        
    ring.show()
 
    offset += 0.013  # Bigger number = faster spin
