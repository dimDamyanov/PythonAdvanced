text = input()
even_words = [word for word in text.split() if len(word) % 2 == 0]
for word in even_words:
    print(word)
