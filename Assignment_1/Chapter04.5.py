today = eval(input("Enter today's day : "))
future = eval(input("Enter the number of days elapsed since today : "))
total = (today+future)%7
tDay=""
str=""
if today == 0:
    tDay="Sunday"
elif today == 1:
    tDay="Monday"
elif today == 2:
    tDay="Tuesday"
elif today == 3:
    tDay="Wednesday"
elif today == 4:
    tDay="Thrusday"
elif today == 5:
    tDay="Friday"
elif today == 6:
    tDay="Saturday"

if total == 0:
    str="Sunday"
elif total == 1:
    str="Monday"
elif total == 2:
    str="Tuesday"
elif total == 3:
    str="Wednesday"
elif total == 4:
    str="Thrusday"
elif total == 5:
    str="Friday"
elif total == 6:
    str="Saturday"



print("Today is",tDay,"and the future day is",str)