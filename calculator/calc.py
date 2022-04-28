from PyQt5 import QtCore, QtGui, QtWidgets


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
    '<=': (3, 0, 1, 1),
    '.': (3, 2, 1, 1),
    'C': (3, 3, 1, 1),
    '=': (3, 4, 1, 1)
}


class BracketsMatchError(Exception): pass


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('Calculator')
        MainWindow.setFixedSize(420, 400)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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

    
    def _setup_font(self):
        self.font = QtGui.QFont()
        self.font.setFamily("Consolas")
        self.font.setPointSize(15)
        self.font.setWeight(50)
    
    def _create_btn(self, btn_name):
        button = QtWidgets.QPushButton(text=btn_name)
        button.setMinimumSize(QtCore.QSize(0, 75))
        button.setFont(self.font)
        button.setStyleSheet("background-color: rgb(49, 49, 49); color: rgb(255, 255, 255);")
        return button

    def _create_display(self):
        display = QtWidgets.QLabel(self.verticalLayoutWidget)
        display.setFont(self.font)
        display.setStyleSheet("background-color: rgb(61, 61, 61); color: rgb(255, 255, 255);")
        display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        display.setText('0')
        self.verticalLayout.addWidget(display)
        return display

    def _pushed_btn(self, btn):
        if btn.text() == 'C':
            self.display.setText('0')

        elif btn.text() == '=':
            self._calculate_result()

        elif btn.text() == '<=':
            text = self.display.text()[:-1]
            self.display.setText(text)
        
        elif btn.text() in ['+', '-', '*', '/', '.'] and self.display.text() == '0':
            text = '0' + btn.text()
            self.display.setText(text)

        else:
            if self.display.text() == '0' or self.display.text() == 'Division by 0' or self.display.text() == 'Error':
                self.display.setText('')
            
            text = self.display.text() + btn.text()
            self.display.setText(text)

        if self.display.text() == '':
            self.display.setText('0')


    def _calculate_result(self):
        try:
            if self.display.text().count('(') != self.display.text().count(')'):
                raise BracketsMatchError
            result = eval(self.display.text())
        except ZeroDivisionError:
            self.display.setText('Division by 0')
            return
        except (SyntaxError, TypeError, BracketsMatchError):
            self.display.setText('Error')
            return
        
        if result == int(result):
            self.display.setText(str(int(result)))
        else:
            self.display.setText(str(result))