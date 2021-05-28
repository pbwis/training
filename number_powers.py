"""
Exponentiation
short function
"""


def exponentiation(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_item = base ** power
            new_list.append(new_item)
    return new_list


print(exponentiation([2, 3, 4, 43], [1, 2, 3]))


# OUTPUT:
# [2, 4, 8, 3, 9, 27, 4, 16, 64, 43, 1849, 79507]
