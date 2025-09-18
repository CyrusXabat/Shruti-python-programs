def get_student_marks():
    # Step 1: Create a dictionary of student marks
    student_marks = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78,
        'David': 88
    }

    # Step 2: Ask the user to input a student's name
    student_name = input("Enter the student's name: ")

    # Step 3: Retrieve and display the corresponding marks or display a message if the student is not found
    if student_name in student_marks:
        print(f"{student_name}'s marks: {student_marks[student_name]}")
    else:
        print("Student not found.")

# Call the function to execute the program
get_student_marks()
