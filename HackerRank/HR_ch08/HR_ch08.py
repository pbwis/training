s = "aabbbccde"


my_dict = {i: s.count(i) for i in s}

print(my_dict)

sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: (item[1], item[1]), reverse=True)[:3]}

print(sorted_dict)

for item in sorted_dict:
    print(item, sorted_dict[item])