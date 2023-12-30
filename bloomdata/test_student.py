'''
This Test file is for functions in the student.py file made from a previous
assignment to see if each function can work properly.
'''
from bloomdata.student import Student, BloomTechStudent, student_generator
import pytest


def test_student_instance():
    """This is s test for the instantiation of a Student object"""
    student = Student('John', 22)
    assert isinstance(student, Student)
    assert student.name == 'John'
    assert student.age == 22


def test_bloomtechstudent_instance():
    """Testing the Instantion of a BloomTechStudent object"""
    bloomtech_student = BloomTechStudent('Alice', 20, 'Computer Science')
    assert isinstance(bloomtech_student, BloomTechStudent)
    assert bloomtech_student.name == 'Alice'
    assert bloomtech_student.age == 20
    assert bloomtech_student.major == 'Computer Science'


def test_student_generator():
    """Testing the functionality of the student_generator Function"""
    students = student_generator()
    assert len(students) == 5

    for student in students:
        assert isinstance(student, BloomTechStudent)
        assert student.name in ['Alex', 'Frank', 'Jenny', 'Chris', 'Adam']
        assert student.age in [18, 19, 20, 21, 28]
        assert student.major in ['Data Science', 'Cooking', 'Math',
                                 'Business', 'Law']
