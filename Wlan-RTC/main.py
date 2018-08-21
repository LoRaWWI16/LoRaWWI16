import pycom
import machine
from machine import Timer, Pin, PWM
#from helpers import *
import utime
from ds3231 import DS3231
from network import WLAN

pycom.heartbeat(False)

VERSION = '0.7.0'

ertc = DS3231(0, (Pin.module.P21, Pin.module.P20))
print(ertc.get_time())
# print(ertc.save_time())

######################
#  External RTC
#######################

# def setup_rtc():
#     rtc = machine.RTC()
#     utime.timezone(+7200)
#     #rtc.init((2017, 2, 28, 10, 30, 0, 0, 0))
#     rtc.ntp_sync("pool.ntp.org")
#     while not rtc.synced():
#         utime.sleep_ms(100)
#         print("nope")
#     print('RTC now synced: {}'.format(ertc.get_time()))
#
#
# rtc_synced = pycom.nvs_get('rtc_synced')
# if rtc_synced is None:
#     print ('RTC not synced, syncing now')
#     setup_rtc()
#     ertc.save_time()
#     pycom.nvs_set('rtc_synced', 1)
# else:
#     print('RTC synced: {}'.format(ertc.get_time()))
