# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fe.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_fe(object):
    def go_back(self,itWindow):
        itWindow.hide()
    def setupUi_fe(self, MainWindow_fe):
        MainWindow_fe.setObjectName("MainWindow_fe")
        MainWindow_fe.resize(1300, 800)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        MainWindow_fe.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\darsh\\Downloads\\DarnIT-main (1)\\DarnIT-main\\DARN IT\\pictures\\icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_fe.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow_fe)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.phy1_b = QtWidgets.QPushButton(self.frame)
        self.phy1_b.setGeometry(QtCore.QRect(160, 200, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.phy1_b.setFont(font)
        self.phy1_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.phy1_b.setObjectName("phy1_b")
        self.m1_b = QtWidgets.QPushButton(self.frame)
        self.m1_b.setGeometry(QtCore.QRect(160, 530, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.m1_b.setFont(font)
        self.m1_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.m1_b.setObjectName("m1_b")
        self.chem1_b = QtWidgets.QPushButton(self.frame)
        self.chem1_b.setGeometry(QtCore.QRect(160, 310, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chem1_b.setFont(font)
        self.chem1_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.chem1_b.setObjectName("chem1_b")
        self.bee_b = QtWidgets.QPushButton(self.frame)
        self.bee_b.setGeometry(QtCore.QRect(160, 640, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bee_b.setFont(font)
        self.bee_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.bee_b.setObjectName("bee_b")
        self.mech_b = QtWidgets.QPushButton(self.frame)
        self.mech_b.setGeometry(QtCore.QRect(160, 420, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mech_b.setFont(font)
        self.mech_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.mech_b.setObjectName("mech_b")
        self.eg_b = QtWidgets.QPushButton(self.frame)
        self.eg_b.setGeometry(QtCore.QRect(740, 640, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eg_b.setFont(font)
        self.eg_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.eg_b.setObjectName("eg_b")
        self.phy2_b = QtWidgets.QPushButton(self.frame)
        self.phy2_b.setGeometry(QtCore.QRect(739, 200, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.phy2_b.setFont(font)
        self.phy2_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.phy2_b.setObjectName("phy2_b")
        self.m2_b = QtWidgets.QPushButton(self.frame)
        self.m2_b.setGeometry(QtCore.QRect(740, 530, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.m2_b.setFont(font)
        self.m2_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.m2_b.setObjectName("m2_b")
        self.cp_b = QtWidgets.QPushButton(self.frame)
        self.cp_b.setGeometry(QtCore.QRect(740, 420, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cp_b.setFont(font)
        self.cp_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.cp_b.setObjectName("cp_b")
        self.chem2_b = QtWidgets.QPushButton(self.frame)
        self.chem2_b.setGeometry(QtCore.QRect(740, 310, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chem2_b.setFont(font)
        self.chem2_b.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.chem2_b.setObjectName("chem2_b")
        self.l1 = QtWidgets.QLabel(self.frame)
        self.l1.setGeometry(QtCore.QRect(300, 90, 121, 35))
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
        self.l1_2.setGeometry(QtCore.QRect(870, 90, 121, 35))
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\darsh\\Downloads\\DarnIT-main (1)\\DarnIT-main\\DARN IT\\pictures\\try2-dark-stripes-background-elegant-design-wallpapers_518299-1505.jpg"))
        self.label.setObjectName("label")
        self.back = QtWidgets.QPushButton(self.frame,clicked = lambda : self.go_back(MainWindow_fe))
        self.back.setGeometry(QtCore.QRect(40, 30, 151, 61))
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
        self.label.raise_()
        self.phy1_b.raise_()
        self.m1_b.raise_()
        self.chem1_b.raise_()
        self.bee_b.raise_()
        self.mech_b.raise_()
        self.eg_b.raise_()
        self.phy2_b.raise_()
        self.m2_b.raise_()
        self.cp_b.raise_()
        self.chem2_b.raise_()
        self.l1.raise_()
        self.l1_2.raise_()
        self.back.raise_()
        MainWindow_fe.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_fe)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_fe)

    def retranslateUi(self, MainWindow_fe):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_fe.setWindowTitle(_translate("MainWindow_fe", "DARN IT"))
        self.phy1_b.setText(_translate("MainWindow_fe", "Physics-1"))
        self.m1_b.setText(_translate("MainWindow_fe", "MATHS-1"))
        self.chem1_b.setText(_translate("MainWindow_fe", "Chemistry-1"))
        self.bee_b.setText(_translate("MainWindow_fe", "BEE"))
        self.mech_b.setText(_translate("MainWindow_fe", "Mechanics"))
        self.eg_b.setText(_translate("MainWindow_fe", "Engineering Graphics"))
        self.phy2_b.setText(_translate("MainWindow_fe", "Physics-2"))
        self.m2_b.setText(_translate("MainWindow_fe", "MATHS-2"))
        self.cp_b.setText(_translate("MainWindow_fe", "C-Programming"))
        self.chem2_b.setText(_translate("MainWindow_fe", "Chemistry-2"))
        self.l1.setText(_translate("MainWindow_fe", "Sem-1"))
        self.l1_2.setText(_translate("MainWindow_fe", "Sem-2"))
        self.back.setText(_translate("MainWindow_fe", "BACK"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_fe = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_fe()
    ui.setupUi(MainWindow_fe)
    MainWindow_fe.show()
    sys.exit(app.exec_())
