import smbus
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
bus = smbus.SMBus(1)
key1=0
class keypad():
    def __init__(self):
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
        bus.write_byte_data(0x34, 0x1d, 0x0f)
        bus.write_byte_data(0x34, 0x1e, 0x0f)
        bus.write_byte_data(0x34, 0x1f, 0x00)
        bus.write_byte_data(0x34, 0x01, 0x95)
    
        GPIO.add_event_detect(5, GPIO.FALLING, callback=button_pressed_callback, bouncetime=100)
    
def button_pressed_callback(channel):
    bus.write_byte(0x34,0x04)
    key = bus.read_byte(0x34)
    press = key & 0x80
    key =key & 0x7F
    if press == 128:
        if key == 4:
            print("pressed value : A")
        elif key == 11:
            print("pressed value : 4")
        elif key == 12:
            print("pressed value : 5")
        elif key == 13:
            print("pressed value : 6")
        elif key == 14:
            print("pressed value : B")
        elif key == 21:
            print("pressed value : 7")
        elif key == 22:
            print("pressed value : 8")
        elif key == 23:
            print("pressed value : 9")
        elif key == 24:
            print("pressed value : C")
        elif key == 31:
            print("pressed value : *")
        elif key == 32:
            print("pressed value : 0")
        elif key == 33:
            print("pressed value : #")
        elif key == 34:
            print("pressed value : D")
        else:
            print("pressed value :",key)
    bus.write_byte_data(0x34,0x02,0x01)
    
                         
    
if __name__ == '__main__':
    keypad=keypad()
    while True:
        bus.write_byte_data(0x34,0x02,0x01)
