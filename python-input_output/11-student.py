#!/usr/bin/python3
'''Write a class Student that
defines a student by: (based on 10-student.py)'''


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of Student instance."""
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
