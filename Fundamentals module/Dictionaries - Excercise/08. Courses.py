data = input()

courses = {}

while not data == "end":
    course_name, student_name = data.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    data = input()

sorted_courses = sorted(courses.items(), key=lambda kvpt: len(kvpt[1]), reverse= True)

for course_name, student_name in sorted_courses:
    print(f"{course_name}: {len(student_name)}")
    for name in sorted(student_name):
        print(f"-- {name}")