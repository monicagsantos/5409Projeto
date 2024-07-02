import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)
        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        self.grid_layout = QGridLayout()
        for row, button_row in enumerate(self.buttons):
            for col, button_text in enumerate(button_row):
                button = QPushButton(button_text)
                button.clicked.connect(self.button_clicked)
                self.grid_layout.addWidget(button, row, col)
        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)

    def button_clicked(self):
        button = self.sender()
        text = button.text()
        if text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())