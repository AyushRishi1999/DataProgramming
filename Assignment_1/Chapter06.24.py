def isPrime(number):
    c=0
    for i in range(2,number):
        if number%i==0:
            c+=1

    if c==0:
        return True
    else:
        return False

def isPalindrome(number):
    rev = 0
    temp=number
    while temp!=0:
        d=temp%10
        rev=(rev*10)+d
        temp=temp//10

    if rev == number:
        return True
    else:
        return False

count=0
n=2
while count<100:
    if isPrime(n) and isPalindrome(n):
        print(n,end=' ')
        count+=1
        if count%10==0:
            print()
        n+=1