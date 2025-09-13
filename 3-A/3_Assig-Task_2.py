import math

# Main program
def main():
    # Ask the user for a number
    number = float(input("Enter a number: "))

    # Calculate the square root
    square_root = math.sqrt(number)

    # Calculate the natural logarithm
    natural_log = math.log(number)

    # Calculate the sine of the number (in radians)
    sine_value = math.sin(number)

    # Display the results
    print(f"Square root: {square_root}")
    print(f"Logarithm: {natural_log}")
    print(f"Sine: {sine_value}")

# Run the main program
if __name__ == "__main__":
    main()

