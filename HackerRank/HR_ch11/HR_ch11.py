# helpful function for creating web addresses (long tails)

a = "this is some kind of string"


def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)


new_string = split_and_join(a)

print("https://www.page-example.com/" + new_string)

# OUTPUT:
# https://www.page-example.com/this-is-some-kind-of-string
