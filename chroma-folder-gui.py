from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit, QFileDialog
import sys
import os

class ChromaGUI(QMainWindow):

    def __init__(self):
        super(ChromaGUI, self).__init__()
        self.filename = None
        self.savename = None
        self.initUI()
    
    def initUI(self):
        self.resize(241, 129)
        self.setWindowTitle("Chroma Folder")
        
        self.btnChange = QtWidgets.QPushButton(self)
        self.btnChange.setGeometry(QtCore.QRect(5, 90, 160, 31))
        self.btnChange.setText("Change Folder Icons")
        self.btnChange.setObjectName("btnChange")

        self.btnReset = QtWidgets.QPushButton(self)
        self.btnReset.setGeometry(QtCore.QRect(155, 90, 81, 31))
        self.btnReset.setText("Reset")
        self.btnReset.setObjectName("btnClear")

        self.lblDir = QtWidgets.QLabel(self)
        self.lblDir.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.lblDir.setText("Directory:")
        self.lblDir.setObjectName("lblDir")

        self.txtDir = QtWidgets.QLineEdit(self)
        self.txtDir.setGeometry(QtCore.QRect(90, 8, 141, 20))
        self.txtDir.setText(os.path.expanduser("~/Desktop"))
        self.txtDir.setObjectName("txtDir")

        self.horTop = QtWidgets.QFrame(self)
        self.horTop.setGeometry(QtCore.QRect(10, 30, 221, 20))
        self.horTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.horTop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horTop.setObjectName("horTop")

        self.chkLoad = QtWidgets.QCheckBox(self)
        self.chkLoad.setGeometry(QtCore.QRect(10, 50, 101, 17))
        self.chkLoad.setText("Load Config")
        self.chkLoad.setObjectName("chkLoad")

        self.horBot = QtWidgets.QFrame(self)
        self.horBot.setGeometry(QtCore.QRect(10, 70, 221, 20))
        self.horBot.setFrameShape(QtWidgets.QFrame.HLine)
        self.horBot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horBot.setObjectName("horBot")

        self.chkSave = QtWidgets.QCheckBox(self)
        self.chkSave.setGeometry(QtCore.QRect(130, 50, 101, 17))
        self.chkSave.setText("Save Config")
        self.chkSave.setObjectName("chkSave")

        self.btnChange.clicked.connect(self.change)
        self.btnReset.clicked.connect(self.reset)
        self.chkLoad.stateChanged.connect(self.loadConfig)
        self.chkSave.stateChanged.connect(self.saveConfig)
        

    def change(self):
        pass


    def reset(self):
        self.txtDir.setText(os.path.expanduser("~/Desktop"))
        self.chkLoad.setChecked(False)
        self.chkSave.setChecked(False)
        self.filename = self.savename = None
        self.repaint()


    def loadConfig(self):
        if self.chkLoad.isChecked():
            self.filename = QFileDialog.getOpenFileName(None, "Select Config", "data", "Icon Files (*.icns)")
            if self.filename:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Successfully loaded config file.")
                msgBox.setWindowTitle("Config Load Success")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Failed to load config file. Please retry.")
                msgBox.setWindowTitle("Config Load Fail")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
        else:
            self.filename = None


    def saveConfig(self):
        if self.chkSave.isChecked():
            self.saveConfig = QInputDialog.getText(self, "Save Config","Config name:", QLineEdit.Normal, "")[0].split(".")[0] + ".icns"
        else:
            self.savename = None


def main():
    app = QApplication(sys.argv)
    win = ChromaGUI()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()