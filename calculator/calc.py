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


class Calculator(object):

    def __init__(self):
        self.main_window = self._create_main_window()
        self.central_widget = QtWidgets.QWidget(self.main_window)
        self.vl_widget, self.vl = self._create_vl()
        self.font = self._setup_font()
        self.display = self._create_display()
        self.gridLayout = QtWidgets.QGridLayout()
        self.buttons = self._create_btns()
        self.vl.addLayout(self.gridLayout)
        self.main_window.setCentralWidget(self.central_widget)

        for btn in self.buttons:
            btn.clicked.connect(lambda checked, btn=btn: self._pushed_btn(btn))

    def show(self): self.main_window.show()

    def _create_main_window(self):
        main_window = QtWidgets.QMainWindow()
        main_window.setWindowTitle('Calculator')
        main_window.setFixedSize(420, 400)
        main_window.setStyleSheet("background-color: rgb(0, 0, 0);")
        return main_window

    # Create Vertical Layout
    def _create_vl(self):
        vl_widget = QtWidgets.QWidget(self.central_widget)
        vl_widget.setGeometry(QtCore.QRect(10, 10, 403, 380))
        vl = QtWidgets.QVBoxLayout(vl_widget)
        vl.setContentsMargins(0, 0, 0, 0)
        return vl_widget, vl

    def _setup_font(self):
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        font.setWeight(50)
        return font

    def _create_btns(self) -> list[QtWidgets.QPushButton]:
        buttons = []

        for btn_name, coords in BUTTONS.items():
            new_button = QtWidgets.QPushButton(text=btn_name)
            new_button.setMinimumSize(QtCore.QSize(0, 75))
            new_button.setFont(self.font)
            new_button.setStyleSheet(
                "background-color: rgb(49, 49, 49);\n"
                "color: rgb(255, 255, 255);"
                )

            self.gridLayout.addWidget(new_button, *coords)
            buttons.append(new_button)
        return buttons


    def _create_display(self):
        display = QtWidgets.QLabel(self.vl_widget)
        display.setFont(self.font)
        display.setStyleSheet(
            "background-color: rgb(61, 61, 61);\n"
            "color: rgb(255, 255, 255);\n"
            "padding-right: 5"
            )
        display.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )
        display.setText('0')
        self.vl.addWidget(display)
        return display

    def _pushed_btn(self, btn):
        if btn.text() == 'C':
            self.display.setText('0')
            return

        elif btn.text() == '=':
            self._calculate_result()
            return

        elif self.display.text() == '':
            self.display.setText('0')
            return

        elif btn.text() == '<=':
            if len(self.display.text()) > 1:
                text = self.display.text()[:-1]
                self.display.setText(text)
                return
            else:
                self.display.setText('0')
                return

        elif (btn.text() in ['+', '-', '*', '/', '.']
                and self.display.text() == '0'):

            text = '0' + btn.text()
            self.display.setText(text)
            return

        elif not self.display.text():
            self.display.setText('0')
            return

        if (self.display.text() == '0'
                or any([x.isalpha() for x in self.display.text()])):

            self.display.setText('')

        text = self.display.text() + btn.text()
        self.display.setText(text)

    def _calculate_result(self):
        try:
            result = eval(self.display.text())
        except ZeroDivisionError:
            self.display.setText('Division by 0')
            return
        except (SyntaxError, TypeError, NameError):
            self.display.setText('Error')
            return

        if result == int(result):
            self.display.setText(str(int(result)))
        else:
            self.display.setText(str(result))
