class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject_taught):
        super().__init__(name, age)
        self.subject_taught = subject_taught

    def teach(self):
        print(f"{self.name} teaches {self.subject_taught}")


class Student(Person):
    def __init__(self, name, age, student_id, courses_enrolled):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses_enrolled = courses_enrolled

    def study(self):
        print(f"{self.name} studies the following courses: {', '.join(self.courses_enrolled)}")
class Subject:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)
