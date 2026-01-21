import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontMetrics
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QSizePolicy
)

# ==========================================
# LOGIC SECTION: PURE MATH OPERATIONS
# ==========================================
class CalculatorOperations:
    """Handles the core math logic, separated from the UI."""
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def calculate(self, left_operand, operator, right_operand):
        """Routes the operation to the correct function."""
        # Convert strings to floats for calculation
        try:
            a = float(left_operand)
            b = float(right_operand)
        except ValueError:
            return "Error"

        try:
            if operator == "+":
                return self.add(a, b)
            elif operator == "−" or operator == "-": # Handle both hyphen and minus symbol
                return self.subtract(a, b)
            elif operator == "×" or operator == "*":
                return self.multiply(a, b)
            elif operator == "÷" or operator == "/":
                return self.divide(a, b)
            else:
                return "Error"
        except ZeroDivisionError:
            return "Cannot divide by zero"
        except Exception:
            return "Error"

# ==========================================
# UI SECTION: LAYOUT AND EVENT HANDLING
# ==========================================
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize the separated logic class
        self.logic = CalculatorOperations()

        self.setWindowTitle("Calculator")
        self.setFixedSize(320, 430) 
        
        central = QWidget()
        self.setCentralWidget(central)
        central.setStyleSheet("background-color: #202020;") 

        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        central.setLayout(main_layout)

        # --- Top Section (Display) ---
        self.display_container = QWidget()
        self.display_container.setFixedHeight(110)
        
        display_layout = QVBoxLayout()
        display_layout.setContentsMargins(0, 0, 0, 0)
        display_layout.setSpacing(0)
        self.display_container.setLayout(display_layout)

        self.history_label = QLabel("")
        self.history_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.history_label.setFixedHeight(30)
        self.history_label.setStyleSheet("color: #a0a0a0; font-family: 'Segoe UI'; font-size: 14px; padding-right: 15px;")
        display_layout.addWidget(self.history_label)

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.display.setFont(QFont('Segoe UI Semibold', 36))
        self.display.setStyleSheet("""
            QLabel {
                color: white; 
                padding-right: 10px;
                padding-bottom: 5px;
            }
        """)
        display_layout.addWidget(self.display)

        main_layout.addWidget(self.display_container)

        # --- Bottom Section (Buttons) ---
        self.buttons_container = QWidget()
        
        buttons_layout = QGridLayout()
        buttons_layout.setSpacing(3)
        buttons_layout.setContentsMargins(4, 0, 4, 4) 
        self.buttons_container.setLayout(buttons_layout)

        buttons = [
            ("CE", 0, 0, "func"), ("C", 0, 1, "func"), ("⌫", 0, 2, "func"), ("÷", 0, 3, "op"),
            ("7", 1, 0, "num"),   ("8", 1, 1, "num"),   ("9", 1, 2, "num"),   ("×", 1, 3, "op"),
            ("4", 2, 0, "num"),   ("5", 2, 1, "num"),   ("6", 2, 2, "num"),   ("−", 2, 3, "op"),
            ("1", 3, 0, "num"),   ("2", 3, 1, "num"),   ("3", 3, 2, "num"),   ("+", 3, 3, "op"),
            ("+/-", 4, 0, "num"), ("0", 4, 1, "num"),   (".", 4, 2, "num"),   ("=", 4, 3, "equals"),
        ]

        self.waiting_for_operand = False 

        for text, row, col, type_ in buttons:
            btn = QPushButton(text)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.clicked.connect(self.on_button_click)
            
            if type_ == "num":
                btn.setStyleSheet(self.num_style())
            elif type_ == "op" or type_ == "func":
                btn.setStyleSheet(self.op_style())
            elif type_ == "equals":
                btn.setStyleSheet(self.equals_style())

            buttons_layout.addWidget(btn, row, col)

        main_layout.addWidget(self.buttons_container)

    def set_display_text(self, text):
        self.display.setText(text)
        self.adjust_font_size()

    def adjust_font_size(self):
        text = self.display.text()
        if not text: return
        current_size = 36
        font = self.display.font()
        font.setPointSize(current_size)
        available_width = self.display.width() - 20 
        metrics = QFontMetrics(font)
        while metrics.horizontalAdvance(text) > available_width and current_size > 12:
            current_size -= 2
            font.setPointSize(current_size)
            metrics = QFontMetrics(font)
        self.display.setFont(font)

    def format_number(self, value_str):
        if isinstance(value_str, (float, int)):
            value_str = f"{value_str:g}" # Convert raw number to string first

        if "Error" in value_str or "Inf" in value_str or "Cannot" in value_str: return value_str
        
        clean_val = value_str.replace(",", "")
        if clean_val == "" or clean_val == "-": return clean_val
        
        if "." in clean_val:
            parts = clean_val.split(".")
            integer_part = parts[0]
            decimal_part = parts[1] if len(parts) > 1 else ""
            
            if integer_part == "" or integer_part == "-":
                formatted_int = integer_part if integer_part else "0"
            else:
                try:
                    formatted_int = "{:,}".format(int(integer_part))
                except:
                    formatted_int = integer_part
            return f"{formatted_int}.{decimal_part}"
        else:
            try:
                return "{:,}".format(int(clean_val))
            except:
                return value_str

    def on_button_click(self):
        btn = self.sender()
        text = btn.text()
        current_text = self.display.text()
        # Clean commas for logic processing
        raw_current = current_text.replace(",", "")

        if "Error" in current_text or "Cannot" in current_text:
            current_text = "0"
            raw_current = "0"
            self.set_display_text("0")

        # --- Logic Handling ---

        if text == "C":
            self.set_display_text("0")
            self.history_label.setText("")
        elif text == "CE":
            self.set_display_text("0")
        elif text == "⌫":
            if len(raw_current) > 1:
                new_raw = raw_current[:-1]
                if new_raw == "-": new_raw = "0"
                self.set_display_text(self.format_number(new_raw))
            else:
                self.set_display_text("0")
        
        elif text.isdigit() or text == ".":
            if self.waiting_for_operand:
                self.set_display_text(text)
                self.waiting_for_operand = False
            else:
                digit_count = sum(c.isdigit() for c in raw_current)
                if digit_count < 16:
                    if raw_current == "0" and text != ".":
                        new_text = text
                    elif text == "." and "." in raw_current:
                        new_text = raw_current
                    else:
                        new_text = raw_current + text
                    self.set_display_text(self.format_number(new_text))
        
        elif text == "+/-":
            try:
                val = float(raw_current)
                new_val = val * -1
                self.set_display_text(self.format_number(new_val))
            except:
                pass
        
        elif text in ["+", "−", "×", "÷"]:
            if raw_current.endswith("."): raw_current = raw_current[:-1]
            self.history_label.setText(f"{self.format_number(raw_current)} {text}")
            self.waiting_for_operand = True
            
        elif text == "=":
            history = self.history_label.text()
            if not history or "=" in history: return 
            
            # Parse History: "1,234 +" -> ["1,234", "+"]
            parts = history.split(" ")
            if len(parts) < 2: return

            prev_val_str_fmt = parts[0]
            op = parts[1]
            
            # Clean inputs for math engine
            left_operand = prev_val_str_fmt.replace(",", "")
            right_operand = raw_current
            
            # === DELEGATE TO LOGIC CLASS ===
            result = self.logic.calculate(left_operand, op, right_operand)
            # ===============================

            self.history_label.setText(f"{prev_val_str_fmt} {op} {self.format_number(raw_current)} =")
            
            # If result is a number, format it. If error message, show as is.
            if isinstance(result, (float, int)):
                self.set_display_text(self.format_number(result))
            else:
                self.set_display_text(str(result))
            
            self.waiting_for_operand = True

    def num_style(self):
        return """
            QPushButton {
                background-color: #3b3b3b;
                color: white;
                font-family: 'Segoe UI';
                font-size: 16px;
                font-weight: bold;
                border-radius: 4px;
            }
            QPushButton:hover { background-color: #323232; }
            QPushButton:pressed { background-color: #282828; }
        """
    def op_style(self):
        return """
            QPushButton {
                background-color: #323232;
                color: white;
                font-family: 'Segoe UI';
                font-size: 16px;
                border-radius: 4px;
            }
            QPushButton:hover { background-color: #3b3b3b; }
            QPushButton:pressed { background-color: #282828; }
        """
    def equals_style(self):
        return """
            QPushButton {
                background-color: #76b9ed;
                color: #000000;
                font-family: 'Segoe UI';
                font-size: 20px;
                border: 1px solid #76b9ed;
                border-radius: 4px;
            }
            QPushButton:hover { background-color: #69a6d4; }
            QPushButton:pressed { background-color: #5a90b9; }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())