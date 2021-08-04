# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'source.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(736, 569)
        self.button_RED = QtWidgets.QCheckBox(form)
        self.button_RED.setGeometry(QtCore.QRect(150, 120, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_RED.setFont(font)
        self.button_RED.setObjectName("button_RED")
        self.button_GREEN = QtWidgets.QCheckBox(form)
        self.button_GREEN.setGeometry(QtCore.QRect(150, 180, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_GREEN.setFont(font)
        self.button_GREEN.setObjectName("button_GREEN")
        self.button_BLUE = QtWidgets.QCheckBox(form)
        self.button_BLUE.setGeometry(QtCore.QRect(150, 240, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_BLUE.setFont(font)
        self.button_BLUE.setObjectName("button_BLUE")
        self.button_temp = QtWidgets.QPushButton(form)
        self.button_temp.setGeometry(QtCore.QRect(250, 320, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_temp.setFont(font)
        self.button_temp.setObjectName("button_temp")
        self.button_humid = QtWidgets.QPushButton(form)
        self.button_humid.setGeometry(QtCore.QRect(250, 390, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_humid.setFont(font)
        self.button_humid.setObjectName("button_humid")
        self.label_temp = QtWidgets.QLabel(form)
        self.label_temp.setGeometry(QtCore.QRect(60, 330, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_temp.setFont(font)
        self.label_temp.setObjectName("label_temp")
        self.label_humid = QtWidgets.QLabel(form)
        self.label_humid.setGeometry(QtCore.QRect(100, 400, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_humid.setFont(font)
        self.label_humid.setObjectName("label_humid")
        self.button_refresh = QtWidgets.QPushButton(form)
        self.button_refresh.setGeometry(QtCore.QRect(280, 460, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_refresh.setFont(font)
        self.button_refresh.setObjectName("button_refresh")

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "PiHAT_UI"))
        self.button_RED.setText(_translate("form", "RED"))
        self.button_GREEN.setText(_translate("form", "GREEN"))
        self.button_BLUE.setText(_translate("form", "BLUE"))
        self.button_temp.setText(_translate("form", "Temp"))
        self.button_humid.setText(_translate("form", "Humid"))
        self.label_temp.setText(_translate("form", "TEMPEARTURE"))
        self.label_humid.setText(_translate("form", "HUMIDITY"))
        self.button_refresh.setText(_translate("form", "Refresh"))
