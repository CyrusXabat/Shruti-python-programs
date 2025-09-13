# Function to calculate the factorial of a number

def factorial(n):
    result = 1  # Start with 1
    for i in range(1, n + 1):  # Loop from 1 to n
        result *= i  # Multiply result by the current number
    return result  # Return the final result

# Main program

def main():
    # Take an integer input from the user
    number = int(input("Enter a number: "))
    # Call the factorial function and print the result
    print(f"Factorial of {number} is: {factorial(number)}")

# Run the main program

if __name__ == "__main__":
    main()

    