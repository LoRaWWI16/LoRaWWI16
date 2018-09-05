from machine import RTC
import time
import socket
from ds3231 import DS3231
from colour import Colour
import pycom
from machine import Timer, Pin, PWM
from pindef import Pins
from senddata import Data

# test = None
# def pin_handler(arg):
#     x = 1
#     if (x == 1):
#         print("got an interrupt in pin P4")
#         time.sleep(1)
#         test = True
#         x=0
#     else:
#         print("nein")
#p = Pins()
#p4 = p.p4
#p4 = Pins.pin4()[0]
p4 = Pin('P4', mode=Pin.IN, pull=Pin.PULL_UP)#lichtschranke
#p4.callback(Pin.IRQ_RISING, pin_handler, test)
#time.sleep(60)
p8 = Pin('P8', mode=Pin.IN, pull=Pin.PULL_UP) # gelb Buzzer
p9 = Pin('P9', mode=Pin.IN, pull=Pin.PULL_UP) #blau Präsenztaste
p10 = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)# grün PTaste Licht
p11 = Pin('P11', mode=Pin.IN, pull=Pin.PULL_UP)#case

def wait_pin_change(pin):
    print("test")
    cur_value=pin.value()
    active = 0
    while active < 20:
        if pin.value() != cur_value:
            active += 1
            print(active)
            Data.sendlightsensor()
        else:
            active = 0
            print("not active")
        time.sleep(1)

for i in range(50):
    print("sende")
    print(wait_pin_change(p4))

    # print(wait_pin_change(p8))
    # print(wait_pin_change(p9))
    # print(wait_pin_change(p10))
    # print(wait_pin_change(p11))


    time.sleep(1)
