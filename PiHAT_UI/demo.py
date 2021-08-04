from  PyQt5 import QtCore,QtGui,QtWidgets
from pihatui import Ui_form
from RGB import RGB_set
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

class pihatui(QtWidgets.QMainWindow,Ui_form):
    def __init__(self):
        super(pihatui,self).__init__()
        self.ui = Ui_form()
        self.rgb = RGB_set()
        self.ui.setupUi(self)
        self.ui.button_RED.toggled.connect(self.button_RED)
        self.ui.button_GREEN.toggled.connect(self.button_GREEN)
        self.ui.button_BLUE.toggled.connect(self.button_BLUE)

    def button_RED(self,value):
            if(value == True):
                print("RED is Selected")
                RED_toggle(1)
                #self.ui.label.setText("Selected")
            else:
                print("RED is De_Seleced")
                #self.ui.label.setText("De_Selected")

    def button_GREEN(self,value):
            if(value == True):
                print("GREEN is Selected")
                #self.ui.label.setText("Selected")
            else:
                print("GREEN is De_Seleced")
                #self.ui.label.setText("De_Selected")

    def button_BLUE(self,value):
            if(value == True):
                print("BLUE is Selected")
                #self.ui.label.setText("Selected")
            else:
                print("BLUE is De_Seleced")
                #self.ui.label.setText("De_Selected")


app = QtWidgets.QApplication([])
window = pihatui()
window.show()
app.exec()
