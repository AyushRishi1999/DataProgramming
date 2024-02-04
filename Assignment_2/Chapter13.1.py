def removeStringFromFile(name, st):
    try:
        with open(name, 'r') as file:
            content = file.read()
        updatedContent = content.replace(st, '')
        with open(name, 'w') as file:
            file.write(updatedContent)
        print(f"All occurrences of '{st}' removed from {name}.")
    except FileNotFoundError:
        print(f"File '{name}' not found.")
    except IOError:
        print(f"Error reading or writing file '{name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

name = input("Enter the filename: ")
stringToRemove = input("Enter the string to be removed: ")
removeStringFromFile(name, stringToRemove)
