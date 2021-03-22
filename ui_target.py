# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'targetfkhRBX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(590, 271)
        Dialog.setStyleSheet(u"background-color: rgb(170, 170, 127);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.lineEdit = QLineEdit(self.splitter)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(500, 500))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.splitter.addWidget(self.lineEdit)
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")
        self.splitter.addWidget(self.pushButton)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2 = QSplitter(Dialog)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.lineEdit_2 = QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(800, 1000))
        self.lineEdit_2.setFont(font)
        self.splitter_2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QPushButton(self.splitter_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.splitter_2.addWidget(self.pushButton_2)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter_3 = QSplitter(Dialog)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.comboBox = QComboBox(self.splitter_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.comboBox.setFont(font1)
        self.splitter_3.addWidget(self.comboBox)
        self.pushButton_3 = QPushButton(self.splitter_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.splitter_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QPushButton(self.splitter_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)
        self.splitter_3.addWidget(self.pushButton_4)

        self.verticalLayout.addWidget(self.splitter_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"linebreak_replacer", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Browse the directory files to convert", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"....", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"browse log text file", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"....", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"unix", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"mac", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"windows", None))

        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Convert", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Clear", None))
    # retranslateUi
