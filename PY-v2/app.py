import sys
import math
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QGridLayout, 
                             QLineEdit, QPushButton)
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt6 Pro Calculator')
        self.setFixedSize(400, 600)
        
        colors = {
            'bg': '#1e1e2e',
            'display_bg': '#313244',
            'text': '#cdd6f4',
            'btn_bg': '#45475a',
            'op_bg': '#89b4fa',
            'sci_bg': '#b4befe',
            'equal_bg': '#fab387',
            'clear_bg': '#f38ba8',
            'hover': '#585b70'
        }

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {colors['bg']};
            }}
            QLineEdit {{
                background-color: {colors['display_bg']};
                color: {colors['text']};
                border: 2px solid {colors['btn_bg']};
                padding: 15px;
                font-size: 36px;
                border-radius: 12px;
                font-weight: bold;
                margin-bottom: 10px;
            }}
            QPushButton {{
                background-color: {colors['btn_bg']};
                color: {colors['text']};
                border-radius: 10px;
                font-size: 16px;
                min-height: 60px;
                border: none;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {colors['hover']};
            }}
            QPushButton#op {{
                background-color: {colors['op_bg']};
                color: {colors['bg']};
                font-weight: bold;
            }}
            QPushButton#sci {{
                background-color: {colors['sci_bg']};
                color: {colors['bg']};
                font-style: italic;
            }}
            QPushButton#equal {{
                background-color: {colors['equal_bg']};
                color: {colors['bg']};
                font-weight: bold;
                font-size: 24px;
            }}
            QPushButton#clear {{
                background-color: {colors['clear_bg']};
                color: {colors['bg']};
                font-weight: bold;
            }}
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setPlaceholderText("0")
        layout.addWidget(self.display)

        # Buttons Grid
        grid = QGridLayout()
        grid.setSpacing(10)
        
        buttons = [
            ('sin', 0, 0, 'sci'), ('cos', 0, 1, 'sci'), ('tan', 0, 2, 'sci'), ('log', 0, 3, 'sci'),
            ('√', 1, 0, 'sci'), ('π', 1, 1, 'sci'), ('e', 1, 2, 'sci'), ('^', 1, 3, 'sci'),
            ('C', 2, 0, 'clear'), ('(', 2, 1, 'op'), (')', 2, 2, 'op'), ('÷', 2, 3, 'op'),
            ('7', 3, 0, 'num'), ('8', 3, 1, 'num'), ('9', 3, 2, 'num'), ('×', 3, 3, 'op'),
            ('4', 4, 0, 'num'), ('5', 4, 1, 'num'), ('6', 4, 2, 'num'), ('-', 4, 3, 'op'),
            ('1', 5, 0, 'num'), ('2', 5, 1, 'num'), ('3', 5, 2, 'num'), ('+', 5, 3, 'op'),
            ('0', 6, 0, 'num'), ('.', 6, 1, 'num'), ('DEL', 6, 2, 'clear'), ('=', 6, 3, 'equal'),
        ]

        for text, row, col, style in buttons:
            btn = QPushButton(text)
            btn.setObjectName(style)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(self.on_click)
            grid.addWidget(btn, row, col)

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_click(self):
        btn = self.sender()
        text = btn.text()
        current = self.display.text()

        if text == '=':
            try:
                expr = current.replace('×', '*').replace('÷', '/').replace('^', '**')
                safe_dict = {
                    'sin': lambda x: math.sin(math.radians(x)),
                    'cos': lambda x: math.cos(math.radians(x)),
                    'tan': lambda x: math.tan(math.radians(x)),
                    'log': math.log10,
                    '√': math.sqrt,
                    'π': math.pi,
                    'e': math.e
                }
                
                # scientific function parsing

                for key in safe_dict:
                    if key in expr and f"{key}(" not in expr:

                        val = expr.replace(key, '')
                        if val.replace('.','',1).isdigit():
                            expr = f"{key}({val})"

                result = eval(expr, {"__builtins__": None}, safe_dict)
                self.display.setText(str(round(result, 8)))
            except Exception:
                self.display.setText("Error")
        elif text == 'C':
            self.display.clear()
        elif text == 'DEL':
            self.display.setText(current[:-1])
        elif text in ['sin', 'cos', 'tan', 'log', '√']:
            self.display.setText(current + text + "(")
        else:
            self.display.setText(current + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
