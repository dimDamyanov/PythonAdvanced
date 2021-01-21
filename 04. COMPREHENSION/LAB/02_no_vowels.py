string = input()
vowels = {'a', 'o', 'u', 'e', 'i'}
no_vowels = [ch for ch in string if ch.casefold() not in vowels]
print(''.join(no_vowels))
