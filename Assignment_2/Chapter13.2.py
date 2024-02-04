def countCharactersWordslLines(name):
    try:
        with open(name, 'r') as file:
            content = file.read()
        charCount = len(content)
        wordCount = len(content.split())
        lineCount = content.count('\n') + 1
        print(f"Number of characters: {charCount}")
        print(f"Number of words: {wordCount}")
        print(f"Number of lines: {lineCount}")

    except FileNotFoundError:
        print(f"File '{name}' not found.")
    except IOError:
        print(f"Error reading file '{name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

name = input("Enter the filename: ")
countCharactersWordslLines(name)
