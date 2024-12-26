def input_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (dd/mm/yyyy): ")
    return student_id, name, dob

def input_course():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return course_id, name

def input_mark():
    student_id = input("Enter student ID: ")
    mark = float(input("Enter mark: "))
    return student_id, mark