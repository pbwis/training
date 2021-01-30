import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    result = ''
    if (n % 2) != 0 or ((n % 2) == 0) and (6 <= n <= 20):
        result = 'Weird'
    elif (((n % 2) == 0) and (n >= 20)) or (((n % 2) != 0) or (2 <= n <= 5)):
        result = 'Not Weird'


print(result)
