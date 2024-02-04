def binary_to_decimal(binary_string):
    if not binary_string:
        return 0
    else:
        last_digit = int(binary_string[-1])
        remaining_digits = binary_string[:-1]
        return last_digit + 2 * binary_to_decimal(remaining_digits)

num = input("Enter a binary string: ")

try:
    res = binary_to_decimal(num)
    print(f"The decimal equivalent of {num} is: {res}")
except ValueError:
    print("Invalid binary string. Please enter a valid binary string.")
