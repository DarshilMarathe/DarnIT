
from PyQt5 import QtCore, QtGui, QtWidgets

from answers import Ui_answer_Dialog


class Ui_MainWindow_faq(object):
    def open_ans(self,quest_no,answer):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_answer_Dialog()
        self.ui.setupUi_ans(self.window,quest_no,answer)
        self.window.show()
    def go_back(self,MainWindow_faq):
        MainWindow_faq.hide()
    def setupUi_faq(self, MainWindow):
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
"font: 22pt \"Artifakt Element\";\n"
"background : transparent;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.back = QtWidgets.QPushButton(self.centralwidget,clicked = lambda :self.go_back(MainWindow))
        self.back.setGeometry(QtCore.QRect(20, 20, 131, 61))
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
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 99, 1280, 691))
        self.scrollArea.setMinimumSize(QtCore.QSize(1280, 680))
        self.scrollArea.setStyleSheet("background : transparent;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1257, 2238))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setMinimumSize(QtCore.QSize(0, 2220))
        self.frame.setStyleSheet("background : transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 1231, 121))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 160, 1231, 121))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 300, 1231, 91))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 410, 1231, 91))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(0, 520, 1231, 121))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(0, 660, 1231, 151))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(0, 830, 1231, 101))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(0, 950, 1231, 101))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(0, 1070, 1231, 101))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(0, 1190, 1231, 101))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(0, 1310, 1231, 81))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(0, 1410, 1231, 251))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(0, 1680, 1231, 161))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(0, 1860, 1231, 161))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(0, 2040, 1231, 161))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Artifakt Element\";\n"
"background : transparent;\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.ans1 = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_ans(1,1))
        self.ans1.setGeometry(QtCore.QRect(1060, 60, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans1.setFont(font)
        self.ans1.setAutoFillBackground(False)
        self.ans1.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans1.setObjectName("ans1")
        self.ans2 = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_ans(2,2))
        self.ans2.setGeometry(QtCore.QRect(1060, 190, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans2.setFont(font)
        self.ans2.setAutoFillBackground(False)
        self.ans2.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans2.setObjectName("ans2")
        self.ans3 = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_ans(3,3))
        self.ans3.setGeometry(QtCore.QRect(1060, 320, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans3.setFont(font)
        self.ans3.setAutoFillBackground(False)
        self.ans3.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans3.setObjectName("ans3")
        self.ans4 = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_ans(4,4))
        self.ans4.setGeometry(QtCore.QRect(1060, 430, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans4.setFont(font)
        self.ans4.setAutoFillBackground(False)
        self.ans4.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans4.setObjectName("ans4")
        self.ans5 = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_ans(5,5))
        self.ans5.setGeometry(QtCore.QRect(1060, 560, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans5.setFont(font)
        self.ans5.setAutoFillBackground(False)
        self.ans5.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans5.setObjectName("ans5")
        self.ans6 = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_ans(6,6))
        self.ans6.setGeometry(QtCore.QRect(1060, 680, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans6.setFont(font)
        self.ans6.setAutoFillBackground(False)
        self.ans6.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans6.setObjectName("ans6")
        self.ans7 = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_ans(7,7))
        self.ans7.setGeometry(QtCore.QRect(1060, 850, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans7.setFont(font)
        self.ans7.setAutoFillBackground(False)
        self.ans7.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans7.setObjectName("ans7")
        self.ans8 = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_ans(8,8))
        self.ans8.setGeometry(QtCore.QRect(1060, 970, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans8.setFont(font)
        self.ans8.setAutoFillBackground(False)
        self.ans8.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans8.setObjectName("ans8")
        self.ans9 = QtWidgets.QPushButton(self.frame,clicked = lambda : self.open_ans(9,9))
        self.ans9.setGeometry(QtCore.QRect(1060, 1090, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans9.setFont(font)
        self.ans9.setAutoFillBackground(False)
        self.ans9.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans9.setObjectName("ans9")
        self.ans10 = QtWidgets.QPushButton(self.frame)
        self.ans10.setGeometry(QtCore.QRect(1060, 1210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans10.setFont(font)
        self.ans10.setAutoFillBackground(False)
        self.ans10.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans10.setObjectName("ans10")
        self.ans11 = QtWidgets.QPushButton(self.frame)
        self.ans11.setGeometry(QtCore.QRect(1060, 1320, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans11.setFont(font)
        self.ans11.setAutoFillBackground(False)
        self.ans11.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans11.setObjectName("ans11")
        self.ans12 = QtWidgets.QPushButton(self.frame)
        self.ans12.setGeometry(QtCore.QRect(1060, 1530, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans12.setFont(font)
        self.ans12.setAutoFillBackground(False)
        self.ans12.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans12.setObjectName("ans12")
        self.asn13 = QtWidgets.QPushButton(self.frame)
        self.asn13.setGeometry(QtCore.QRect(1060, 1730, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.asn13.setFont(font)
        self.asn13.setAutoFillBackground(False)
        self.asn13.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.asn13.setObjectName("asn13")
        self.ans14 = QtWidgets.QPushButton(self.frame)
        self.ans14.setGeometry(QtCore.QRect(1060, 1910, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans14.setFont(font)
        self.ans14.setAutoFillBackground(False)
        self.ans14.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans14.setObjectName("ans14")
        self.ans15 = QtWidgets.QPushButton(self.frame)
        self.ans15.setGeometry(QtCore.QRect(1060, 2080, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ans15.setFont(font)
        self.ans15.setAutoFillBackground(False)
        self.ans15.setStyleSheet("background-color:#4CAF50;\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"\n"
"")
        self.ans15.setObjectName("ans15")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.yt = QtWidgets.QPushButton(self.centralwidget)
        self.yt.setGeometry(QtCore.QRect(1080, 20, 191, 61))
        self.yt.setStyleSheet("background-color:rgb(234, 51, 34);\n"
"color:rgb(255, 255, 255);\n"
"font: 14pt \"Artifakt Element\";\n"
"border : outset ;\n"
"border-width : 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius : 15px")
        self.yt.setObjectName("yt")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("C:\\Users\\darsh\\Downloads\\DarnIT-main (1)\\DarnIT-main\\DARN IT\\pictures\\try2-dark-stripes-background-elegant-design-wallpapers_518299-1505.jpg"))
        self.label_19.setObjectName("label_19")
        self.label_19.raise_()
        self.title.raise_()
        self.back.raise_()
        self.scrollArea.raise_()
        self.yt.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DARN IT"))
        self.title.setText(_translate("MainWindow", "FAQ\'S"))
        self.back.setText(_translate("MainWindow", "BACK"))
        self.label_2.setText(_translate("MainWindow", "Q1-Compare Bus and Star topology ?\n"
"     -Compare Ring and Star topology ?\n"
"     -Is there any relationship between transmission media and topology ?"))
        self.label_3.setText(_translate("MainWindow", "Q2-Draw  and explain the OSI Reference Model ?\n"
"     -What is the OSI Model? Give functions and services of each layer ?\n"
"     -What is OSI model , explain functions , services and protocols of each layer ?"))
        self.label_4.setText(_translate("MainWindow", "Q3-What is congestion and what are its causes? Explain Token bucket algorithm ?\n"
"     -How congestion is controlled in TCP ?"))
        self.label_5.setText(_translate("MainWindow", "Q4-Header format of IPv4 ?"))
        self.label_6.setText(_translate("MainWindow", "Q5-Compare wired and wireless media ?\n"
"     -Explain the different transmission media in networking ?\n"
"     -Explain guided transmission media in detail ?"))
        self.label_7.setText(_translate("MainWindow", "Q6-Explain ALOHA and Slotted ALOHA ?\n"
"    -Examine different types of ALOHA ?\n"
"    -What is pure ALOHA and slotted ALOHA , what is efficiency , justify your answer ?\n"
"    -Compare pure and slotted ALOHA ?"))
        self.label_8.setText(_translate("MainWindow", "Q7-What is HDLC , Compare frame formats,I frame , S frame , U frame ?\n"
"    -Explain HDLC protocol along with its frame structure ?   "))
        self.label_9.setText(_translate("MainWindow", "Q8-Explain IP address and subnet mask ?\n"
"    -What is IP addressing?How it is classified?How is subnet addressing performed ?"))
        self.label_10.setText(_translate("MainWindow", "Q9-Explain CSMA/CD ?\n"
"    -What is p persistant CSMA ?"))
        self.label_11.setText(_translate("MainWindow", "Q10-Compare LAN,MAN,WAN ?\n"
"    -Examine advantages of LAN,MAN,WAN ?"))
        self.label_12.setText(_translate("MainWindow", "Q11-Compare TCP and UDP ?"))
        self.label_13.setText(_translate("MainWindow", "Q12-Suppose you develop a error recovery protocol for a link that is unreliable and delay sensitive ,\n"
"     which of the following protocol you wold choose -\n"
"     1)stop and wait \n"
"     2) selective repeat \n"
"     3)Go back?\n"
"    -What is difference between stop and wait and sliding window protocol ?\n"
"     Explain selective repeat protocol? "))
        self.label_14.setText(_translate("MainWindow", "Q13-Generate the CRC code for a dataword  110010101.The divisor 10101.\n"
"    -Check whether there are errors in the received codeword ?\n"
"     Short note on CRC and checksum ?"))
        self.label_15.setText(_translate("MainWindow", "Q14-What is routing in network , explain shortest routing path routing protocol ?\n"
"    -What are three main functions of network layer?What is routing ?\n"
"     What is shortest path routing ?"))
        self.label_16.setText(_translate("MainWindow", "Q15-Compare Message Switching and Circuit Switching ?\n"
"    -Diffrenciate between message switching , circuit switching and packet switching ?"))
        self.ans1.setText(_translate("MainWindow", "Answer"))
        self.ans2.setText(_translate("MainWindow", "Answer"))
        self.ans3.setText(_translate("MainWindow", "Answer"))
        self.ans4.setText(_translate("MainWindow", "Answer"))
        self.ans5.setText(_translate("MainWindow", "Answer"))
        self.ans6.setText(_translate("MainWindow", "Answer"))
        self.ans7.setText(_translate("MainWindow", "Answer"))
        self.ans8.setText(_translate("MainWindow", "Answer"))
        self.ans9.setText(_translate("MainWindow", "Answer"))
        self.ans10.setText(_translate("MainWindow", "Answer"))
        self.ans11.setText(_translate("MainWindow", "Answer"))
        self.ans12.setText(_translate("MainWindow", "Answer"))
        self.asn13.setText(_translate("MainWindow", "Answer"))
        self.ans14.setText(_translate("MainWindow", "Answer"))
        self.ans15.setText(_translate("MainWindow", "Answer"))
        self.yt.setText(_translate("MainWindow", "YouTube"))



if __name__ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_faq()
    ui.setupUi_faq(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())