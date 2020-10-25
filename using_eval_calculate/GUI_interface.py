from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QLayout, QGridLayout


class Calculator(QWidget):

    def __init__(self, parent=None):  # Q parent의 의미
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        for i in range(10):
            self.digitButton[i] = QToolButton()
            self.digitButton[i].setText(str(i))

        # . and = Buttons
        self.decButton = QToolButton()
        self.decButton.setText('.')
        self.eqButton = QToolButton()
        self.eqButton.setText('=')

        # Operator Buttons
        self.mulButton = QToolButton()
        self.mulButton.setText('*')
        self.divButton = QToolButton()
        self.divButton.setText('/')
        self.addButton = QToolButton()
        self.addButton.setText('+')
        self.subButton = QToolButton()
        self.subButton.setText('-')

        # Parentheses Buttons
        self.lparButton = QToolButton()
        self.lparButton.setText('(')
        self.rparButton = QToolButton()
        self.rparButton.setText(')')

        # Clear Button
        self.clearButton = QToolButton()
        self.clearButton.setText('C')

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0], 3, 0)
        numLayout.addWidget(self.digitButton[1], 2, 0)
        numLayout.addWidget(self.digitButton[2], 2, 1)
        numLayout.addWidget(self.digitButton[3], 2, 2)
        numLayout.addWidget(self.digitButton[4], 1, 0)
        numLayout.addWidget(self.digitButton[5], 1, 1)
        numLayout.addWidget(self.digitButton[6], 1, 2)
        numLayout.addWidget(self.digitButton[7], 0, 0)
        numLayout.addWidget(self.digitButton[8], 0, 1)
        numLayout.addWidget(self.digitButton[9], 0, 2)

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()  # Q 이 부분이 추가된 이유
    sys.exit(app.exec_())
