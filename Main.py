# Define the calculator function
def calculator():
    print("Welcome to the calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operator (+,-,*,/): ")
    
    # Perform the calculation based on the operator
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Invalid operator!")
        return
    
    # Display the result
    print("Result:", result)

# Call the calculator function
calculator()
