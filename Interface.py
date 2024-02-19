from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import main

        

class Ui_MainWindow(object):
    
    
    
        
    def open_on_subit(self):
        #value of Pclass(Passenger class)
        selected_Pclass = self.Pclass.currentText()
        if selected_Pclass == 'Business class':
            pclass = 1
        elif selected_Pclass == 'Economy class':
            pclass = 2
        else:
            pclass = 3   
      
        #value of gender
        selected_gender = self.Gender.currentText()
        #gender = 1 if selected_gender == 'female' else 0
        if selected_gender == 'Female':
            gender = 1
        else:
            gender = 0    
        #value of age          
        age_value = self.Age.value()    
        #value of total number of passenger    
        nop_value = self.Nop.value()
        #value of parch(parent|childern)
        is_parent_selected = self.Parent.isChecked()
        
        if is_parent_selected == True:
            parch = nop_value - 1
        else:
            parch = 0
                
        #value of sibsp(spouse | sibbling)
        is_spouse_selected = self.Spouse.isChecked()
        #sibSp = (nop_value - 1) if is_spouse_selected == 'True' else 0
        if is_spouse_selected == True:
            sibSp = nop_value - 1
        else:
            sibSp = 0
            
        is_alone_selected = self.Alone.isChecked()
        if is_alone_selected == True:
            parch = 0
            sibSp = 0
               
        #value of fare    
        fare = np.random.randint(0,513) 
        #value of embarked place    
        embarked_value = self.Embarked.currentText()
        if embarked_value == 'Cherbourg':
            embarked = 1
        elif embarked_value =='Queenstown':
            embarked = 2
        else:
            embarked = 0    
            
        #my_list  = ['Pclass','Sex',  'age_value' ,  'sibSp' , 'parch' ,  'fare' , 'Embarked'] 
        
        main.perdiction_model([pclass,gender,  age_value ,  sibSp , parch ,  fare , embarked])
    
        
        # Get the age value
        #perform_analysis(age_value)
    import warnings

    warnings.filterwarnings("ignore", category=UserWarning)
        
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 563)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1021, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(110, 50, 781, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(28)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 180, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(550, 180, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 270, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(120, 340, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(120, 420, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lebel = QtWidgets.QLabel(self.frame)
        self.lebel.setGeometry(QtCore.QRect(550, 240, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.lebel.setFont(font)
        self.lebel.setObjectName("lebel")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(550, 340, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.Gender = QtWidgets.QComboBox(self.frame)
        self.Gender.setGeometry(QtCore.QRect(220, 270, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.Gender.setFont(font)
        self.Gender.setObjectName("Gender")
        self.Gender.addItem("")
        self.Gender.addItem("")
        self.Gender.addItem("")
        #selected_gender = self.Gender.currentText()


        self.Age = QtWidgets.QSpinBox(self.frame)
        self.Age.setGeometry(QtCore.QRect(220, 340, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.Age.setFont(font)
        self.Age.setMinimum(1)
        self.Age.setObjectName("Age")        

        
        
        self.Pclass = QtWidgets.QComboBox(self.frame)
        self.Pclass.setGeometry(QtCore.QRect(730, 180, 181, 22))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.Pclass.setFont(font)
        self.Pclass.setObjectName("Pclass")
        self.Pclass.addItem("")
        self.Pclass.addItem("")
        self.Pclass.addItem("")
        self.Pclass.addItem("")
        
        #parent | childern
        self.Parent = QtWidgets.QCheckBox(self.frame)
        self.Parent.setGeometry(QtCore.QRect(730, 240, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.Parent.setFont(font)
        self.Parent.setObjectName("Parent")
        
        #sibling | spouse
        self.Spouse = QtWidgets.QCheckBox(self.frame)
        self.Spouse.setGeometry(QtCore.QRect(730, 270, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.Spouse.setFont(font)
        self.Spouse.setObjectName("Spouse")
        
        self.Alone = QtWidgets.QCheckBox(self.frame)
        self.Alone.setGeometry(QtCore.QRect(730, 300, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.Alone.setFont(font)
        self.Alone.setObjectName("Alone")
        
        self.Embarked = QtWidgets.QComboBox(self.frame)
        self.Embarked.setGeometry(QtCore.QRect(720, 340, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.Embarked.setFont(font)
        self.Embarked.setObjectName("Embarked")
        self.Embarked.addItem("")
        self.Embarked.addItem("")
        self.Embarked.addItem("")
        self.Embarked.addItem("")
        #embarked_value = self.Embarked.currentText()
        
        self.Submit = QtWidgets.QPushButton(self.frame, clicked = lambda : self.open_on_subit())
        self.Submit.setGeometry(QtCore.QRect(560, 400, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        self.Submit.setFont(font)
        self.Submit.setObjectName("Submit")
        self.Nop = QtWidgets.QSpinBox(self.frame)
        self.Nop.setGeometry(QtCore.QRect(280, 420, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(8)
        #nop_value = self.Nop.value()
        
        self.Nop.setFont(font)
        self.Nop.setMinimum(1)
        self.Nop.setObjectName("Nop")
        
        self.Name = QtWidgets.QTextEdit(self.frame)
        self.Name.setGeometry(QtCore.QRect(200, 170, 261, 31))
        self.Name.setObjectName("Name")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 26))
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
        self.Title.setText(_translate("MainWindow", "What if you were in Titanic...?"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_7.setText(_translate("MainWindow", "Accomodation class"))
        self.label_3.setText(_translate("MainWindow", "Gender"))
        self.label_4.setText(_translate("MainWindow", "Age"))
        self.label_6.setText(_translate("MainWindow", "Number of people"))
        self.lebel.setText(_translate("MainWindow", "On vaccation with"))
        self.label.setText(_translate("MainWindow", "Embarking"))
        self.Gender.setItemText(0, _translate("MainWindow", "    ---Select---     "))
        self.Gender.setItemText(1, _translate("MainWindow", "Male"))
        self.Gender.setItemText(2, _translate("MainWindow", "Female"))
        self.Pclass.setItemText(0, _translate("MainWindow", "              ---Select---       "))
        self.Pclass.setItemText(1, _translate("MainWindow", "Business class"))
        self.Pclass.setItemText(2, _translate("MainWindow", "Economy class"))
        self.Pclass.setItemText(3, _translate("MainWindow", "Passenger class"))
        self.Parent.setText(_translate("MainWindow", "Parent"))
        self.Spouse.setText(_translate("MainWindow", "Spouse"))
        self.Alone.setText(_translate("MainWindow", "Alone"))
        self.Embarked.setItemText(0, _translate("MainWindow", "              ---Select---        "))
        self.Embarked.setItemText(1, _translate("MainWindow", "Cherbourg"))
        self.Embarked.setItemText(2, _translate("MainWindow", "Queenstown"))
        self.Embarked.setItemText(3, _translate("MainWindow", "Southampton"))
        self.Submit.setText(_translate("MainWindow", "Book Now"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
