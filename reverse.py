# REVERSE
# Function takes string as an input
# and return that string in reverse

def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word


example = "Peter"
print(reverse(example))

# Output:
# reteP
