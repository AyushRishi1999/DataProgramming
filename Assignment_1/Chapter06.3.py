def reverse(number):
    rev=0
    while number!=0:
        digit=number%10
        rev=(rev*10)+digit
        number=number//10
    return rev

def isPalindrome(number):
    if number==reverse(number):
        print("Palindrome")
    else:
        print("Not Palindrome")

num=eval(input("Enter a number : "))
isPalindrome(num)