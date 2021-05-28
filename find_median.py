# FIND THE MEDIAN
# Median is the middle number
# in a sorted sequence of numbers.

def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        # odd numbers of elements
        index = len(sorted_list) // 2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        # even numbers of elements
        index_1 = len(sorted_list) / 2 - 1
        index_2 = len(sorted_list) / 2
        mean = (sorted_list[int(index_1)] + sorted_list[int(index_2)]) / 2
        return mean


example1 = [2, 4, 5, 9, 11]
example2 = [8, 14, 6, 5, 10, 11, 1, 44, 2]

print(median(example1))
print(median(example2))

# Output:
# 5
# 8
