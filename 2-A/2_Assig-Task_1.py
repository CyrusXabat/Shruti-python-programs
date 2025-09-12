# Take an integer input from the user

number = int(input("Enter a number: "))



# Check if the number is even or odd

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")




# or else you can do it...


'''

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Take an integer input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(Fore.BLUE + str(number) + Style.RESET_ALL + " is an even number.")
else:
    print(Fore.RED + str(number) + Style.RESET_ALL + " is an odd number.")

'''

