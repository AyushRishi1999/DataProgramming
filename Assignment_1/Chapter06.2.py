def sumOfDigits(n):
    sum=0
    while(n>0):
        digit=n%10
        sum+=digit
        n=n//10
    return sum

num=eval(input("Enter a number : "))
sum=sumOfDigits(num)
print(sum)