def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def calculator():
    print("Simple Calculator")

    # Input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display available operations
    print("\nChoose Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Input operation choice
    choice = input("Enter the operation needed : ")

    # Perform calculation based on user choice
    if choice == '+':
        result = add(num1, num2)
    elif choice == '-':
        result = subtract(num1, num2)
    elif choice == '*':
        result = multiply(num1, num2)
    elif choice == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operation choice."

    # Display the result
    print(f"\nResult: {result}")

if __name__ == "__main__":
    calculator()

