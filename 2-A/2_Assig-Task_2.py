# Initialize the sum variable

total_sum = 0


# Use a for loop to iterate over numbers from 1 to 50

for number in range(1, 51):
    total_sum += number


# Display the final sum

print(f"The sum of numbers from 1 to 50 is: {total_sum}")




# or else you can do it...


'''

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Initialize the sum variable
total_sum = 0

# Use a for loop to iterate over numbers from 1 to 50
for number in range(1, 51):
    total_sum += number

# Display the final sum with colored text
print(Fore.YELLOW + "The sum of numbers from " + Fore.CYAN + "1" + Fore.YELLOW + " to " + Fore.MAGENTA + "50" + Fore.YELLOW + " is: " + Fore.RED + str(total_sum))


'''
