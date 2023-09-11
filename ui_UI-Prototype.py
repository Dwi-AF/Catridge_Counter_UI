# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI-PrototypeMSeBWP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(663, 487)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.GaugeBase = QFrame(self.centralwidget)
        self.GaugeBase.setObjectName(u"GaugeBase")
        self.GaugeBase.setGeometry(QRect(10, 10, 320, 320))
        self.GaugeBase.setFrameShape(QFrame.NoFrame)
        self.GaugeBase.setFrameShadow(QFrame.Raised)
        self.GaugeBG = QFrame(self.GaugeBase)
        self.GaugeBG.setObjectName(u"GaugeBG")
        self.GaugeBG.setGeometry(QRect(10, 10, 300, 300))
        self.GaugeBG.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.GaugeBG.setFrameShape(QFrame.NoFrame)
        self.GaugeBG.setFrameShadow(QFrame.Raised)
        self.GaugeMeter = QFrame(self.GaugeBase)
        self.GaugeMeter.setObjectName(u"GaugeMeter")
        self.GaugeMeter.setGeometry(QRect(10, 10, 300, 300))
        self.GaugeMeter.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.799 rgba(255, 255, 255, 0), stop:0.8 rgb(0, 175, 255));\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.164 rgba(0, 0, 0, 0), stop:0.165 rgb(0, 175, 255))\n"
"\n"
"}")
        self.GaugeMeter.setFrameShape(QFrame.NoFrame)
        self.GaugeMeter.setFrameShadow(QFrame.Raised)
        self.Interface = QFrame(self.GaugeBase)
        self.Interface.setObjectName(u"Interface")
        self.Interface.setGeometry(QRect(25, 25, 270, 270))
        self.Interface.setStyleSheet(u"QFrame{\n"
"border-radius:135;\n"
"background-color: rgb(0, 100, 255)\n"
"}")
        self.Interface.setFrameShape(QFrame.StyledPanel)
        self.Interface.setFrameShadow(QFrame.Raised)
        self.LabelCounter = QLabel(self.Interface)
        self.LabelCounter.setObjectName(u"LabelCounter")
        self.LabelCounter.setGeometry(QRect(-20, 180, 321, 20))
        font = QFont()
        font.setFamily(u"Mongolian Baiti")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.LabelCounter.setFont(font)
        self.LabelCounter.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.LabelCounter.setAlignment(Qt.AlignCenter)
        self.Counter = QLineEdit(self.Interface)
        self.Counter.setObjectName(u"Counter")
        self.Counter.setGeometry(QRect(84, 210, 111, 25))
        font1 = QFont()
        font1.setFamily(u"Mongolian Baiti")
        font1.setPointSize(12)
        self.Counter.setFont(font1)
        self.Counter.setStyleSheet(u"background-color: none;\n"
"color: rgb(0, 120, 255)")
        self.Counter.setAlignment(Qt.AlignCenter)
        self.GaugeName = QLabel(self.Interface)
        self.GaugeName.setObjectName(u"GaugeName")
        self.GaugeName.setGeometry(QRect(-20, 100, 311, 61))
        self.GaugeName.setFont(font)
        self.GaugeName.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.GaugeName.setAlignment(Qt.AlignCenter)
        self.Border1 = QFrame(self.GaugeBase)
        self.Border1.setObjectName(u"Border1")
        self.Border1.setGeometry(QRect(10, 10, 300, 300))
        self.Border1.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240.001, stop:0 rgba(255, 255, 255, 255), stop:0.001 rgba(255, 255, 255, 0))\n"
"}")
        self.Border1.setFrameShape(QFrame.NoFrame)
        self.Border1.setFrameShadow(QFrame.Raised)
        self.Border2 = QFrame(self.GaugeBase)
        self.Border2.setObjectName(u"Border2")
        self.Border2.setGeometry(QRect(10, 10, 300, 300))
        self.Border2.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:299.001, stop:0 rgba(255, 255, 255, 255), stop:0.001 rgba(255, 255, 255, 0))\n"
"}")
        self.Border2.setFrameShape(QFrame.NoFrame)
        self.Border2.setFrameShadow(QFrame.Raised)
        self.GaugeBG.raise_()
        self.GaugeMeter.raise_()
        self.Border1.raise_()
        self.Border2.raise_()
        self.Interface.raise_()
        self.GaugeBaseR = QFrame(self.centralwidget)
        self.GaugeBaseR.setObjectName(u"GaugeBaseR")
        self.GaugeBaseR.setGeometry(QRect(330, 10, 320, 320))
        self.GaugeBaseR.setFrameShape(QFrame.NoFrame)
        self.GaugeBaseR.setFrameShadow(QFrame.Raised)
        self.GaugeBGR = QFrame(self.GaugeBaseR)
        self.GaugeBGR.setObjectName(u"GaugeBGR")
        self.GaugeBGR.setGeometry(QRect(10, 10, 300, 300))
        self.GaugeBGR.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.GaugeBGR.setFrameShape(QFrame.NoFrame)
        self.GaugeBGR.setFrameShadow(QFrame.Raised)
        self.GaugeMeterR = QFrame(self.GaugeBaseR)
        self.GaugeMeterR.setObjectName(u"GaugeMeterR")
        self.GaugeMeterR.setGeometry(QRect(10, 10, 300, 300))
        self.GaugeMeterR.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.799 rgba(255, 255, 255, 0), stop:0.8 rgba(255, 50, 0, 255));\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.164 rgba(0, 0, 0, 0), stop:0.165 rgba(255, 50, 0, 255))\n"
"}")
        self.GaugeMeterR.setFrameShape(QFrame.NoFrame)
        self.GaugeMeterR.setFrameShadow(QFrame.Raised)
        self.InterfaceR = QFrame(self.GaugeBaseR)
        self.InterfaceR.setObjectName(u"InterfaceR")
        self.InterfaceR.setGeometry(QRect(25, 25, 270, 270))
        self.InterfaceR.setStyleSheet(u"QFrame{\n"
"border-radius:135;\n"
"background-color: rgb(175, 0, 0)\n"
"}")
        self.InterfaceR.setFrameShape(QFrame.StyledPanel)
        self.InterfaceR.setFrameShadow(QFrame.Raised)
        self.LabelCounterR = QLabel(self.InterfaceR)
        self.LabelCounterR.setObjectName(u"LabelCounterR")
        self.LabelCounterR.setGeometry(QRect(-20, 180, 321, 20))
        self.LabelCounterR.setFont(font)
        self.LabelCounterR.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.LabelCounterR.setAlignment(Qt.AlignCenter)
        self.CounterR = QLineEdit(self.InterfaceR)
        self.CounterR.setObjectName(u"CounterR")
        self.CounterR.setGeometry(QRect(84, 210, 111, 25))
        self.CounterR.setFont(font1)
        self.CounterR.setStyleSheet(u"background-color: none;\n"
"color: rgb(175, 0, 0)")
        self.CounterR.setAlignment(Qt.AlignCenter)
        self.GaugeNameR = QLabel(self.InterfaceR)
        self.GaugeNameR.setObjectName(u"GaugeNameR")
        self.GaugeNameR.setGeometry(QRect(-20, 100, 311, 61))
        self.GaugeNameR.setFont(font)
        self.GaugeNameR.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.GaugeNameR.setAlignment(Qt.AlignCenter)
        self.Border1R = QFrame(self.GaugeBaseR)
        self.Border1R.setObjectName(u"Border1R")
        self.Border1R.setGeometry(QRect(10, 10, 300, 300))
        self.Border1R.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240.001, stop:0 rgba(255, 255, 255, 255), stop:0.001 rgba(255, 255, 255, 0))\n"
"}")
        self.Border1R.setFrameShape(QFrame.StyledPanel)
        self.Border1R.setFrameShadow(QFrame.Raised)
        self.Border2R = QFrame(self.GaugeBaseR)
        self.Border2R.setObjectName(u"Border2R")
        self.Border2R.setGeometry(QRect(10, 10, 300, 300))
        self.Border2R.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:299.001, stop:0 rgba(255, 255, 255, 255), stop:0.001 rgba(255, 255, 255, 0))\n"
"}")
        self.Border2R.setFrameShape(QFrame.StyledPanel)
        self.Border2R.setFrameShadow(QFrame.Raised)
        self.GaugeBGR.raise_()
        self.GaugeMeterR.raise_()
        self.Border1R.raise_()
        self.Border2R.raise_()
        self.InterfaceR.raise_()
        self.CounterBase = QFrame(self.centralwidget)
        self.CounterBase.setObjectName(u"CounterBase")
        self.CounterBase.setGeometry(QRect(20, 350, 441, 121))
        self.CounterBase.setFrameShape(QFrame.Box)
        self.CounterBase.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.CounterBase)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 20, 191, 30))
        font2 = QFont()
        font2.setFamily(u"Mongolian Baiti")
        font2.setPointSize(20)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"background-color: none;\n"
"color: rgb(0, 0, 0)")
        self.TargetLabel = QLabel(self.CounterBase)
        self.TargetLabel.setObjectName(u"TargetLabel")
        self.TargetLabel.setGeometry(QRect(40, 20, 101, 41))
        self.TargetLabel.setFont(font)
        self.TargetLabel.setStyleSheet(u"background-color: none;\n"
"color: rgb(0, 0, 0)")
        self.TargetLabel.setAlignment(Qt.AlignCenter)
        self.TotalLabel = QLabel(self.CounterBase)
        self.TotalLabel.setObjectName(u"TotalLabel")
        self.TotalLabel.setGeometry(QRect(150, 50, 151, 41))
        font3 = QFont()
        font3.setFamily(u"Mongolian Baiti")
        font3.setPointSize(6)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.TotalLabel.setFont(font3)
        self.TotalLabel.setStyleSheet(u"background-color: none;\n"
"color: rgb(0, 0, 0)")
        self.TotalLabel.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(480, 350, 171, 121))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 20, 121, 30))
        font4 = QFont()
        font4.setFamily(u"Mongolian Baiti")
        font4.setPointSize(14)
        self.pushButton.setFont(font4)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 70, 121, 30))
        self.pushButton_2.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LabelCounter.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Current Count</span></p></body></html>", None))
        self.Counter.setText(QCoreApplication.translate("MainWindow", u"20.000", None))
        self.GaugeName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">GOOD</span></p></body></html>", None))
        self.LabelCounterR.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Current Count</span></p></body></html>", None))
        self.CounterR.setText(QCoreApplication.translate("MainWindow", u"1.000", None))
        self.GaugeNameR.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">REJECT</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"20.000", None))
        self.TargetLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#000000;\">Total</span></p></body></html>", None))
        self.TotalLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">Target: 20.000</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

