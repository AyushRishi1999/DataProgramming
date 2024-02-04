def remove_string_from_file(file_name, string_to_remove):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        updated_content = content.replace(string_to_remove, '')
        with open(file_name, 'w') as file:
            file.write(updated_content)
        print(f"All occurrences of '{string_to_remove}' removed from {file_name}.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except IOError:
        print(f"Error reading or writing file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = input("Enter the filename: ")
string_to_remove = input("Enter the string to be removed: ")
remove_string_from_file(file_name, string_to_remove)
