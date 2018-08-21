import pycom
import time

# Colors
off = 0x000000
red = 0x7f0000
green = 0x007f00
blue = 0x00007f
yellow = 0x7f7f00
class Colour:
    def blink_red():
        pycom.rgbled(red)
        time.sleep(0.2)
        pycom.rgbled(off)
        time.sleep(0.2)
        pycom.rgbled(red)
        time.sleep(0.2)
        pycom.rgbled(blue)

    def blink_blue():
        pycom.rgbled(blue)
        time.sleep(0.2)
        pycom.rgbled(off)
        time.sleep(0.2)
        pycom.rgbled(blue)
        time.sleep(0.2)
        pycom.rgbled(off)
        time.sleep(0.2)
        pycom.rgbled(blue)

    def blink_green():
        pycom.rgbled(green)
        time.sleep(0.2)
        pycom.rgbled(off)
        time.sleep(0.2)
        pycom.rgbled(green)
        time.sleep(0.2)
        pycom.rgbled(blue)

    def blink_yellow():
        pycom.rgbled(yellow)
        time.sleep(0.2)
        pycom.rgbled(off)
        time.sleep(0.2)
        pycom.rgbled(yellow)
        time.sleep(0.2)
        pycom.rgbled(blue)
