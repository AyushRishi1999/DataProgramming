def countVowelsAndConsonants(content):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    vowelCount = consonantCount = 0

    for char in content:
        if char.upper() in vowels:
            vowelCount += 1
        elif char.isalpha():
            consonantCount += 1

    return vowelCount, consonantCount

fileName = input("Enter the filename: ")
try:
    with open(fileName, 'r') as file:
        content = file.read()
    vowels, consonants = countVowelsAndConsonants(content)
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")

except FileNotFoundError:
    print(f"File '{fileName}' not found.")
except IOError:
    print(f"Error reading file '{fileName}'.")
except Exception as e:
    print(f"An error occurred: {e}")
