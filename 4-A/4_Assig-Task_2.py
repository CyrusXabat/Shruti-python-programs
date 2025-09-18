def write_and_append_to_file():
    # Step 1: Take user input and write it to the file
    text_to_write = input("Enter text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(text_to_write)
    print("Data successfully written to output.txt.")

    # Step 2: Append additional data to the file
    additional_text = input("\nEnter additional text to append: ")
    with open('output.txt', 'a') as file:
        file.write('\n' + additional_text)
    print("Data successfully appended.")

    # Step 3: Read and display the final content of the file
    with open('output.txt', 'r') as file:
        content = file.read()
    print("\nFinal content of output.txt:")
    print(content)

# Call the function to execute the program
write_and_append_to_file()