def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

try:
    n = int(input("Enter an integer: "))
    result = sum_digits(abs(n))
    print(f"The sum of the digits in {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
