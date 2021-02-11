jobs_list = list(map(int, input().split(', ')))
ind = int(input())
jobs = {}
for i in range(len(jobs_list)):
    jobs[i] = jobs_list[i]
jobs = sorted(jobs.items(), key=lambda x: (x[1], x[0]))
total = 0
for index, time in jobs:
    total += time
    if index == ind:
        break

print(total)
