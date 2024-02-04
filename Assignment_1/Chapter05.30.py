def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def monthDays(year, firstDay):
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        daysInMonth[1] = 29
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for month in range(1, 13):
        print(f"{month}/1/{year} is {days_of_week[firstDay % 7]}")
        firstDay += daysInMonth[month - 1]

year = int(input("Enter the year: "))
firstDay = int(input("Enter the first day of the year (0 for Sunday, 1 for Monday, ..., 6 for Saturday): "))
monthDays(year, firstDay)
