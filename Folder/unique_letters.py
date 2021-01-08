alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def unique_letters_counter(word):
    uniques = 0
    for letter in alphabet:
        if letter in word:
            uniques += 1
    return uniques


print(unique_letters_counter("Mississipi"))
print(unique_letters_counter("Apple"))