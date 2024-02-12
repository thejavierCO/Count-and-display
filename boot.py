# boot.py -- run on boot-up
from machine import Pin, PWM, UART

class display:
    def __init__(self,a,b,c,d,e,f,g,invert=False):
        self.a = Pin(a,Pin.OUT)
        self.b = Pin(b,Pin.OUT)
        self.c = Pin(c,Pin.OUT)
        self.d = Pin(d,Pin.OUT)
        self.e = Pin(e,Pin.OUT)
        self.f = Pin(f,Pin.OUT)
        self.g = Pin(g,Pin.OUT)
    
    def print(self,num):
        if num == 0:
            self.set0()
        elif num == 1:
            self.set1()
        elif num == 2:
            self.set2()
        elif num == 3:
            self.set3()
        elif num == 4:
            self.set4()
        elif num == 5:
            self.set5()
        elif num == 6:
            self.set6()
        elif num == 7:
            self.set7()
        elif num == 8:
            self.set8()
        elif num == 9:
            self.set9()
        else:
            self.a.on()
            self.b.on()
            self.c.on()
            self.d.on()
            self.e.on()
            self.f.on()
            self.g.on()
        
    
    def set0(self):
        self.a.on()
        self.b.on()
        self.c.on()
        self.d.on()
        self.e.off()
        self.f.off()
        self.g.on()
    
    def set1(self):
        self.a.on()
        self.b.on()
        self.c.on()
        self.d.on()
        self.e.off()
        self.f.off()
        self.g.on()
    
    def set2(self):
        self.a.off()
        self.b.off()
        self.c.on()
        self.d.off()
        self.e.off()
        self.f.on()
        self.g.off()
    
    def set3(self):
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.off()
        self.e.on()
        self.f.on()
        self.g.off()
    
    def set4(self):
        self.a.on()
        self.b.off()
        self.c.off()
        self.d.on()
        self.e.on()
        self.f.off()
        self.g.off()
    
    def set5(self):
        self.a.off()
        self.b.on()
        self.c.off()
        self.d.off()
        self.e.on()
        self.f.off()
        self.g.off()
    
    def set6(self):
        self.a.off()
        self.b.on()
        self.c.off()
        self.d.off()
        self.e.off()
        self.f.off()
        self.g.off()
    
    def set7(self):
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.on()
        self.e.on()
        self.f.on()
        self.g.on()
    
    def set8(self):
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.off()
        self.e.off()
        self.f.off()
        self.g.off()
    
    def set9(self):
        self.a.off()
        self.b.off()
        self.c.off()
        self.d.off()
        self.e.on()
        self.f.off()
        self.g.off()