def count_vowels_and_consonants(file_content):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    vowel_count = consonant_count = 0

    for char in file_content:
        if char.upper() in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1

    return vowel_count, consonant_count

file_name = input("Enter the filename: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
    vowels, consonants = count_vowels_and_consonants(content)
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except IOError:
    print(f"Error reading file '{file_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
