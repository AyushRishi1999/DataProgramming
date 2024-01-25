amt = eval(input("Enter the monthly saving amount : "))
interest = 1+(0.05/12)
month1 = amt*interest
month2 = (month1+amt)*interest
month3 = (month2+amt)*interest
month4 = (month3+amt)*interest
month5 = (month4+amt)*interest
month6 = (month5+amt)*interest
print("After the sixth month, the account value is",round(month6,2))