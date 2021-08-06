import smbus
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
bus = smbus.SMBus(1)

class MCP4725():
    
    def dac_write(self,val):
        msb = (val>>8)
        lsb = val & 0x0ff
        bus.write_i2c_block_data(0x64, msb, [lsb])
        time.sleep(0.05)
        
    
 
'''if __name__ == '__main__':
    dac = DAC()
    dac.dac_write(1000)'''
        
