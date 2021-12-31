from PyQt5 import QtCore, QtGui, QtWidgets#import widgets from pyqt5 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import random#import for random numbers
import sqlite3#import for databse

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942, 728)#to resize the window size
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 250, 121, 41))#to increase the size of the widget
        font = QtGui.QFont()
        font.setPointSize(14)#increase the font
        font.setBold(True)#to make it bold
        font.setWeight(75)#increase the font weight
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 330, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 400, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 480, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(242, 260, 201, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 30, 821, 151))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"background-color: rgb(27, 21, 21);")#to change the color of the widget
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(60, 30, 711, 91))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")#change the font
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 340, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  #to convert normal text to encoded text like "text"--->"*****"
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 410, 201, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 490, 201, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 580, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submit)#connect to the function submit
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(525, 255, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(642, 265, 201, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(525, 320, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(645, 330, 201, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 580, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.search)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(510, 400, 350, 125))
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(470, 200, 20, 441))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, 200, 20, 441))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Website"))
        self.label_4.setText(_translate("MainWindow", "Keyword"))
        self.label_5.setText(_translate("MainWindow", "  PASSWORD MANAGER"))
        self.pushButton.setText(_translate("MainWindow", "Submit "))
        self.label_6.setText(_translate("MainWindow", "Website"))
        self.label_7.setText(_translate("MainWindow", "Passcode"))
        self.pushButton_2.setText(_translate("MainWindow", " Search "))
        
    

    def submit(self):
 
        user = self.lineEdit.text()#to retrive text from user input we use ".text()"

        passc = self.lineEdit_2.text()

        web = self.lineEdit_3.text()

        key = self.lineEdit_4.text()
 
        hasnum = False#make to bool to check the base conditions
        hasup = False
        haslo = False
        haspecial = False
        haslen = len(passc)>=8#if length of pass is > 8 it will return True or else False
        special_characters = "!@#$%^&*()?/"
        for i in range(len(passc)):      
            c = passc[i]
            if c.isdigit():#used to see whether a given character is number or not
                hasnum = True
            elif c.isupper():#used to see whether a given character is capitalized
                hasup = True
            elif c.islower():#used to see whether a given character is not capitalized
                haslo = True
            elif c in special_characters:#used to see whether a given character conatins special character
                haspecial = True
        if hasnum==True and hasup==True and haslo==True and haspecial==True and haslen==True:#checks wheter the given password has passed all the above conditions
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Entry Successful")#to set a text in Qmessagebox
            msgBox.setWindowTitle("Password Manager")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            conn = sqlite3.connect('password.sqlite')#connection with database
            cur = conn.cursor()
            task = (user,passc,web)
            cur.execute('INSERT INTO pass (user,pass,web) values (?,?,?)',task)#to insert the values in the database by passing task var
            conn.commit()#to commit changes
            conn.close()
        else:
            special="!@#$%^&*()?/"
            suggest=""
            i=0
            while i<4:
                while len(key)<8:#to check whether given keyword by the user has len >8
                    key=key+chr(random.randint(ord('a'),ord('z')))#generates a Alphabet using random numbers generated with a range of ASCII Values
                key+=str(random.randint(0,9))
                key+=str(random.choice(special))#used to generate a char in a specfic set of elements
                key=key.capitalize()#to capitalize first letter of word
                suggest+=key+'\n'
                i=i+1
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Password Manager")
            msgBox.setText("Your password didn't meet the standards.")
            s="Your password should meet the conditions mentions below \n 1. At least 1 Uppercase \n 2. At least 1 lower case \n 3. At least 1 number \n 4. At least 1 special character \n 5. At least 8 characters."
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.setInformativeText("Password Suggestions: "+str(suggest))#show a msg in the qmsg box
            msgBox.setDetailedText(s)#to create a hide details option in the msg box
            returnValue = msgBox.exec()
    def search(self):

        paz = self.lineEdit_6.text()

        we = self.lineEdit_5.text()
        
        if paz=='root':#if users enters root only the search buttons works
            

            conn = sqlite3.connect('password.sqlite')
            cur = conn.cursor()
            cur.execute("SELECT * FROM pass WHERE web=?",[we])#fetching username and password using website name

            rows = cur.fetchall()

            for row in rows:
                print(row)
            self.textEdit.setText(" Username \t Password \n\n "+str(rows[-1][0])+" \t "+str(rows[-1][1]))
            
            conn.commit()
            conn.close()

        
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle("Password Manager")
            msgBox.setText("Wrong password. Please try again!!")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
            returnValue = msgBox.exec()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
