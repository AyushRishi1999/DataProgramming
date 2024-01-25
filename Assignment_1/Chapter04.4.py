import random

x=random.randint(0,100)
y=random.randint(0,100)
print("Sum of",x,"+",y ,"is")
response = eval(input("Answer : "))
print(response == (x+y))