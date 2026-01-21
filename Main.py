import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 200)

        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Enter two numbers separated by comma")
        self.input_box.setFixedSize(280, 30)
        self.input_box.move(10, 10)

        self.result_label = QLabel("", self)
        self.result_label.setFixedSize(280, 30)
        self.result_label.move(10, 50)

        operations = [("Add", add), ("Subtract", subtract), ("Multiply", multiply), ("Divide", divide)]
        for i, (name, func) in enumerate(operations):
            btn = QPushButton(name, self)
            btn.setFixedSize(QSize(130, 40))
            btn.move((i % 2) * 140 + 10, 90 + (i // 2) * 50)
            btn.clicked.connect(lambda checked=False, f=func: self.calculate(f))

    def calculate(self, operation):
        text = self.input_box.text()
        try:
            a_str, b_str = text.split(",")
            a, b = float(a_str.strip()), float(b_str.strip())
            result = operation(a, b)
        except ValueError:
            result = "Error: enter two numbers separated by comma"
        except Exception as e:
            result = f"Error: {str(e)}"

        self.result_label.setText(f"Result: {result}")


#Test again
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "cannot divide by 0"
    return a / b 

def multiply(a, b):
    if b == 0:
        return "cannot divide by 0"
    return b * a


def operation(op, a, b):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    

# main loop of program
app = QApplication(sys.argv)

window = Calculator()
window.show()

app.exec()


# ans = None
# while True:
    
#     if ans != None:
#         first_num = ans
#         second_num = float(input("Enter number: "))
#         ans = operation(input("Enter operation (+, -, *, /): "), first_num, second_num)
#     else:
#         first_num = float(input("Enter first number: "))
#         second_num = float(input("Enter second number: "))
#         ans = operation(input("Enter operation (+, -, *, /): "), first_num, second_num)

#     print(f"Result: {ans}")


