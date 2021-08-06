import smbus
import time

class SI7006_TH():
    def __init__(self):
        self.bus = smbus.SMBus(1)

    def humidity_read(self):
        self.bus.write_byte(0x40,0xF5)
        time.sleep(0.5)
        humidityM = self.bus.read_byte(0x40)
        humidityL = self.bus.read_byte(0x40)
        humidity = (humidityM<<8)+(humidityL) 
        humidity = ((125*humidity/65536)-6)
        return humidity
    
    def temperature_read(self):
        self.bus.write_byte(0x40,0xF3)
        time.sleep(0.5)
        temperatureM = self.bus.read_byte(0x40)
        temperatureL = self.bus.read_byte(0x40)
        temperature = (temperatureM<<8)+(temperatureL) 
        temperature = ((175.72*temperature/65536)-46.85)
        return temperature

'''si7006 = SI7006()
while True:
    humid = si7006.humidity_read()
    temperature = si7006.temperature_read()
    
    print(f"Humidity:{round(humid,2)}%")
    print(f"Temperature:{round(temperature,2)}*C")'''
    
