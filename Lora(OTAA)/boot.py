import pycom

# Turn Wifi off
pycom.wifi_on_boot(False)

# Turn off hearbeat LED
pycom.heartbeat(False)
