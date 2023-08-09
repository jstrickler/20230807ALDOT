from itertools import groupby

with open("DATA/words.txt") as words_in:
    all_words = words_in.read().splitlines()

print(all_words[:25])

grouped_words = groupby(all_words, key=lambda w: w[0])
print(f"grouped_words: {grouped_words}\n")

for letter, group in grouped_words:
    print(letter, len(list(group)))
print()