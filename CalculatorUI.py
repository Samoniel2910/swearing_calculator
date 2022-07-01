from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, \
    QGridLayout, QPushButton


class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Swearing Calculator')
        self.setFixedSize(500, 500)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)

        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()

        self.display.setFixedHeight(70)
        self.display.setAlignment(Qt.AlignLeft)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
                                   border-radius: 20px;
                                   font-size: 39px;
                                   padding-right: 15%;
                                   padding-left: 15%;
                                   font-weight: 900;
                                   border: 1px solid grey;
                                   """)

        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()

        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   }

        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(90, 90)
            self.buttons[btnText].setStyleSheet("""
                                                background-color: grey;
                                                color: white;
                                                border-radius: 20px;
                                                font-weight: 900;
                                                font-size: 30px;
                                                border: 1px solid rgb(110, 110, 110);
                                                """)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')