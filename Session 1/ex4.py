#simple calculator using functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
def modulo(x, y):
    if y == 0:
        return "Error! Modulo by zero."
    else:
        return x % y
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op=input("Enter an arithmetic operation(+ or - or * or / or %)")
if op == '+':
        print("Result:", add(num1, num2))
elif op == '-':
        print("Result:", subtract(num1, num2))
elif op == '*':
        print("Result:", multiply(num1, num2))
elif op == '/':
        print("Result:", divide(num1, num2))
elif op == '%':
        print("Result:", modulo(num1, num2))
else:
        print("Invalid input")