import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class RGB_set():
    def __init__(self):
        self.red = 22
        self.green = 23
        self.blue = 24
        GPIO.setup(22,GPIO.OUT,initial = GPIO.HIGH)
        GPIO.setup(23,GPIO.OUT,initial = GPIO.HIGH)
        GPIO.setup(24,GPIO.OUT,initial = GPIO.HIGH)
            
    def RED_toggle(self,value):
        if (value == True):
            GPIO.output(self,red,0)
        else:
            GPIO.output(self,red,1)

    def GREEN_toggle(self,value):
        if (value == True):
            GPIO.output(self,green,0)
        else:
            GPIO.output(self,green,1)

    def BLUE_toggle(self,value):
        if (value == True):
            GPIO.output(self,blue,0)
        else:
            GPIO.output(self,blue,1)
