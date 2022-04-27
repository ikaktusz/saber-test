from PyQt5 import QtCore, QtGui, QtWidgets
import time


BUTTONS = {
    '0': (3, 1, 1, 1),
    '1': (2, 0, 1, 1),
    '2': (2, 1, 1, 1),
    '3': (2, 2, 1, 1),
    '4': (1, 0, 1, 1),
    '5': (1, 1, 1, 1),
    '6': (1, 2, 1, 1),
    '7': (0, 0, 1, 1),
    '8': (0, 1, 1, 1),
    '9': (0, 2, 1, 1),
    '(': (2, 3, 1, 1),
    ')': (2, 4, 1, 1),
    '+': (0, 3, 1, 1),
    '-': (0, 4, 1, 1),
    '/': (1, 3, 1, 1),
    '*': (1, 4, 1, 1),
    '^': (3, 0, 1, 1),
    '.': (3, 2, 1, 1),
    'C': (3, 3, 1, 1),
    '=': (3, 4, 1, 1)
}


class Ui_MainWindow(object):

    
    def _setup_font(self):
        self.font = QtGui.QFont()
        self.font.setFamily("Consolas")
        self.font.setPointSize(15)
        self.font.setWeight(50)

    '''def _create_main_window(self):
        MainWindow.setWindowTitle('Calculator')
        MainWindow.resize(420, 400)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)'''

    '''def _create_vertical_layout():
        verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 403, 380))
        verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        return '''
    
    def _create_btn(self, btn_name):
        button = QtWidgets.QPushButton(text=btn_name)
        button.setMinimumSize(QtCore.QSize(0, 75))
        button.setFont(self.font)
        button.setStyleSheet("background-color: rgb(49, 49, 49); color: rgb(255, 255, 255);")

        return button

    def _create_display(self):
        display = QtWidgets.QLabel(self.verticalLayoutWidget)
        display.setFont(self.font)
        display.setStyleSheet("background-color: rgb(61, 61, 61);color: rgb(255, 255, 255);")
        display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        display.setText('0')
        self.verticalLayout.addWidget(display)
        return display


    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('Calculator')
        MainWindow.resize(420, 400)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        '''self._create_main_window()
        self._create_vertical_layout()'''

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 403, 380))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)


        self._setup_font()
        self.display = self._create_display()
        

        self.gridLayout = QtWidgets.QGridLayout()

        self.buttons = []

        for btn_name, coords in BUTTONS.items():
            new_button = self._create_btn(btn_name)
            self.gridLayout.addWidget(new_button, *coords)
            self.buttons.append(new_button)


        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)


        for btn in self.buttons:
            btn.clicked.connect(lambda checked, btn=btn: self._pushed_btn(btn))        
    


    def _pushed_btn(self, btn):
        if btn.text() == 'C':
            self.display.setText('0')
        elif btn.text() == '=':
            try:
                result = eval(self.display.text())
            except ZeroDivisionError:
                self.display.setText('Division by 0')
                return
                
            self.display.setText(str(result))
        else:
            if self.display.text() == '0' or self.display.text() == 'Division by 0':
                self.display.setText('')
            text = self.display.text() + btn.text()
            self.display.setText(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
