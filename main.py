from machine import Pin, PWM, UART
from neopixel import NeoPixel
from time import sleep

pin = Pin(0,Pin.IN,Pin.PULL_DOWN)

led = NeoPixel(Pin (16),1)

def on():
    led[0] = (10,10,10)
    led.write()
    sleep(1)
def off():
    led[0] = (0,0,0)
    led.write()
    sleep(1)
off()

count = 0
change = False
maxCount = 10

dis = display(1,2,3,4,5,6,7)

while True:
    dis.print(count)
    sleep(0.01)
    OLD = count+1
    while pin.value() == 0:
        if count >= maxCount:
            count = 0;
        elif OLD > count:
            count = count+1;
    
        