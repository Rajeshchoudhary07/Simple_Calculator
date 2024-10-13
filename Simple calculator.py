import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def smart_calculator():
    print(" Calculator:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Square root")
    print("8. Evaluate Expression")
    
    while True:

        choice = input("\nEnter your choice (1-8) or 'q' to quit: ")

        # Quit condition
        if choice.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice == '7':
            num = float(input("Enter the number: "))
            print(f"√{num} = {sqrt(num)}")

        # Evaluate mathematical expression directly
        elif choice == '8':
            expression = input("Enter the expression to evaluate: ")
            try:
                result = eval(expression)
                print(f"Result: {expression} = {result}")
            except Exception as e:
                print(f"Error evaluating expression: {e}")

        # For operations that need two operands
        else:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '6':
                print(f"{num1} ^ {num2} = {exponent(num1, num2)}")
            else:
                print("Invalid input! Please choose a valid operation.")

smart_calculator()
