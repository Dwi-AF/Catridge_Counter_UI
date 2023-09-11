# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GaugeIhILCN.ui'
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
        MainWindow.resize(341, 336)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LabelCounter.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Current Count</span></p></body></html>", None))
        self.Counter.setText(QCoreApplication.translate("MainWindow", u"20.000", None))
        self.GaugeName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">GOOD</span></p></body></html>", None))
    # retranslateUi

