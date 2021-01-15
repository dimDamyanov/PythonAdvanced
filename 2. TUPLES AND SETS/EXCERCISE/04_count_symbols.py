text = input()
chars = {}
for ch in text:
    if ch not in chars:
        chars[ch] = 0
    chars[ch] += 1
data = sorted(chars.items(), key=lambda x: x[0])
for ch, count in data:
    print(f'{ch}: {count} time/s')
