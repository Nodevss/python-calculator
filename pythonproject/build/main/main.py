from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QWidget
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("calculator lol")
        self.setGeometry(100, 100, 300, 400)

        # Set the window icon
        self.setWindowIcon(QIcon("icon.ico"))

        # Rest of your code...

        # Disable window resizing and maximizing
        self.setFixedSize(300, 400)

        # Set up the main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create the display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
            QLineEdit {
                font-size: 24px;
                padding: 10px;
                border: 1px solid #555;
                border-radius: 5px;
                background-color: #333;
                color: #eee;
            }
        """)
        self.layout.addWidget(self.display)

        # Create the button grid
        self.create_buttons()

    def create_buttons(self):
        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4)  # Span across 4 columns
        ]

        for text, row, col, *span in buttons:
            button = QPushButton(text)
            button.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    padding: 10px;
                    background-color: #444;
                    color: #eee;
                    border: 1px solid #555;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #555;
                }
                QPushButton:pressed {
                    background-color: #222;
                }
            """)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col, *(span or [1, 1]))

    def on_button_click(self):
        button_text = self.sender().text()

        if button_text == 'C':
            self.display.clear()
        elif button_text == '=':
            try:
                expression = self.display.text()
                result = eval(expression)  # Evaluate the expression
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            current_text = self.display.text()
            self.display.setText(current_text + button_text)

# Create the application
app = QApplication([])
app.setStyleSheet("""
    QMainWindow {
        background-color: #222;
    }
    QWidget {
        background-color: #222;
    }
""")
calculator = Calculator()
calculator.show()

# Run the application
app.exec()
