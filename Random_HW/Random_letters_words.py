import random

text = input("Write your text:").split()
new_text = []
for word in text:
    if len(word) == 1:
        new_text.append(word)
        continue
    else:
        letter_list = list(word)
        # Shuffle all letters except of the first and the last
        new_word = random.sample(letter_list[1:-1], len(letter_list[1:-1]))
        new_text.append(letter_list[0] + ''.join(new_word) + letter_list[-1])
print(' '.join(new_text))
