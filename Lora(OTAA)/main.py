from machine import RTC
from network import LoRa
import time
import socket
import binascii
from ds3231 import DS3231
from colour import Colour
import pycom
from machine import Timer, Pin, PWM


ertc = DS3231(0, (Pin.module.P21, Pin.module.P20))

# Colors
off = 0x000000
red = 0x7f0000
green = 0x007f00
blue = 0x00007f
yellow = 0x7f7f00

# LoRa region will be set when you update the firmware
# it does not need to be explicitly stated
lora = LoRa(mode=LoRa.LORAWAN)

# OTAA authentication parameters
app_eui = binascii.unhexlify('70B3D57ED0010C13')
app_key = binascii.unhexlify('B643A4B467C9C31D7F586DE8978E4482')

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0, dr=0)
pycom.rgbled(red)
# wait until the module has joined the network
while not lora.has_joined():
    pycom.rgbled(red)
     #pass no delays, just keeps looping until .has_joined() returns true
print('Joined!!')
pycom.rgbled(blue)
time.sleep(0.5)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
s.send(bytes([0x01, 0x02, 0x03]))

Colour.blink_green()

# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)

#RTC init
rtc = RTC()
rtc.init((2018,8,9,14,53,0,0,0))
print(rtc.now())

# split timestamp
y = str(rtc.now()[0])
print(y)
byte_y=y.encode('utf-8')
print(byte_y)

# send timestamp data
s.send(y)
s.send(byte_y)

for i in range(5):
    print(ertc.get_time(True))
    pkt = b'PKT #' + bytes([i])
    print('Sending:', pkt)
    s.send(pkt)
    Colour.blink_green()
    time.sleep(4)
    rx, port = s.recvfrom(256)
    if rx:
        print("Received {}, on Port: {}".format(rx,port))
        Colour.blink_yellow()
    time.sleep(6)
