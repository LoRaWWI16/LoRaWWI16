import machine
from network import WLAN

from network import WLAN

# wlan starten mit ssid = 'Wlan Name' und auth=(net.sec, 'Passwort')

# wlan = WLAN(mode=WLAN.STA)
#
# nets = wlan.scan()
# for net in nets:
#     if net.ssid == 'OnePlus3':
#         print('Network found!')
#         wlan.connect(net.ssid, auth=(net.sec, '123456789'), timeout=5000)
#         while not wlan.isconnected():
#             machine.idle() # save power while waiting
#         print('WLAN connection succeeded!')
#         break
