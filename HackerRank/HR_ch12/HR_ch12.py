# Capitalize each word
name = "john Smith - doe"
print(name)

if not name:
    print("No data")


def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s


print(solve(name))
