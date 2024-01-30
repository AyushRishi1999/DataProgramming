def displaySortedNumbers(num1,num2,num3):
    if num1>num2:
        num1,num2=num2,num1
    if num2>num3:
        num2,num3=num3,num2
    if num1>num2:
        num1,num2=num2,num1
    return num1,num2,num3

n1,n2,n3 = eval(input("Enter three numbers "))
print("The sorted numbers are",displaySortedNumbers(n1,n2,n3))

