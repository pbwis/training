n = 3
number_oryg = n
split_number = []

while n > 1:
    n = n - 1
    split_number.append(n)


split_number.sort(reverse=False)
split_number.append(number_oryg)

for n in split_number:
    print(n, end="")
