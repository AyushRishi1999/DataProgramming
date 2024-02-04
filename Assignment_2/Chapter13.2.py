def count_characters_words_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        char_count = len(content)
        word_count = len(content.split())
        line_count = content.count('\n') + 1
        print(f"Number of characters: {char_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of lines: {line_count}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except IOError:
        print(f"Error reading file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = input("Enter the filename: ")
count_characters_words_lines(file_name)
