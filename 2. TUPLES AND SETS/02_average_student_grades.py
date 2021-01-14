def avg(values):
    return sum(values) / len(values)


n = int(input())

students_grades = {}
for i in range(n):
    line = input()
    student, grade = line.split()
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for student, grades in students_grades.items():
    print(f'{student} -> {" ".join(map(lambda x: f"{x:.2f}", grades))} (avg: {avg(grades):.2f})')