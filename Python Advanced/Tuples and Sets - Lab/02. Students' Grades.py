count = int(input())
grades = {}

for _ in range(count):
    name, grade_str = input().split()
    grade = float(grade_str)

    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for name, grades in grades.items():
    average_grade = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {average_grade:.2f})")