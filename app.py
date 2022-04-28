import sys

from calculator.calc import Calculator, QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Calculator()
    ui.show()
    sys.exit(app.exec_())
