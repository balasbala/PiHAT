import smbus
import time

class BH1745():
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.bus.write_byte_data(0x38, 0x41, 0x02)
        self.bus.write_byte_data(0x38, 0x42, 0x10)
        self.bus.write_byte_data(0x38, 0x44, 0x02)
        time.sleep(0.5)

    def readRGB(self):
        data = self.bus.read_i2c_block_data(0x38, 0x50, 8)
        color = []
        color.append(data[1] * 256 + data[0])
        color.append(data[3] * 256 + data[2])
        color.append(data[5] * 256 + data[4])
        color.append(data[7] * 256 + data[6])
        return color
        
        
    def readRED(self):
        color = self.readRGB()
        return color[0]

    def readGREEN(self):
        color = self.readRGB()
        return color[1]
    
    def readBLUE(self):
        color = self.readRGB()
        return color[2]
    
    def readCLEAR(self):
        color = self.readRGB()
        return color[3]
    
'''bh1745 = BH1745()
red = bh1745.readRED()
green = bh1745.readGREEN()
blue = bh1745.readBLUE()
clear = bh1745.readCLEAR()
print(f"Red:{red}")
print(f"Green:{green}")
print(f"Blue:{blue}")
print(f"Clear:{clear}")'''
