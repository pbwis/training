# Merge the Tools!
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = ""
        for j in string[i: i + k]:
            if j in s:
                continue
            else:
                s += j
        print(s)


example = merge_the_tools("AABCAAADA", 3)
print(example)

# OUTPUT:
# AB
# CA
# AD
