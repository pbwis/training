# COUNTER LIST ITEM
# Define a function which can count amount
# of items inside list

def count(sequence, item):
    amount = 0
    for i in sequence:
        if i == item:
            amount += 1
    return amount


names = ['John', 'Peter', 'Adam', 'John', 'Adam', 'Adam', 'Meg']

example = count(names, 'John')
print(example)

# OUTPUT:
# 2
