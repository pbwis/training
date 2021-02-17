import collections

z = [1,2,3,2,1,5,6,5,5,5]
print(z)
print([item for item, count in collections.Counter(z).items() if count > 1])