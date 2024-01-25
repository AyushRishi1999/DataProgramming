import random
randNum = random.randint(100,999)
userNum = eval(input("Enter 3 digit Number : "))

randNum1 = randNum%10
remRandNum = randNum//10
randNum2 = remRandNum//10
randNum3 = remRandNum//10

userNum1 = userNum%10
remUserNum = userNum//10
userNum2 = remUserNum//10
userNum3 = remUserNum//10

if randNum == userNum:
    print("You won $10,000")
elif ((randNum1 == userNum2 and
      randNum2 == userNum1 and
      randNum3 == userNum3) or
      (randNum1 == userNum3 and
      randNum3 == userNum1 and
       randNum2 == userNum2) or
      (randNum1 == userNum1 and
      randNum2 == userNum3 and
       randNum3 == userNum2)):
    print("You won $3,000")
elif ((randNum1 == userNum2 or
      randNum2 == userNum1 or
      randNum3 == userNum3) or
      (randNum1 == userNum3 or
      randNum3 == userNum1 or
       randNum2 == userNum2) or
      (randNum1 == userNum1 or
      randNum2 == userNum3 or
       randNum3 == userNum2)):
    print("You won $1,000")
else:
    print("You win Nothing")