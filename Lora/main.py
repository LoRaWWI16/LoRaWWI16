from machine import RTC
import time
import socket
from ds3231 import DS3231
from colour import Colour
from senddata import Data
import pycom
from machine import Timer, Pin, PWM

#Get the RTC
ertc = DS3231(0, (Pin.module.P21, Pin.module.P20))

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
# s.setblocking(True)


# make the socket non-blocking
# (because if there's no data received it will block forever...)
# s.setblocking(False)

# split timestamp
# timestamp = str(ertc.get_time()).replace('(',' ').replace(')',' ').replace(',',' ').split(" ")

# print(ertc.get_time())
#
# timestamp = ''.join(listtimestamp)
#
timestamp = Data.get_timestamp()
s.send(timestamp)
print(timestamp)


# byte_y=y.encode('utf-8').split(",")
# print(byte_y)

# send timestamp data
# s.send(y)
# s.send(byte_y)


# for i in range(5):
#     s.bind(2)
#     pkt = i + 1
#     print('Sending:', pkt)
#
#     s.send(pkt)
#     Colour.blink_green()
#     time.sleep(4)
#     rx, port = s.recvfrom(256)
#     if rx:
#         print("Received {}, on Port: {}".format(rx,port))
#         Colour.blink_yellow()
#     time.sleep(6)
