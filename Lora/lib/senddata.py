from machine import RTC
import time
import socket
from ds3231 import DS3231
from colour import Colour
import pycom
from machine import Timer, Pin, PWM

#Get the RTC
ertc = DS3231(0, (Pin.module.P21, Pin.module.P20))

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

def get_timestamp():
    timestamp = ertc.get_time()
    timestamplist = ''
    for i in timestamp:
        x = 0
        if i < 10:
            timestamplist = timestamplist + str("{0:0>2}".format(i))

        else:
            timestamplist = timestamplist + str(i)

    return(timestamplist)

class Data:
    def get_timestamp():
        timestamp = get_timestamp()

        return timestamp

    def sendoutputbasket():
        timestamp = get_timestamp()
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        s.setblocking(True)

        ######################
        #  Data
        #######################
        s.bind(1)
        s.send(timestamp)
        time.sleep(5)

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)

    def sendbuzzer():
        timestamp = get_timestamp()
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        # s.setblocking(True)

        ######################
        #  Data
        #######################
        s.bind(2)
        s.send(timestamp)
        time.sleep(5)

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        # s.setblocking(False)

    def sendpresencebutton():
        timestamp = get_timestamp()
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        s.setblocking(True)

        ######################
        #  Data
        #######################
        s.bind(3)
        s.send(timestamp)
        time.sleep(5)

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)

    def sendlightsensor():
        timestamp = get_timestamp()
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        s.setblocking(True)

        ######################
        #  Data
        #######################
        s.bind(4)
        s.send(timestamp)
        time.sleep(5)

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)

    def sendcase():
        timestamp = get_timestamp()
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        s.setblocking(True)

        ######################
        #  Data
        #######################
        s.bind(5)
        s.send(timestamp)
        time.sleep(5)

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)
