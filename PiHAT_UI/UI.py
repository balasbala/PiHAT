from  PyQt5 import QtCore,QtGui,QtWidgets
from source import Ui_form
from RGB import RGB_set
from Temp_Humid import SI7006_TH
from amb_RGB import BH1745
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

class pihatui(QtWidgets.QMainWindow,Ui_form):
    def __init__(self):
        super(pihatui,self).__init__()
        self.ui = Ui_form()
        self.rgb = RGB_set()
        self.th = SI7006_TH()
        self.amb_rgb = BH1745()
        self.ui.setupUi(self)
        self.ui.button_RED.toggled.connect(self.button_RED)
        self.ui.button_GREEN.toggled.connect(self.button_GREEN)
        self.ui.button_BLUE.toggled.connect(self.button_BLUE)
        self.ui.button_refresh.pressed.connect(self.temp_humid_amb)

    def button_RED(self,value):
            if(value == True):
                print("RED is Selected")
                self.rgb.RED_toggle(1)
            else:
                print("RED is De_Seleced")
                self.rgb.RED_toggle(0)

    def button_GREEN(self,value):
            if(value == True):
                print("GREEN is Selected")
                self.rgb.GREEN_toggle(1)
            else:
                print("GREEN is De_Seleced")
                self.rgb.GREEN_toggle(0)

    def button_BLUE(self,value):
            if(value == True):
                print("BLUE is Selected")
                self.rgb.BLUE_toggle(1)
            else:
                print("BLUE is De_Seleced")
                self.rgb.BLUE_toggle(0)
                
    def temp_humid_amb(self):
        temperature = self.th.temperature_read()
        self.ui.button_temp.SetText(str(round(temperature,2)))
        
        humidity = self.th.humidity_read()
        self.ui.button_humid.SetText(str(round(humidity,2)))

        red = self.amb_rgb.readRED()
        green = self.amb_rgb.readGREEN()
        blue = self.amb_rgb.readBLUE()
        self.ui.button_amb_r.SetText(str(round(red,2)))
        self.ui.button_amb_g.SetText(str(round(green,2)))
        self.ui.button_amb_b.SetText(str(round(blue,2)))


    

app = QtWidgets.QApplication([])
window = pihatui()
window.show()
app.exec()
