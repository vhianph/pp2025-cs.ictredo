from domains.management import StudentManagement
from input import input_student, input_course, input_mark
from output import print_students, print_courses, print_marks, print_gpa

def main():
    management = StudentManagement()
    
    # Input students
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id, name, dob = input_student()
        management.add_student(student_id, name, dob)
    
    # Input courses
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id, name = input_course()
        management.add_course(course_id, name)
    
    # Input marks
    for course in management.list_course():
        print(f"Entering marks for course {course.name} (ID: {course.course_id})")
        for student in management.list_students():
            print(f"Student: {student.name} (ID: {student.student_id})")
            mark = float(input("Enter mark: "))
            management.add_mark(course.course_id, student.student_id, mark)
    
    # Output data
    print_students(management.list_students())
    print_courses(management.list_course())
    
    # View marks for a course
    course_id = input("\nEnter course ID to view marks: ")
    marks = management.get_marks(course_id)
    print_marks(marks, course_id)
    
    # Calculate GPA
    gpas = management.calculate_gpa()
    print_gpa(gpas)

if __name__ == "__main__":
    main()