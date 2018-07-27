from network import LoRa
from machine import RTC
import binascii
import struct
import socket


lora = LoRa(mode=LoRa.LORAWAN)

dev_addr = struct.unpack(">l", binascii.unhexlify('26011E26'))[0]
nwk_swkey = binascii.unhexlify('C3E8DC4C040628F2EA2D93BCA7FDF6F5')
app_swkey = binascii.unhexlify('9FED3EA46F7A9F26A1352B0824175672')

lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)

s.send(bytes([1, 2, 3]))

