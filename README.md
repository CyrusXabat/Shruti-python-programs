# Shruti-python-programs

Assignment 1 
--------------------

Task 1      Functionality Description: 
------------------------------------------

1.  Taking Input:

Take two numbers as input from the user

The program prompts the user to enter two numbers. The input() function is used to take the input from the user, and int() is used to convert the input to an integer.

2.   Performing Mathematical Operations:

Addition: 
The program adds the two numbers using the + operator and stores the result in the addition variable.

Subtraction: 
The program subtracts the second number from the first number using the - operator and stores the result in the subtraction variable.

Multiplication: 
The program multiplies the two numbers using the * operator and stores the result in the multiplication variable.

Division: The program divides the first number by the second number using the / operator and stores the result in the division variable.


3.  Displaying the Results:

The program prints the results of each operation using the print() function. The results are displayed in a straightforward manner, showing the operation name followed by the result.



Task 2      Functionality Description:
-------------------------------------------

1.  Input:  Takes first and last names from the user.

2.  Concatenation:  Joins them into a full name.

3.  Output:  Displays a greeting using the full name.



Assignment 2 
-------------------------


Task 1    
---------------

1.  Input: The program uses the input function to get a number from the user and converts it to an integer using int().

2.  Check: The program uses an if-else statement to check if the number is even or odd. The condition number % 2 == 0 checks if the remainder when the number is divided by 2 is 0.

    *  If the condition is true, the number is even.
    *  If the condition is false, the number is odd.

3.  Output: The program prints the result using the print function.




Task 2     
----------------

1.   Initialization: The variable total_sum is initialized to 0. This variable will hold the running total of the numbers.

2.  Loop: The for loop iterates through each number from 1 to 50. For each number, it adds the number to total_sum.

3.  Output: After the loop finishes, the program prints the final sum.



Assignment 3 
----------------------

Task 1
----------

1.  Function Definition: The factorial function initializes a variable result to 1. It then uses a for loop to multiply result by each number from 1 to n (inclusive). Finally, it returns the calculated factorial.

2.   Main Program:

      *  The main function prompts the user to enter a number.
      *  It converts the input to an integer and calls the factorial function with this number.
      *  It prints the result returned by the factorial function.

  
Task 2
-----------

1.  Import the Math Module: The program imports the math module to access mathematical functions.

2.  Main Program:

   *  The main function prompts the user to enter a number and converts the input to a float.
   *  It calculates the square root using math.sqrt().
   *  It calculates the natural logarithm using math.log().
   *  It calculates the sine of the number using math.sin().
   *  It prints the results.



Assignments 4 
---------------------

Task 1 
---------

1.  Function Definition:

   *  The function read_file takes one parameter, file_name, which is the name of the file to be read.

2.  Try Block:

   *  The try block attempts to open the file using the open function.
   *  The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
   *  The for loop iterates over each line in the file using enumerate, which provides both the line number and the line content.
   *  line.strip() removes any leading or trailing whitespace, including the newline character at the end of each line.
   *  Each line is printed with its corresponding line number.

3.  Except Block:

   *  If the file does not exist, a FileNotFoundError is raised.
   *  The except block catches this error and prints an error message indicating that the file was not found.


Task 2 
---------

1.  Taking User Input and Writing to the File:

   *  The program prompts the user to enter text to write to the file.
   *  It opens the file in write mode ('w'), which creates the file if it does not exist or overwrites it if it does.
   *  The user input is written to the file.

2.  Appending Additional Data to the File:

   *  The program prompts the user to enter additional text to append to the file.
   *  It opens the file in append mode ('a'), which allows adding new data to the end of the file without overwriting the existing content.
   *  The additional user input is appended to the file.

3.  Reading and Displaying the Final Content of the File:

   *  The program opens the file in read mode ('r') to read its content.
   *  It reads the entire content of the file and prints it to the console.



