#this program performs basic arithmetic operations based on user input

#this function performs the basic arithmetic operations
#It uses try and except to make sure the inputs are valid numbers
#And then validates the operation input to ensure it is one of the allowed operations
#Finally, it performs the operation and returns the result
def basic_operation(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Both inputs must be numbers."

    if operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1 - num2

    elif operation == "*":
        return num1 * num2

    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

    elif operation == "all":
        return {
            "Addition": num1 + num2,
            "Subtraction": num1 - num2,
            "Multiplication": num1 * num2,
            "Division": "Error: Dividing by zero is not allowed." if num2 == 0 else num1 / num2
        }

    else:
        return "Error: Operation must be '+', '-', '*', '/', or 'all'."

#this function returns the name of the operation for user-friendly output
#it validates the operation input and returns a descriptive name
def operation_name(operation):
    if operation == "+":
        return "addition"
    elif operation == "-":
        return "subtraction"
    elif operation == "*":
        return "multiplication"
    elif operation == "/":
        return "division"
    elif operation == "all":
        return "all the operations"
    else:
        return "Error: Invalid operation"

# user inputs, makes sure all is lower case
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /, all): ").lower()

# calls the functions and prints the result
print("-----------------------------")
print(f"For inputs {num1} and {num2}, the result of {operation_name(operation)} is:")
print(basic_operation(num1, num2, operation))