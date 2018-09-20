import time
from machine import Timer, Pin, PWM
from senddata import Data

p4 = Pin('P4', mode=Pin.IN, pull=Pin.PULL_UP) # rot: Lichtschranke
p8 = Pin('P8', mode=Pin.IN, pull=Pin.PULL_UP) # orange: case
p9 = Pin('P9', mode=Pin.IN, pull=Pin.PULL_UP) # gelb: Buzzer
p10 = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP) # grün Präsenztaste Licht
p11 = Pin('P11', mode=Pin.IN, pull=Pin.PULL_UP) # blau: Präsenztaste

switch1 = 0
switch2 = 0

while True:
    if(p4.value() == 0):
        time.sleep(0.1)
        if(p4.value() == 0 and switch1 == 0):
            print(p4.id() + "Schalter1 an entprellt")
            Data.sendoutputbasket(1)
            switch1 = 1

    if(p4.value() == 1 and switch1 == 1):
        time.sleep(0.1)
        if(p4.value() == 1 and switch1 == 1):
            print(p4.id() + "Schalter1 aus entprellt")
            Data.sendoutputbasket(2)
            switch1 = 0

    if(p8.value() == 0):
        time.sleep(0.1)
        if(p8.value() == 0 and switch2 == 0):
            print(p4.id() + "Schalter2 an entprellt")
            Data.sendcase(3)
            switch2 = 1

    if(p8.value() == 1 and switch2 == 1):
        time.sleep(0.1)
        if(p8.value() == 1 and switch2 == 1):
            print(p8.id() + "Schalter2 aus entprellt")
            Data.sendcase(4)
            switch2 = 0

    if(p9.value() == 0):
        time.sleep(0.1)
        if(p9.value() == 0):
            print(" taster entprellt ")
            Data.sendbuzzer()

    if(p10.value() == 0):
        time.sleep(0.1)
        if(p10.value() == 0):
            print("taster entprellt")
            Data.sendled()
    #
    if(p11.value() == 0):
        time.sleep(0.1)
        if(p11.value() == 0):
            print("taster entprellt")
            Data.sendpresencebutton()
