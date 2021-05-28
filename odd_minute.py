# different solution for odd minute in current hour
from datetime import datetime

current_minute = datetime.today().minute
print("Today is: ", datetime.today())
print("Current minute is : ", current_minute)

minutes = range(1, 61)
odds = []
for minute in minutes:
    if minute % 2 != 0:
        odds.append(minute)
    else:
        False

print("All odds minutes in 1 hour: \n", odds)

if current_minute in odds:
    print("This minute is odd")
else:
    print("This minute is even")

# OUTPUT:
# Today is:  2021-05-04 19:38:10.890664
# Current minute is :  38
# All odds minutes in 1 hour:
#  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# This minute is even