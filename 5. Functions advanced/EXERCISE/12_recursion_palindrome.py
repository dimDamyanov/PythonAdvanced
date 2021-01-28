def palindrome(word, ind):
    chs = word[ind]
    che = word[-(ind + 1)]
    if len(word) - 1 == ind:
        return f'{word} is a palindrome'
    elif chs != che:
        return f'{word} is not a palindrome'
    else:
        return palindrome(word, ind + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
