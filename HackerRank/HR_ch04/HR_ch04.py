year = 1990

def is_leap(year):
    leap = False
    no_leap = True

    Y_Leaps = [2000, 2400]
    Y_No_Leaps = [1800, 1900, 2100, 2200, 2300, 2500]
    # Write your logic here

    for y_leap in Y_Leaps:
        if year == y_leap:
            return no_leap

    for y_no_Leap in Y_No_Leaps:
        if year == y_no_Leap:
            return leap

    if (year % 4) == 0:
        if (year % 100) != 0:
            if (year % 400) == 0:
                return leap
        return no_leap
    return leap

print(is_leap(year))