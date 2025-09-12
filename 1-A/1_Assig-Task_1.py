# Take two numbers as input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Perform operations
add = a + b
sub = a - b
mul = a * b
div = a / b

# Display results
print("\nAddition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)


     #  or else you can do this


# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

# Display the results
print(f"\nAddition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")




    #or else you can do this also


'''
# Function to take two numbers as input from the user
def get_two_numbers():
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Returning the numbers as a tuple
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return get_two_numbers()  # Recursively call the function if input is invalid

# Function to perform mathematical operations
def perform_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "undefined (division by zero)"
    return addition, subtraction, multiplication, division

# Main program
def main():
    # Get the two numbers from the user
    number1, number2 = get_two_numbers()

    # Perform the operations
    add, sub, mul, div = perform_operations(number1, number2)

    # Display the results
    print(f"Addition: {add}")
    print(f"Subtraction: {sub}")
    print(f"Multiplication: {mul}")
    print(f"Division: {div}")

# Run the main program
if __name__ == "__main__":
    main()

'''