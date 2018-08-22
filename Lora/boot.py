import pycom
import time
import binascii
from colour import Colour
from network import LoRa

# Turn Wifi off
pycom.wifi_on_boot(False)

# Turn off hearbeat LED
pycom.heartbeat(False)
# Turn Red LED on
pycom.rgbled(Colour.off())

# LoRa region will be set when you update the firmware
# it does not need to be explicitly stated
lora = LoRa(mode=LoRa.LORAWAN)

# OTAA authentication parameters
app_eui = binascii.unhexlify('70B3D57ED0010C13')
app_key = binascii.unhexlify('B643A4B467C9C31D7F586DE8978E4482')

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0, dr=0)
pycom.rgbled(Colour.red())
# wait until the module has joined the network
while not lora.has_joined():
    pass #no delays, just keeps looping until .has_joined() returns true
print('Joined!!')
pycom.rgbled(Colour.blue())
time.sleep(0.5)
