import sys
from PyQt5 import QtWidgets
from calculator.calc import Calculator


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
