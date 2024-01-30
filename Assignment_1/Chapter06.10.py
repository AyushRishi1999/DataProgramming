def isPrime(number):
    c=0
    for i in range(2,number):
        if number%i==0:
            c+=1

    if c==0:
        return True
    else:
        return False

count = 0
for i in range(2,10000):
    if isPrime(i)==True:
        count+=1

print("Number of prime numbers till 10000 are",str(count))