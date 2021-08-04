import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class RGB():
    def __init__(self):
        self.red = 22
        self.green = 23
        self.blue = 24
        GPIO.setup(22,GPIO.OUT,initial = GPIO.HIGH)
        GPIO.setup(23,GPIO.OUT,initial = GPIO.HIGH)
        GPIO.setup(24,GPIO.OUT,initial = GPIO.HIGH)
    
    def set_led(self,r,g,b):
            GPIO.output(self.red,r)
            GPIO.output(self.green,g)
            GPIO.output(self.blue,b)
            
            
led = RGB()
led.set_led(1,1,0)
led.set_led(0,1,1)
led.set_led(1,0,1)
led.set_led(1,0,0)
led.set_led(0,0,1)
led.set_led(0,1,0)