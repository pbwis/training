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
