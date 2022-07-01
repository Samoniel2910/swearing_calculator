import sys
from PyQt5.QtWidgets import QApplication

from CalculatorUI import *
from CalculatorCtrl import *


def main():
    pycalc = QApplication(sys.argv)

    view = CalculatorUI()
    view.show()

    model = evaluateExpression
    CalculatorCtrl(model=model, view=view)

    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()