from machine import Pin
#import time

class Pins:
    def pin4(): # rot: Lichtschranke
        p4 = Pin('P4', mode=Pin.IN, pull=Pin.PULL_UP)
        p4_Value = p4.value()
        return p4, p4_Value

    def p8(): # orange: case
        p8 = Pin('P8', mode=Pin.IN, pull=Pin.PULL_UP)
        return p8.value()

    def pin9(): # gelb: Buzzer
        p9 = Pin('P9', mode=Pin.IN, pull=Pin.PULL_UP)
        p9_Value = p9.value()
        return p9.value()

    def p10(): # grün: Licht Prösenztaste
        p10 = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
        return p10.value()

    def p11(): # blau: Präsenztaste
        p11 = Pin('P11', mode=Pin.IN, pull=Pin.PULL_UP)
        return p11.value()
