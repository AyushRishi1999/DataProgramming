occur = [0] * 100
print("Enter integers between 1 and 100 (enter 0 to stop):")
while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    if 1 <= num <= 100:
        occur[num - 1] += 1
    else:
        print("Please enter an integer between 1 and 100.")
for n in range(len(occur)):
    count = occur[n]
    if count>0:
        plural = "times" if count > 1 else "time"
        print(f"{n + 1} occurs {count} {plural}")
