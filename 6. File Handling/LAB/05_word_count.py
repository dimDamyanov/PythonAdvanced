import re

with open('../File Handling Resources/Words Count/words.txt') as file:
    words = ''.join(file.readlines()).split()

with open('../File Handling Resources/Words Count/text.txt') as file:
    text = ''.join(file.readlines())

occurrences = {word: len(list(re.findall(f'(^|(?<=\s))\W*{word}', text, re.IGNORECASE))) for word in words}
occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)
result = '\n'.join([f'{key} - {value}' for key, value in occurrences])
print(result)
with open('../File Handling Resources/Words Count/results.txt', 'w') as file:
    file.writelines(result)