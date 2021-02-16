from collections import deque

males = list(map(int, input().split()))
females_list = list(map(int, input().split()))
females = deque(females_list)
matches = 0
males = [e for e in males if e > 0]
females = deque([e for e in females if e > 0])
while females and males:
    current_female = females.popleft()
    current_male = males.pop()
    if current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue
    elif current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue
    if current_female == current_male:
        matches += 1
    else:
        if current_male - 2 > 0:
            males.append(current_male - 2)
        continue

print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join([str(e) for e in reversed(males)])}')
else:
    print(f'Males left: none')
if females:
    print(f'Females left: {", ".join([str(e) for e in females])}')
else:
    print(f'Females left: none')
