def binary_to_hex(binVal):
    hex_value = hex(int(binVal, 2))[2:]
    return hex_value

binVal = input("Enter a binary number: ")
res = binary_to_hex(binVal)
print(f"The hexadecimal value of the binary number {binVal} is: {res}")
