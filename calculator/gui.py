from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    
    def _setup_font(self):
        self.font = QtGui.QFont()
        self.font.setFamily("Consolas")
        self.font.setPointSize(15)
        self.font.setBold(False)
        self.font.setItalic(False)
        self.font.setWeight(50)
    
    def _create_btn(self, btn_name):
        button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        button.setMinimumSize(QtCore.QSize(0, 75))
        button.setFont(self.font)
        button.setStyleSheet("background-color: rgb(49, 49, 49); color: rgb(255, 255, 255);")
        button.setObjectName(btn_name)

        return button

    def _create_display(self):
        display = QtWidgets.QLabel(self.verticalLayoutWidget)
        display.setFont(self.font)
        display.setStyleSheet("background-color: rgb(61, 61, 61);color: rgb(255, 255, 255);")
        display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        display.setObjectName("display")
        self.verticalLayout.addWidget(display)
        return display


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 400)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 403, 380))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")


        self._setup_font()
        self.display = self._create_display()
        

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.btn_0 = self._create_btn('btn_0')
        self.btn_1 = self._create_btn('btn_1')
        self.btn_2 = self._create_btn('btn_2')
        self.btn_3 = self._create_btn('btn_3')
        self.btn_4 = self._create_btn('btn_4')
        self.btn_5 = self._create_btn('btn_5')
        self.btn_6 = self._create_btn('btn_6')
        self.btn_7 = self._create_btn('btn_7')
        self.btn_8 = self._create_btn('btn_8')
        self.btn_9 = self._create_btn('btn_9')
        self.btn_Lbracket = self._create_btn('btn_Lbracket')
        self.btn_Rbracket = self._create_btn('btn_Rbracket')
        self.btn_add = self._create_btn('btn_add')
        self.btn_clr = self._create_btn('btn_clr')
        self.btn_div = self._create_btn('btn_div')
        self.btn_mult = self._create_btn('btn_mult')
        self.btn_dot = self._create_btn('btn_dot')
        self.btn_pow = self._create_btn('btn_pow')
        self.btn_res = self._create_btn('btn_res')
        self.btn_sub = self._create_btn('btn_sub')

        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_Lbracket, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_Rbracket, 2, 4, 1, 1)
        self.gridLayout.addWidget(self.btn_add, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_clr, 3, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_div, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_mult, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.btn_dot, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_pow, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_res, 3, 4, 1, 1)
        self.gridLayout.addWidget(self.btn_sub, 0, 4, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.btn_0.clicked.connect(lambda: self.pushed_btn(self.btn_0))
        self.btn_1.clicked.connect(lambda: self.pushed_btn(self.btn_1))
        self.btn_2.clicked.connect(lambda: self.pushed_btn(self.btn_2))
        self.btn_3.clicked.connect(lambda: self.pushed_btn(self.btn_3))
        self.btn_4.clicked.connect(lambda: self.pushed_btn(self.btn_4))
        self.btn_5.clicked.connect(lambda: self.pushed_btn(self.btn_5))
        self.btn_6.clicked.connect(lambda: self.pushed_btn(self.btn_6))
        self.btn_7.clicked.connect(lambda: self.pushed_btn(self.btn_7))
        self.btn_8.clicked.connect(lambda: self.pushed_btn(self.btn_8))
        self.btn_9.clicked.connect(lambda: self.pushed_btn(self.btn_9))
        self.btn_Lbracket.clicked.connect(lambda: self.pushed_btn(self.btn_Lbracket))
        self.btn_Rbracket.clicked.connect(lambda: self.pushed_btn(self.btn_Rbracket))
        self.btn_add.clicked.connect(lambda: self.pushed_btn(self.btn_add))
        self.btn_clr.clicked.connect(self.clear_display)
        self.btn_div.clicked.connect(lambda: self.pushed_btn(self.btn_div))
        self.btn_mult.clicked.connect(lambda: self.pushed_btn(self.btn_mult))
        self.btn_dot.clicked.connect(lambda: self.pushed_btn(self.btn_dot))
        self.btn_pow.clicked.connect(lambda: self.pushed_btn(self.btn_pow))
        self.btn_res.clicked.connect(lambda: self.pushed_btn(self.btn_res))
        self.btn_sub.clicked.connect(lambda: self.pushed_btn(self.btn_sub))
        
    


    def pushed_btn(self, btn):
        text = self.display.text() + btn.text()
        self.display.setText(text)

    def clear_display(self):
        self.display.setText('0')



    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.display.setText(_translate("MainWindow", "0"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_Rbracket.setText(_translate("MainWindow", ")"))
        self.btn_res.setText(_translate("MainWindow", "="))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_clr.setText(_translate("MainWindow", "C"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_pow.setText(_translate("MainWindow", "^"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_Lbracket.setText(_translate("MainWindow", "("))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_3.setText(_translate("MainWindow", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
