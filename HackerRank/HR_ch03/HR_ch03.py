if __name__ == '__main__':
    n = int(input())
    each_number = []

    while n > 0:
        n = n - 1
        each_number.append(n)

    each_number.sort(reverse=False)

    for num in each_number:
        print(num ** 2)