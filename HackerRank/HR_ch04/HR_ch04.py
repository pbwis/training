year = 1990


def is_leap(year):
    leap = False
    no_leap = True
    y_leaps = [2000, 2400]
    y_no_leaps = [1800, 1900, 2100, 2200, 2300, 2500]

    for y_leap in y_leaps:
        if year == y_leap:
            return no_leap

    for y_no_Leap in y_no_leaps:
        if year == y_no_Leap:
            return leap

    if (year % 4) == 0:
        if (year % 100) != 0:
            if (year % 400) == 0:
                return leap
        return no_leap
    return leap


print(is_leap(year))
