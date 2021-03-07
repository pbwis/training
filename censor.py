# Function CENSOR
# Split sentence, pick one word and replace it


def censor(text, word):
    words = text.split()
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result = ' '.join(words)
    return result


sentence = 'My name is Peter and what is your name?'
word_censored = 'Peter'
example = censor(sentence, word_censored)

print(example)
