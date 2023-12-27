class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class BloomTechStudent(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major


def student_generator():
    names = ['Alex', 'Frank', 'Jenny', 'Chris', 'Adam']
    ages = [18, 19, 20, 21, 28]
    majors = ['Data Science', 'Cooking', 'Math', 'Business', 'Law']

    bloomtech_students = [
        BloomTechStudent(name, age, major)
        for name, age, major in zip(names, ages, majors)
    ]

    return bloomtech_students


bloomtech_students = student_generator()

for student in bloomtech_students:
    print(f"Name: {student.name}, Age: {student.age}, Major: {student.major}")
