# return random numbers between range of numbers
import random

print('[1, 100]:', end=' ')

for i in range(3):
    print(random.randint(1, 100), end=' ')  # randint(start, stop)

print('\n[-5, 5]:', end=' ')

for i in range(3):
    print(random.randint(-5, 5), end=' ')
print()

for i in range(3):
    print(random.randrange(0, 101, 5), end=' ')  # randrange(start, stop, step)
print()