# Multiplication numbers on list


def multiplication(lst):
    total = 1
    for num in lst:
        total = total * num
    return total


example = [4, 5, 5]

print(multiplication(example))

# Output:
# 100 (4 * 5 * 5)


# FACTORIAL

def fact(x):
    total = 1
    while x > 0:
        total *= x
        x -= 1
    return total


example2 = fact(3)
print(example2)

# OUTPUT:
# 6
