class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class StudentIterator:
    def __init__(self, students):
        self.students = students
        self.position = 0

    def has_next(self):
        return self.position < len(self.students)

    def next(self):
        student = self.students[self.position]
        self.position += 1
        return student


class StudentCollection:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def create_iterator(self):
        return StudentIterator(self.students)


students = StudentCollection()
students.add_student(Student("Ahsin"))
students.add_student(Student("Naufal"))
students.add_student(Student("Aziz"))

iterator = students.create_iterator()

while iterator.has_next():
    student = iterator.next()
    print(student.get_name())