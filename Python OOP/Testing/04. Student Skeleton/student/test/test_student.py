from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student('John', {"Course 1": ["Note about course 1", "second note"], "Course 2": ["my note"]})

    def test_init_with_name(self):
        name = "John"
        student = Student(name)
        self.assertEqual(name, student.name)

    def test_init_with_name_and_course(self):
        name = "John"
        courses = {"Course 1": ["Note about course 1", "second note"]}
        student = Student(name, courses)
        self.assertEqual(name, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_with_already_added_course_and_add_notes(self):
        result = self.student.enroll("Course 2", ["comment"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['my note', 'comment'], self.student.courses["Course 2"])

    def test_enroll_new_course_with_notes_Y(self):
        course = "Course 3"
        notes = ['Fe1', 'Fe2']
        result = self.student.enroll(course, notes, 'Y')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_new_course_with_notes_empty_str_arg(self):
        course = "Course 3"
        notes = ['Fe1', 'Fe2']
        result = self.student.enroll(course, notes, '')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_new_course_with_notes_adds_the_course_without_notes(self):
        course = "Course 3"
        notes = ['Fe1', 'Fe2']
        result = self.student.enroll(course, notes, 'N')
        self.assertEqual('Course has been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_to_existing_course(self):
        result = self.student.add_notes("Course 2", 'new note 4')
        self.assertEqual('Notes have been updated', result)
        self.assertEqual(['my note', 'new note 4'], self.student.courses["Course 2"])

    def test_add_notes_raises_when_course_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Invalid course", 'random note')
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_leave_course_remove_course_from_student(self):
        result = self.student.leave_course("Course 1")
        self.assertEqual("Course has been removed", result)
        self.assertTrue("Course 1" not in self.student.courses)
        self.assertTrue(len(self.student.courses))

    def test_leave_course_if_course_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Course 41241")
            self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
if __name__ == '__main__':
    main()
