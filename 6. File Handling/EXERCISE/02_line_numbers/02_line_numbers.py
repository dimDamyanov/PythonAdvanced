import re

with open('text.txt', 'r') as file:
    lines = file.readlines()

result_lines = []
for ind, line in enumerate(lines):
    line = line.strip()
    letters_count = len(re.findall(r'\w', line))
    punctuation_count = len(re.findall('[!?"#$%&@`\'(){},.:;+_-]', line))
    res = f'Line {ind+1}: {line} ({letters_count})({punctuation_count})'
    result_lines.append(res)

with open('output.txt', 'w') as file:
    file.writelines('\n'.join(result_lines))
