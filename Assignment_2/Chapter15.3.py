def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

try:
    m = int(input("Enter the first integer: "))
    n = int(input("Enter the second integer: "))
    result = gcd(m, n)
    print(f"The GCD of {m} and {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
