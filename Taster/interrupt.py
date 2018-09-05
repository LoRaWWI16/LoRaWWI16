from machine import Pin

def pin_handler(arg):
    print("got an interrupt in pin P4")

p4 = Pin('P4', mode=Pin.IN, pull=Pin.PULL_UP)
#p4.callback(Pin.IRQ_HIGH_LEVEL, pin_handler)

while True:
    print(p4())
