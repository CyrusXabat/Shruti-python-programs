def demonstrate_list_slicing():

    # Step 1: Create a list of numbers from 1 to 10
    original_list = list(range(1, 11))

    # Step 2: Extract the first five elements from the list
    extracted_elements = original_list[:5]

    # Step 3: Reverse these extracted elements
    reversed_extracted_elements = extracted_elements[::-1]

    # Step 4: Print both the extracted list and the reversed list
    print("Original list:", original_list)
    print("Extracted first five elements:", extracted_elements)
    print("Reversed extracted elements:", reversed_extracted_elements)

# Call the function to execute the program
demonstrate_list_slicing()

