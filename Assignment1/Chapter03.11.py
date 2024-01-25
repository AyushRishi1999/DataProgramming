num = eval(input("Enter an integer : "))
d1 = num%10
num //= 10
d2 = num%10
num //= 10
d3 = num%10
num //= 10
d4 = num%10
num //= 10
rev = (d1*1000)+(d2*100)+(d3*10)+d4
print("The reversed number is",rev)