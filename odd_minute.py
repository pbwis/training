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