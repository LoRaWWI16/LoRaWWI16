import pycom

# Turn Wifi off
pycom.wifi_on_boot(False)

# Turn off hearbeat LED
pycom.heartbeat(False)
# Turn Red LED on
pycom.rgbled(0x7f0000)
