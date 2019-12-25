from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
import sys
import os


class Ui_MainWindow(object):

    def __init__(self):
        self.filename = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(241, 129)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnChange = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange.setGeometry(QtCore.QRect(10, 90, 221, 31))
        self.btnChange.setObjectName("btnChange")
        self.lblDir = QtWidgets.QLabel(self.centralwidget)
        self.lblDir.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.lblDir.setObjectName("lblDir")
        self.txtDir = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDir.setGeometry(QtCore.QRect(90, 8, 141, 20))
        self.txtDir.setObjectName("txtDir")
        self.horTop = QtWidgets.QFrame(self.centralwidget)
        self.horTop.setGeometry(QtCore.QRect(10, 30, 221, 20))
        self.horTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.horTop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horTop.setObjectName("horTop")
        self.chkLoad = QtWidgets.QCheckBox(self.centralwidget)
        self.chkLoad.setGeometry(QtCore.QRect(10, 50, 101, 17))
        self.chkLoad.setObjectName("chkLoad")
        self.horBot = QtWidgets.QFrame(self.centralwidget)
        self.horBot.setGeometry(QtCore.QRect(10, 70, 221, 20))
        self.horBot.setFrameShape(QtWidgets.QFrame.HLine)
        self.horBot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horBot.setObjectName("horBot")
        self.chkSave = QtWidgets.QCheckBox(self.centralwidget)
        self.chkSave.setGeometry(QtCore.QRect(130, 50, 101, 17))
        self.chkSave.setObjectName("chkSave")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.txtDir.setText(os.path.expanduser("~/Desktop"))
        self.btnChange.clicked.connect(self.change)
        self.chkLoad.stateChanged.connect(self.loadConfig)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chroma Folder"))
        self.btnChange.setText(_translate("MainWindow", "Change Folder Icons"))
        self.lblDir.setText(_translate("MainWindow", "Directory:"))
        self.chkLoad.setText(_translate("MainWindow", "Load Config"))
        self.chkSave.setText(_translate("MainWindow", "Save Config"))

    def change(self):
        pass

    def loadConfig(self):
        if self.chkLoad.isChecked():
            self.filename = QtWidgets.QFileDialog.getOpenFileName(None, "Select Config", "data", "Icon Files (*.icns)")
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()