# Take input from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate the first and last name into a full name
full_name = first_name + " " + last_name

# Print the personalized greeting message
print(f"\nHello, {full_name}! Welcome to the Python program.")




# or else you can do this also

'''

# Function to take user's first and last name as input
def get_full_name():
    # Taking input from the user
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Returning the full name
    return first_name, last_name

# Main program
def main():
    # Get the full name from the user
    first_name, last_name = get_full_name()

    # Concatenate the first and last name into a full name
    full_name = first_name + " " + last_name

    # Print the personalized greeting message
    print(f"\nHello, {full_name}! Welcome to the Python program.")

# Run the main program
if __name__ == "__main__":
    main()


'''