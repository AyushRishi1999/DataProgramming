
#Chinese Zodiac
#BMI
#Computing Tax
#First 15 prime numbers
#Turtle Mesh
'''
import time
MS = int(time.time() % 26)
randomUppercase = chr(ord('A')+MS)
print(randomUppercase)

import turtle
w,h =eval(input("Enter width and height  "))
turtle.penup()
turtle.goto(w/2,h/2)
turtle.pendown()
turtle.goto(w/2,h/2)
turtle.goto(w/2,-h/2)
turtle.goto(-w/2,-h/2)
turtle.goto(-w/2,h/2)
turtle.goto(w/2,h/2)
turtle.penup()
x,y=eval(input("enter coordinates  "))
d1 = ((w/2)**2+(h/2)**2)**0.5
d2 = (x**2+y**2)**0.5
if(x<(w/2) and x>(-w/2) and y<(h/2) and y>(-h/2)):
    print("the point is inside the rectangle")
else:
    print("the point is outside the rectangle")

turtle.done()
st=str(input("Enter lowercase letter"))
a=ord(st)-ord('a')+ord('A')
print(chr(a))

def gcd(num1,num2)

def isPrime(n)


def increment(num1, num2):
    return num1+1,num2+1
r1,r2=increment(10,20)
print(r1,r2)

def printMessage(st,num):
    for i in range(0,num):
        print(st)
printMessage(st='Message',num=5)

def sumOfTwoInt(num1,num2):
    sum = 0
    for i in range(num1, num2):
        sum += i
    return sum
def maxOfTwo(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

def maxOfThree(num1,num2,num3):
    return maxOfTwo(maxOfTwo(num1,num2),num3)

num1,num2 = eval(input("Enter Range : "))
print(maxOfThree(num1,num2))
print(maxOfTwo(num1,num2))
sum=sumOfTwoInt(num1,num2)
print(sum)

for i in range(1,10):
    for j in range(1,10):
        print(format(i*j, "<3d"), end='')
    print()

for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print()

isPrime = True 
num=eval(input("Enter a number : "))
for i in range(2,num//2):
    if num%i==0:
        isPrime=False
        break
print("Prime" if isPrime else "Not Prime")

num1=eval(input("Enter a number : "))
num2=eval(input("Enter a number : "))
gcd=1
for i in range(min(num1,num2),2,-1):
    if num1%i==0 and num2%i==0:
        gcd=i
        break
print(gcd)

num1=eval(input("Enter a number : "))
num2=eval(input("Enter a number : "))
gcd=1
for i in range(2,min(num1,num2)+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)

for i in range(10,0,-1):
    print(i)

num = eval(input("Enter a number : 0 is the end : "))
sum = 0

while num!=0:
    sum+=num
    num = eval(input("Enter a number : 0 is the end"))
print(sum)


import random
rand = random.randint(0, 100)
guess = eval(input("Enter a guess"))
while guess != rand:
    if guess<rand:
        print("Too low")
    else:
        print("Too High")
    guess = eval(input("Enter a guess"))
print("You got it right")

import random
count = 0
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
if num1 < num2:
    num1, num2 = num2, num1

if num1 > num2:
    response = eval(input("What is " + str(num1) + " - " + str(num2) + " ?"))
    while response != num1 - num2:
        print("Wrong!")
        response = eval(input("What is " + str(num1) + " - " + str(num2) + " ?"))
    print("Correct")

import random
count = 0
correct = 0
while count <= 5:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    if num1 < num2:
        num1, num2 = num2, num1

    if num1 > num2:
        response = eval(input("What is " + str(num1) + " - " + str(num2) + " ?"))
        if response == num1 - num2:
            print("Correct")
            correct+=1
        else:
            print("Incorrect")
    count += 1
print("Done")
print(100*correct/5)

count = 0
while count < 10:
    count += 2
    print(count)
print("Done")

import random
randNum = random.randint(10,99)
userNum = eval(input("Enter 2 digit Number"))

randNum1 = randNum%10
randNum2 = randNum//10
userNum1 = userNum%10
userNum2 = userNum//10

if randNum == userNum:
    print("You won $10,000")
elif randNum1 == userNum2 and randNum2 == userNum1:
    print("You won $3,000")
elif randNum1 == userNum2 or randNum2 == userNum1 or randNum1 == userNum1 and randNum2 == userNum2:
    print("You won $1,000")
else:
    print("You win Nothing")

year = eval(input("Enter number"))
if (year%4==0 or year%100!=0) or year%400==0:
    print("Leap Year")

num = eval(input("Enter number"))
if num%3==0 and num%2==0:
    print("Divisible by 2 and 3")
if num%3==0 or num%2==0:
    print("Divisible by 2 or 3")
if (num%3==0 or num%2==0) and not(num%3==0 and num%2==0) :
    print("Divisible by 2 or 3 but not both")

age = 24
print(not(age>10))

import random
num1 = random.randint(0,9)
num2 = random.randint(0,9)
if num1<num2:
    num1,num2=num2,num1

if num1>num2:
    response = eval(input("What is "+str(num1)+" - "+str(num2)+" ?"))
    if response==num1-num2:
        print("Correct")
    else:
        print("Incorrect")

import random
num1 = random.randint(0,9)
num2 = random.randint(0,9)
if num1>num2:
    response = eval(input("What is "+str(num1)+" - "+str(num2)+" ?"))
    print(response==(num1-num2))

num = eval(input("Enter a number"))
if num%5==0:
    print("HiFive")
if num%2==0:
    print("HiEven")

isSunny = True
if isSunny:
    pass

isSunny = True
if isSunny:
    print("I go shopping")
    print("I am happy")
    if 7<3:
        print("Hello")
        print("Python")

if 7>3:
    print("Bye")
    print("Java")
else:
    print("I stay home and study")
    
print("Done")

import random
num1 = random.randint(0,9)
num2 = random.randint(0,9)
response = eval(input("What is "+str(num1)+" + "+str(num2)+" ?"))
print(response == (num1+num2))

num1 = random.randint(0,9)
num2 = random.randrange(0,10)
num3 = random.random()
num4 = int(random.random() * 10)

b=False
#print(type(b))

#num=int(b)
#a=100
#b=bool(a)
#print(b)'''