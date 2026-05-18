class Student:
    def __init__(self, name, matric_number, course_code):
        """Initializes a Student entity with name, matric number, and course code."""
        self.name = name
        self.matric_number = matric_number
        self.course_code = course_code

    def to_string(self):
        """Formats the object properties into a single text line for file storage."""
        return f"{self.name}|{self.matric_number}|{self.course_code}"
