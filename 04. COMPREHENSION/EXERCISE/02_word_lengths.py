text = input()
word_lengths = [f'{word} -> {len(word)}' for word in text.split(', ')]
print(', '.join(word_lengths))
