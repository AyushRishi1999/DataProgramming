students = eval(input("enter the number of students : "))
highest=0
secondHighest=0
for i in range(0, students):
    score = eval(input("Enter Score : "))
    if highest<score:
        secondHighest = highest
        highest=score

    elif secondHighest<score and secondHighest!=highest:
        secondHighest=score
print("Highest Score : ", highest)
print("Second Highest : ", secondHighest)