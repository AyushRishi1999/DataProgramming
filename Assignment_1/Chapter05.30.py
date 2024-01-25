import calendar
year = int(input("Enter the year: "))
first_day = int(input("Enter the first day of the year (1 for Monday, 2 for Tuesday, ..., 7 for Sunday): "))

if first_day < 1 or first_day > 7:
    print("Invalid input for the first day. Please enter a number between 1 and 7.")
else:
    for month in range(1, 13):
        day_name = calendar.day_name[first_day - 1]
        print(f"{calendar.month_name[month]} 1, {year} is {day_name}")
        _, last_day = calendar.monthrange(year, month)
        first_day = (first_day + last_day) % 7 + 1

nahi hua bhai