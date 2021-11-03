class Class:

    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []


    def add_student(self, student_name:str, student_grade:float):
        if Class.__students_count > 0:
            self.students.append(student_name)
            self.grades.append(student_grade)
            Class.__students_count -= 1

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        students_list = ", ".join(self.students)
        return f"The students in {self.name}: {students_list}. Average grade: {self.get_average_grade():.2f}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
