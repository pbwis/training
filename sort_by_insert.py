# Sort array by insert function.

def sort_by_insert(unsorted):

    for number in range(1, len(unsorted)):
        value = unsorted[number]
        position = number

        while position > 0 and unsorted[position - 1] > value:
            unsorted[position] = unsorted[position -1]
            position = position - 1

        unsorted[position] = value


# Example of unsorted array
unsorted = [3, 8, 2, 9, 12, 45, 54, 77, 567, 333, 1, 18, 102]
print("Unsorted example: ", unsorted)
sort_by_insert(unsorted)
print("Sorted example: ", unsorted)