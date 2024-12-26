def print_students(students):
    print("\nList of students:")
    for student in students:
        print(student)

def print_courses(courses):
    print("\nList of courses:")
    for course in courses:
        print(course)

def print_marks(marks, course_id):
    print(f"\nMarks for course ID {course_id}:")
    for student_id, mark in marks.items():
        print(f"Student ID {student_id}: {mark}")

def print_gpa(gpas):
    print("\nGPA for students:")
    for student_id, gpa in gpas.items():
        print(f"Student ID {student_id}: GPA {gpa}")