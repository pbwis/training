# Find hidden word in list of words
from collections import Counter


hidden_word = "mot"
a = 'remote'
b = 'moto'
c = 'abcde'
d = 'unmotivated'

all_words = [a, b, c, d]
print(all_words)

output = Counter(all_words)
print(output)


def find_word():
    for item in all_words:
        if item.__contains__(hidden_word):
            print(hidden_word, "-- Found in: -- ", item)
        else:
            print(hidden_word, "-- NOT found in: -- ", item)


find_word()

# OUTPUT:
# mot -- Found in: --  remote
# mot -- Found in: --  moto
# mot -- NOT found in: --  abcde
# mot -- Found in: --  unmotivated
