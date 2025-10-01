requirements = {
    "must have"   : {
        "functions" : ["add", "subtract", "multiply", "division", "modulus"],
        "input_handling" : ["select an operation", "input two numbers", "converting data types"],
        "conditional_logic" : ["if", "elif", "else"],
        "output_formatting" : "clear and readable format",
        "error_handling" : ["division by zero", "informative error messages"]
    },
    "should not use" : ["external libraries", "frameworks"]
}

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            result = modulus(num1, num2)
            print(f"{num1} % {num2} = {result}")
    else:
        print("Invalid input. Please select a valid operation with selecting the options available between 1 to 5.")


calculator()