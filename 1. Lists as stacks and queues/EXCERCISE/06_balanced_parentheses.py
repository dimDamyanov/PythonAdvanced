expression = input()
s = []
flag = False

for i in range(len(expression)):
    ch = expression[i]
    if ch in '({[':
        s.append(ch)
    elif ch in ')}]':
        if s:
            last = s.pop()
            if (ch == ')' and last != '(') or (ch == '}' and last != '{') or (ch == ']' and last != '['):
                flag = True
                break
        else:
            flag = True
            break
if flag:
    print('NO')
else:
    print('YES')