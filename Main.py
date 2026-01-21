#TODO add UI

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


