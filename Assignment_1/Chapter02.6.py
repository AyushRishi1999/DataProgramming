num = eval(input("Enter a number between 0 and 1000 : "))
temp = num
d1 = temp%10
temp = temp//10
d2 = temp%10
temp = temp//10
d3 = temp%10
temp = temp//10
sum = d1+d2+d3+temp
print("The sum of digits is ", sum)