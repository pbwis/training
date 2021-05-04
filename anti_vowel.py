# ANTI VOWEL
# Function takes one string and return
# string without vowels

def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
        if char not in vowels:
            result = result + char
    return result


example = "Hello book"
print(anti_vowel(example))

# OUTPUT:
# Hll bk