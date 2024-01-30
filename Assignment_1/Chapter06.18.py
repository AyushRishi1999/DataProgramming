import random
def printMatrix(n):
    for i in range(0,n):
        for j in range(0,n):
            r=random.randint(0,1)
            print(r,end=' ')
        print()

n=eval(input("Enter n: "))
printMatrix(n)