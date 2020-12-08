
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
import re
import sys, os
from replacer import *
from ui_target import *
import zipfile
import shutil
from threading import Thread



class Main(QDialog, Ui_Dialog):

    def __init__(self,parent=None):

        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.Handel_Buttons()


    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.browse_file1)
        self.pushButton_2.clicked.connect(self.browse_file2)
        self.pushButton_3.clicked.connect(self.download1)
        self.pushButton_4.clicked.connect(self.clear)


    def browse_file1(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)



        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.lineEdit.setText(QDir.toNativeSeparators(str(filenames[0])))

    def browse_file2(self):
        self.browse_file = QFileDialog.getOpenFileName(self, "browse files", directory=".",filter="All Files (*.*)")
        self.lineEdit_2.setText(QDir.toNativeSeparators(str(self.browse_file[0])))
        return self.browse_file[0]



    def download1(self):
        try:
            input_file1= self.lineEdit.text()
            logfile= self.lineEdit_2.text()
            exttype= self.comboBox.currentText()
            mapreduce(input_file1, exttype, logfile)

        except Exception:
            QMessageBox.warning(self, "Warning", "The file conversion failed")
            return

        QMessageBox.information(self, "Information", "The converted files successfully added to the folder")




    def clear(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")


def main1():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__=='__main__':
    main1()
