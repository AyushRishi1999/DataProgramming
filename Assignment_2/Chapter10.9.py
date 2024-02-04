import math

def mean(x):
    return sum(x) / len(x) if len(x) > 0 else 0

def deviation(x):
    x_mean = mean(x)
    squared_diff = [(xi - x_mean) ** 2 for xi in x]
    variance = sum(squared_diff) / len(x) if len(x) > 0 else 0
    std_deviation = math.sqrt(variance)
    return std_deviation

user_input = input("Enter a list of numbers, separated by spaces: ")

number_list = []
current_number = ""

for char in user_input:
    if char.isdigit() or char == '.' or (char == '-' and not current_number):
        current_number += char
    elif current_number:
        number_list.append(float(current_number))
        current_number = ""

if current_number:
    number_list.append(float(current_number))

if len(number_list) > 0:
    mean_value = mean(number_list)
    std_deviation_value = deviation(number_list)
    print(f"Mean: {mean_value:.2f}")
    print(f"Standard Deviation: {std_deviation_value:.2f}")
else:
    print("Please enter a valid list of numbers.")
