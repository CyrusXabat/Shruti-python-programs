
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print("Reading file content:")
            for index, line in enumerate(file, start=1):
                print(f"Line {index}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")


# Call the function with the file name

read_file('sample.txt')

