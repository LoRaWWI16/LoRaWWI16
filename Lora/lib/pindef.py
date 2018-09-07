from machine import Pin
#import time

class Pins:
    def pin4(): # rot: Lichtschranke
        p4 = Pin('P4', mode=Pin.IN, pull=Pin.PULL_UP)
        p4_Value = p4.value()
        return p4, p4_Value

    def pin8(): # gelb: Buzzer
        p8 = Pin('P8', mode=Pin.IN, pull=Pin.PULL_UP)
        p8_Value = p8.value()
        return p8.value()

    def p9(): # blau: Präsenztaste
        p9 = Pin('P9', mode=Pin.IN, pull=Pin.PULL_UP)
        return p9.value()

    def p10(): # grün: Licht Prösenztaste
        p10 = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
        return p10.value()

    def p11(): # orange: case
        p11 = Pin('P11', mode=Pin.IN, pull=Pin.PULL_UP)
        return p11.value()
