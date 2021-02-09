""""
Decimal
Octal
Hexadecimal (capitalized)
Binary
"""

dec = 17
n = 0
print("The decimal value of", dec, "is:")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
print(bin(dec), "in binary.")


while n <= dec - 1:
    n += 1
    print(n, oct(n)[2:], f'{n:X}', bin(n)[2:])