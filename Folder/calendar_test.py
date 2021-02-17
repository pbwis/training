# Calendar - part of the project / number of leap years

import calendar

sep = calendar.TextCalendar(calendar.SUNDAY)
sep.prmonth(2017, 9)
leaps = calendar.leapdays(1900, 2018)
print(leaps)

print(">>> Leap Year Calculator <<<\n")
y1 = int(input("Enter the first year: "))
y2 = int(input("Enter the second year: "))

leaps = calendar.leapdays(y1, y2)
print("Number of leap years between", y1, "and", y2, "is:", leaps)