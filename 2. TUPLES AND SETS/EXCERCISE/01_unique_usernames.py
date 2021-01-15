n = int(input())
usernames = set()
for _ in range(n):
    username = input()
    usernames.add(username)
for username in usernames:
    print(username)