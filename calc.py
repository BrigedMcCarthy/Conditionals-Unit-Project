# Python calculator
# Briged McCarthy 2024

# Number input and operation input
num1 = float(input("Type the first number for your equation: "))
num2 = float(input("Type the second number for your equation: "))
operation = int(input("Choose your operation (1: addition, 2: subtraction, 3: multiplication, 4: division): "))

# Check if operation is valid using a Boolean
valid_operation = (operation >= 1 and operation <= 4)

if valid_operation:
    # Perform the operation based on user input
    if operation == 1:
        result = num1 + num2
    elif operation == 2:
        result = num1 - num2
    elif operation == 3:
        result = num1 * num2
    elif operation == 4:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "You cannot divide by zero!"
    
    print("Result: " + str(result))
else:
    print("Please choose 1, 2, 3, or 4.")
