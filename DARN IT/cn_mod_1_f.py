# -*- coding: utf-8 -*-
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector

class Ui_MainWindow_mod(object):

    def go_back(self, MainWindow_mod):
        MainWindow_mod.hide()

    def setupUi_mod(self, MainWindow,mod_no,year,marks):
        print("year is " + str(year))
        print("marks is " + str(marks))
        print("module is " + str(mod_no))
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="yourdatabase")
        mycursor = mydb.cursor()
        if mod_no == 7:
            mycursor.execute("SELECT * FROM cnquestions")                
        elif year == 0 and marks == 0:
            mycursor.execute("SELECT * FROM cnquestions where module = " + str(mod_no))    
        else :
            # //for now change for custom here
            mycursor.execute("SELECT * FROM cnquestions where module = "+ str(mod_no) +" and questionyear = "+str(year) + " and marks = " + str(marks))  
            # select * from cnquestions where module =2  and questionyear = 2016 and marks =5;              
        

        myresult = mycursor.fetchall()
        questions = []
        # maxxx=0
        for data in myresult:
            question = str(data[0]) +"? M-"+str(int(data[2])) + " ("+ str(data[3]) +"-"+ str(data[4])+")"
            questions.append(question)
            # maxxx = max(maxxx,len(question))

        mycursor.close()
        mydb.close()

        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\darsh\\Downloads\\DarnIT-main (1)\\DarnIT-main\\DARN IT\\pictures\\icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(300, 20, 660, 61))
        self.title.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 16pt \"Artifakt Element\";\n"
                                 "background : transparent;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.back = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.go_back(MainWindow))
        self.back.setGeometry(QtCore.QRect(20, 20, 151, 61))
        self.back.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                "color: rgb(255, 255, 255);\n"
                                "font: 16pt \"Artifakt Element\";\n"
                                "border : outset ;\n"
                                "border-width : 1px;\n"
                                "border-color: rgb(255, 255, 255);\n"
                                "border-radius : 15px;\n"
                                "\n"
                                "")
        self.back.setObjectName("back")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 99, 1280, 691))
        self.scrollArea.setMinimumSize(QtCore.QSize(1280, 680))
        self.scrollArea.setStyleSheet("background : transparent;\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1257, 5018))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        # if
        # self.frame.setMinimumSize(QtCore.QSize(5000,21000))
        self.frame.setStyleSheet("background : transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        num_questions = len(questions)
        for i in range(num_questions):
            label = QtWidgets.QLabel(self.frame)
            label.setGeometry(QtCore.QRect(0, i*110, 3000, 100))
            label.setStyleSheet("color: rgb(255, 255, 255);\n"
                         "font: 22pt \"Artifakt Element\";\n"
                         "background : transparent;\n"
                         "border : outset ;\n"
                         "border-width : 1px;\n"
                         "border-color: rgb(255, 255, 255);\n"
                         "border-radius:15px;\n")
            label.setAlignment(QtCore.Qt.AlignCenter)
            # chalochale = len(questions[i])
            self.frame.setMinimumSize(QtCore.QSize(8000,i*110))
            label.setObjectName(f"label_{i+2}")
            label.setText(f"Q{i+1}) "+questions[i])
            print(questions[i])
            label.setAlignment(QtCore.Qt.AlignLeft)
            label.setWordWrap(True)

        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.yt = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: webbrowser.open(
            'https://www.youtube.com/watch?v=JFF2vJaN0Cw&list=PLxCzCOWd7aiGFBD2-2joCpWOLUrDLvVV_'))  # just put the required url
        self.yt.setGeometry(QtCore.QRect(1050, 20, 221, 61))
        self.yt.setStyleSheet("background-color:rgb(234, 51, 34);\n"
                              "color:rgb(255, 255, 255);\n"
                              "font: 14pt \"Artifakt Element\";\n"
                              "border : outset ;\n"
                              "border-width : 1px;\n"
                              "border-color: rgb(255, 255, 255);\n"
                              "border-radius : 15px")
        self.yt.setObjectName("yt")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.label_19.setText("")
        self.label_19.setPixmap(
            QtGui.QPixmap("C:\\Users\\darsh\\Downloads\\DarnIT-main (1)\\DarnIT-main\\DARN IT\\pictures\\try2-dark-stripes-background-elegant-design-wallpapers_518299-1505.jpg"))
        self.label_19.setObjectName("label_19")
        self.label_19.raise_()
        self.title.raise_()
        self.back.raise_()
        self.scrollArea.raise_()
        self.yt.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow,mod_no)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow,mod_no):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DARN IT"))
        if (mod_no == 1):
            self.title.setText(_translate("MainWindow", "MODULE 1 :INTRODUCTION"))
        if (mod_no == 2):
            self.title.setText(_translate("MainWindow", "MODULE 2 :PHYSICAL LAYER AND DATA LINK LAYER"))
        if (mod_no == 3):
            self.title.setText(_translate("MainWindow", "MODULE 3 :NETWORK LAYER"))
        if (mod_no == 4):
            self.title.setText(_translate("MainWindow", "MODULE 4 :TRANSPORT LAYER AND SESSION LAYER"))
        if (mod_no == 5):
            self.title.setText(_translate("MainWindow", "MODULE 5 :PRESENTATION AND APPLICATION LAYER"))
        if (mod_no == 6):
            self.title.setText(_translate("MainWindow", "MODULE 6 :NETWORK DESIGN CONCEPTS"))
        if (mod_no == 7):
            self.title.setText(_translate("MainWindow", "MODULE 7 :ALL PYQ'S"))

        self.back.setText(_translate("MainWindow", "BACK"))
        self.yt.setText(_translate("MainWindow", "YouTube"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_mod()
    ui.setupUi_mod(MainWindow,1)
    MainWindow.show()
    sys.exit(app.exec_())
