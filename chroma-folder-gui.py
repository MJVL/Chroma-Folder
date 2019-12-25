from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(337, 129)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnChange = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange.setGeometry(QtCore.QRect(10, 90, 191, 31))
        self.btnChange.setObjectName("btnChange")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(210, 90, 121, 31))
        self.btnReset.setObjectName("btnReset")
        self.lblDir = QtWidgets.QLabel(self.centralwidget)
        self.lblDir.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.lblDir.setObjectName("lblDir")
        self.txtDir = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDir.setGeometry(QtCore.QRect(90, 8, 241, 20))
        self.txtDir.setObjectName("txtDir")
        self.horTop = QtWidgets.QFrame(self.centralwidget)
        self.horTop.setGeometry(QtCore.QRect(10, 30, 321, 20))
        self.horTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.horTop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horTop.setObjectName("horTop")
        self.btnLoad = QtWidgets.QCheckBox(self.centralwidget)
        self.btnLoad.setGeometry(QtCore.QRect(20, 50, 101, 17))
        self.btnLoad.setObjectName("btnLoad")
        self.horBot = QtWidgets.QFrame(self.centralwidget)
        self.horBot.setGeometry(QtCore.QRect(10, 70, 321, 20))
        self.horBot.setFrameShape(QtWidgets.QFrame.HLine)
        self.horBot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horBot.setObjectName("horBot")
        self.btnClean = QtWidgets.QCheckBox(self.centralwidget)
        self.btnClean.setGeometry(QtCore.QRect(240, 50, 101, 17))
        self.btnClean.setObjectName("btnClean")
        self.btnSave = QtWidgets.QCheckBox(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(130, 50, 101, 17))
        self.btnSave.setObjectName("btnSave")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chroma Folder"))
        self.btnChange.setText(_translate("MainWindow", "Change Folder Icons"))
        self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.lblDir.setText(_translate("MainWindow", "Directory:"))
        self.btnLoad.setText(_translate("MainWindow", "Load Config"))
        self.btnClean.setText(_translate("MainWindow", "Clean Icons"))
        self.btnSave.setText(_translate("MainWindow", "Save Config"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()