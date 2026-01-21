import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 300)

        for i in range(9):
            index = i + 1
            btn = QPushButton(str(index), self)
            btn.setFixedSize(QSize(100, 100))
            btn.move((i % 3) * 100, (i // 3) * 100)
            btn.clicked.connect(lambda checked=False, idx=index: self.onPress(idx))

    def onPress(self, num):
        print(num)



def add(a, b):
    pass

def subtract(a, b):
    pass

def divide(a, b):
    pass

def multiply(a, b):
    pass


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


ans = None
while True:
    
    if ans != None:
        first_num = ans
        second_num = float(input("Enter number: "))
        ans = operation(input("Enter operation (+, -, *, /): "), first_num, second_num)
    else:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        ans = operation(input("Enter operation (+, -, *, /): "), first_num, second_num)

    print(f"Result: {ans}")


