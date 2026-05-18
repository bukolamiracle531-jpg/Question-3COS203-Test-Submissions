import os
from student_module import Student

FILE_NAME = "submissions.txt"

def save_record(student_obj):
    """Appends a student record to the submissions file."""
    with open(FILE_NAME, "a") as file:
        file.write(student_obj.to_string() + "\n")

def get_all_records():
    """Retrieves and reads all submission records from the text file."""
    if not os.path.exists(FILE_NAME):
        return []
    
    records = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 3:
                records.append(Student(parts[0], parts[1], parts[2]))
    return records

def search_by_matric(matric_number):
    """Searches through the records file to locate a student matching the target matric number."""
    records = get_all_records()
    for student in records:
        if student.matric_number.lower() == matric_number.lower().strip():
            return student
    return None
