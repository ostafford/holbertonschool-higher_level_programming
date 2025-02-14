#!/usr/bin/python3
'''Write a class Student
that defines a student by:
(based on 9-student.py)'''


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of Student instance."""
        return self.__dict__
