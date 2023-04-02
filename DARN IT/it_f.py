# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'it.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from cn_f import Ui_MainWindow_cn


class Ui_itWindow(object):
    def go_back(self,itWindow):
        itWindow.hide()
    def open_cn(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_cn()
        self.ui.setupUi_cn(self.window)
        self.window.show()
    def setupUi_it(self, itWindow):
        itWindow.setObjectName("itWindow")
        itWindow.resize(1300, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        itWindow.setWindowIcon(icon)
        itWindow.setWindowOpacity(3.0)
        self.centralwidget = QtWidgets.QWidget(itWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.poc_b = QtWidgets.QPushButton(self.frame)
        self.poc_b.setGeometry(QtCore.QRect(170, 200, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.poc_b.setFont(font)
        self.poc_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.poc_b.setObjectName("poc_b")
        self.dsa_b = QtWidgets.QPushButton(self.frame)
        self.dsa_b.setGeometry(QtCore.QRect(170, 530, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dsa_b.setFont(font)
        self.dsa_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.dsa_b.setObjectName("dsa_b")
        self.m3_b = QtWidgets.QPushButton(self.frame)
        self.m3_b.setGeometry(QtCore.QRect(170, 310, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.m3_b.setFont(font)
        self.m3_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.m3_b.setObjectName("m3_b")
        self.dbms_b = QtWidgets.QPushButton(self.frame)
        self.dbms_b.setGeometry(QtCore.QRect(170, 640, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dbms_b.setFont(font)
        self.dbms_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.dbms_b.setObjectName("dbms_b")
        self.pcpf_b = QtWidgets.QPushButton(self.frame)
        self.pcpf_b.setGeometry(QtCore.QRect(170, 420, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pcpf_b.setFont(font)
        self.pcpf_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.pcpf_b.setObjectName("pcpf_b")
        self.coa_b = QtWidgets.QPushButton(self.frame)
        self.coa_b.setGeometry(QtCore.QRect(750, 640, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.coa_b.setFont(font)
        self.coa_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.coa_b.setObjectName("coa_b")
        self.at_b = QtWidgets.QPushButton(self.frame)
        self.at_b.setGeometry(QtCore.QRect(749, 200, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.at_b.setFont(font)
        self.at_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.at_b.setObjectName("at_b")
        self.m4_b = QtWidgets.QPushButton(self.frame)
        self.m4_b.setGeometry(QtCore.QRect(750, 530, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.m4_b.setFont(font)
        self.m4_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.m4_b.setObjectName("m4_b")
        self.cn_b = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_cn())
        self.cn_b.setGeometry(QtCore.QRect(750, 420, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cn_b.setFont(font)
        self.cn_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.cn_b.setObjectName("cn_b")
        self.os_b = QtWidgets.QPushButton(self.frame)
        self.os_b.setGeometry(QtCore.QRect(750, 310, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.os_b.setFont(font)
        self.os_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.os_b.setObjectName("os_b")
        self.l1 = QtWidgets.QLabel(self.frame)
        self.l1.setGeometry(QtCore.QRect(300, 100, 121, 35))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.l1.setFont(font)
        self.l1.setStyleSheet("font: 20pt \"Artifakt Element\";\n"
"background : transparent;\n"
"color: rgb(255, 255, 255);")
        self.l1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.l1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.l1_2 = QtWidgets.QLabel(self.frame)
        self.l1_2.setGeometry(QtCore.QRect(890, 100, 121, 35))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.l1_2.setFont(font)
        self.l1_2.setStyleSheet("font: 20pt \"Artifakt Element\";\n"
"background : transparent;\n"
"color: rgb(255, 255, 255);")
        self.l1_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.l1_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_2.setObjectName("l1_2")
        self.bg = QtWidgets.QLabel(self.frame)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("pictures/try2-dark-stripes-background-elegant-design-wallpapers_518299-1505.jpg"))
        self.bg.setObjectName("bg")
        self.back = QtWidgets.QPushButton(self.frame,clicked = lambda : self.go_back(itWindow))
        self.back.setGeometry(QtCore.QRect(40, 40, 151, 61))
        self.back.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.back.setObjectName("back")
        self.bg.raise_()
        self.poc_b.raise_()
        self.dsa_b.raise_()
        self.m3_b.raise_()
        self.dbms_b.raise_()
        self.pcpf_b.raise_()
        self.coa_b.raise_()
        self.at_b.raise_()
        self.m4_b.raise_()
        self.cn_b.raise_()
        self.os_b.raise_()
        self.l1.raise_()
        self.l1_2.raise_()
        self.back.raise_()
        itWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(itWindow)
        QtCore.QMetaObject.connectSlotsByName(itWindow)

    def retranslateUi(self, itWindow):
        _translate = QtCore.QCoreApplication.translate
        itWindow.setWindowTitle(_translate("itWindow", "DARN IT"))
        self.poc_b.setText(_translate("itWindow", "POC"))
        self.dsa_b.setText(_translate("itWindow", "DSA"))
        self.m3_b.setText(_translate("itWindow", "MATHS-3"))
        self.dbms_b.setText(_translate("itWindow", "DBMS"))
        self.pcpf_b.setText(_translate("itWindow", "PCPF"))
        self.coa_b.setText(_translate("itWindow", "COA"))
        self.at_b.setText(_translate("itWindow", "AT"))
        self.m4_b.setText(_translate("itWindow", "MATHS-4"))
        self.cn_b.setText(_translate("itWindow", "CN"))
        self.os_b.setText(_translate("itWindow", "OS"))
        self.l1.setText(_translate("itWindow", "Sem-3"))
        self.l1_2.setText(_translate("itWindow", "Sem-4"))
        self.back.setText(_translate("itWindow", "BACK"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    itWindow = QtWidgets.QMainWindow()
    ui = Ui_itWindow()
    ui.setupUi_it(itWindow)
    itWindow.show()
    sys.exit(app.exec_())