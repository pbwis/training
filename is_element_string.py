# Is element string


def is_element_string(x):
    if isinstance(x, str):
        return True
    else:
        return False


ls = [1, 2, 3, '4', '5', 6, 7, '87', 10]
list(filter(is_element_string, ls))
r = filter(lambda x: isinstance(x, str), ls)

for i in r:
    print(i)

# Output:
# 4
# 5
# 87
