"""
IS PRIME:
The prime number is positive integer greater than 1
that has no positive divisors othe than 1 and itself.
"""


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                return False
        return True


print(is_prime(13))
print(is_prime(10))

# OUTPUT:
# True
# False
