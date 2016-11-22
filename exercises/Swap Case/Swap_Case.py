
word = input("Enter a word: ")


def swap(word):
    swap_word = []
    for ch in word:
        if ch == ch.lower():
            swap_word.append(ch.upper())
        else:
            ch == ch.upper()
            swap_word.append(ch.lower())
    return "".join(swap_word)

print (swap(word))
