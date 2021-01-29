import re
with open('text.txt', 'r') as file:
    lines = file.readlines()

result = []
for ind, line in enumerate(lines):
    if ind % 2 == 0:
        res = re.sub(r'[,.!?-]', '@', line)
        result.append(' '.join(list(reversed(re.findall('@*[a-zA-Z\']+@*', res)))))

print(*result, sep='\n')
