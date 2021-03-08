# REMOVE DUPLICATES FROM LIST

def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    inputlist = sorted(inputlist)
    outputlist = [inputlist[0]]
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
    return outputlist


unsorted_list = [1, 2, 2, 2, 3, 5, 9, 3, 67, 33, 3, 0, 334, 1, 9]
example = remove_duplicates(unsorted_list)
print(unsorted_list)
print(example)
