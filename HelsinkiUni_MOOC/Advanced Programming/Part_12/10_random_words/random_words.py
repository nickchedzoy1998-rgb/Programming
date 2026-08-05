# Write your solution here:
def word_generator(characters: str, length: int, amount: int):
    import random

    words_generated = []

    no_selections = len(characters) - 1

    while len(words_generated) < amount:
        chars = ''

        while len(chars) < length:
            chars += characters[random.randint(0, no_selections)]

        words_generated.append(chars)

    return words_generated




if __name__ == '__main__':
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)

