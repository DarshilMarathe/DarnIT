# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'darnit.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from fe_f import Ui_MainWindow_fe
from it_f import Ui_itWindow


class Ui_MainWindow(object):
    def open_second_window(self):
        if self.cb1.currentText() == "FE":
            self.open_fe()
        if self.cb1.currentText() == "SE":
            if self.cb2.currentText() == "IT":
                self.open_IT()
            if self.cb2.currentText() == "AIDS":
                self.open_AIDS()
            if self.cb2.currentText() == "CS":
                self.open_CS()
            if self.cb2.currentText() == "EXTC":
                self.open_EXTC()
            if self.cb2.currentText() == "Chemical":
                self.open_Chemical()

    def open_IT(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_itWindow()
        self.ui.setupUi_it(self.window)
        self.window.show()

    def open_fe(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_fe()
        self.ui.setupUi_fe(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.f1 = QtWidgets.QFrame(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.f1.setStyleSheet("")
        self.f1.setFrameShape(QtWidgets.QFrame.Box)
        self.f1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f1.setLineWidth(2)
        self.f1.setObjectName("f1")
        self.l1 = QtWidgets.QLabel(self.f1)
        self.l1.setGeometry(QtCore.QRect(250, 420, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.l1.setFont(font)
        self.l1.setStyleSheet("background : transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";")
        self.l1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.l1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l1.setObjectName("l1")
        self.icon = QtWidgets.QLabel(self.f1)
        self.icon.setGeometry(QtCore.QRect(830, 70, 391, 371))
        self.icon.setStyleSheet("background :  transparent;\n"
"")
        self.icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.icon.setFrameShadow(QtWidgets.QFrame.Plain)
        self.icon.setLineWidth(0)
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("icon.png"))
        self.icon.setScaledContents(True)
        self.icon.setWordWrap(False)
        self.icon.setObjectName("icon")
        self.l1_2 = QtWidgets.QLabel(self.f1)
        self.l1_2.setGeometry(QtCore.QRect(220, 510, 102, 31))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.l1_2.setFont(font)
        self.l1_2.setStyleSheet("background : transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";")
        self.l1_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.l1_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l1_2.setObjectName("l1_2")
        self.label_2 = QtWidgets.QLabel(self.f1)
        self.label_2.setGeometry(QtCore.QRect(820, 520, 421, 121))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(56)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background : transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 56pt \"Artifakt Element\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.wel = QtWidgets.QLabel(self.f1)
        self.wel.setGeometry(QtCore.QRect(90, 70, 511, 91))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.wel.setFont(font)
        self.wel.setStyleSheet("background : transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 36pt \"Artifakt Element\";")
        self.wel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.wel.setObjectName("wel")
        self.info = QtWidgets.QLabel(self.f1)
        self.info.setGeometry(QtCore.QRect(90, 180, 652, 182))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.info.setFont(font)
        self.info.setStyleSheet("background : transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Artifakt Element\";")
        self.info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info.setObjectName("info")
        self.cb1 = QtWidgets.QComboBox(self.f1)
        self.cb1.setGeometry(QtCore.QRect(420, 420, 137, 34))
        self.cb1.setAutoFillBackground(False)
        self.cb1.setStyleSheet("color: rgb(238, 244, 239);\n"
"background-color: rgb(0, 85, 0);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"background : transparent;\n"
"opacity: 1.8;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);")
        self.cb1.setEditable(False)
        self.cb1.setDuplicatesEnabled(False)
        self.cb1.setFrame(True)
        self.cb1.setObjectName("cb1")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb2 = QtWidgets.QComboBox(self.f1)
        self.cb2.setGeometry(QtCore.QRect(420, 510, 137, 34))
        self.cb2.setAutoFillBackground(False)
        self.cb2.setStyleSheet("color: rgb(238, 244, 239);\n"
"background-color: rgb(0, 85, 0);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"background : transparent;\n"
"opacity: 1.8;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);")
        self.cb2.setObjectName("cb2")
        self.cb2.addItem("")
        self.cb2.addItem("")
        self.cb2.addItem("")
        self.cb2.addItem("")
        self.cb2.addItem("")
        self.phy1_b_7 = QtWidgets.QPushButton(self.f1,clicked = lambda : self.open_second_window())
        self.phy1_b_7.setGeometry(QtCore.QRect(250, 600, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.phy1_b_7.setFont(font)
        self.phy1_b_7.setAutoFillBackground(False)
        self.phy1_b_7.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.phy1_b_7.setObjectName("phy1_b_7")
        self.bg = QtWidgets.QLabel(self.f1)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("pictures/try2-dark-stripes-background-elegant-design-wallpapers_518299-1505.jpg"))
        self.bg.setObjectName("bg")
        self.bg.raise_()
        self.l1.raise_()
        self.icon.raise_()
        self.l1_2.raise_()
        self.label_2.raise_()
        self.wel.raise_()
        self.info.raise_()
        self.cb1.raise_()
        self.cb2.raise_()
        self.phy1_b_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DARN IT"))
        self.l1.setText(_translate("MainWindow", "Year :"))
        self.l1_2.setText(_translate("MainWindow", "Branch :"))
        self.label_2.setText(_translate("MainWindow", "DARN-IT"))
        self.wel.setText(_translate("MainWindow", "WELCOME !!!"))
        self.info.setText(_translate("MainWindow", "<html><head/><body><p>DARN-IT is an engineering study app that helps students prepare for<br/>exams by sortng questions module-wise.With a simple and initutive <br/>interface, students can easily select the modules they need to study <br/>and focus on those specific area.The app also provides a feature to <br/>track progress and performance allowing students to identify area<br/>that need improvements. <br/></p></body></html>"))
        self.cb1.setItemText(0, _translate("MainWindow", "FE"))
        self.cb1.setItemText(1, _translate("MainWindow", "SE"))
        self.cb2.setItemText(0, _translate("MainWindow", "IT"))
        self.cb2.setItemText(1, _translate("MainWindow", "CS"))
        self.cb2.setItemText(2, _translate("MainWindow", "EXTC"))
        self.cb2.setItemText(3, _translate("MainWindow", "Chemical"))
        self.cb2.setItemText(4, _translate("MainWindow", "AIDS"))
        self.phy1_b_7.setText(_translate("MainWindow", "SUBMIT"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())