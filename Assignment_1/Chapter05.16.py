n1, n2 = eval(input("Enter 2 numbers : "))
d=0
if n1<n2:
    d=n1
else:
    d=n2
for i in range(d,1,-1):
    if n1%i==0 and n2%i==0:
        print("Greatest Common Divisor :",i)
        break
