def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("Welcome to Calculator")
print("Operations:")
print("1. Addition '+' ")
print("2. Subtraction '-' ")
print("3. Multiplication '*' ")
print("4. Division '/'")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter your choice of operation: ")


if choice == '+':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '-':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '*':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '/':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")
