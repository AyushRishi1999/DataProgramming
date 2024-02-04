def count_letters(s):
    count = sum(c.isalpha() for c in s)
    return count

userInput = input("Enter a string: ")
result = count_letters(userInput)
print("Number of letters in the string:",result)
