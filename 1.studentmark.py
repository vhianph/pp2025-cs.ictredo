def input_function():
    students_lst = []
    # Input number of students in a class
    num_student = int(input("Enter the number of students: "))
    # Input student information: id, name, DoB
    for i in range(num_student):
        print("Student %d information:" % (i + 1))
        student_id = input("Enter the student ID: ")
        student_name = input("Enter full name of the student: ")
        student_dob = input("Enter date of birth of the student (dd/mm/yyyy): ")
        students_lst.append({"ID": student_id, "Full_name": student_name, "DoB": student_dob})

    course_lst = []
    # Input number of courses
    num_course = int(input("Enter the number of courses: "))
    # Input course information: id, name
    for i in range(num_course):
        print("Course %d information:" % (i + 1))
        course_id = input("Enter the course ID: ")
        course_name = input("Enter name of the course: ")
        course_lst.append({"ID": course_id, "Name": course_name})

    # Select a course and input marks for students in this course
    marks = {}
    for course in course_lst:
        course_id = course["ID"]
        course_mark = {}
        print(f"Enter the marks for {course['Name']} (ID: {course_id}):")

        for student in students_lst:
            mark = float(input(f"Enter the mark for student {student['Full_name']} ({student['ID']}): "))
            course_mark[student["ID"]] = mark
        marks[course_id] = course_mark

    return students_lst, course_lst, marks

def main():
    students_lst, course_lst, marks = input_function()

    # List courses
    print("\nList of courses:")
    for course in course_lst:
        print(f"ID: {course['ID']}, Name: {course['Name']}")

    # List students
    print("\nList of students:")
    for student in students_lst:
        print(f"ID: {student['ID']}, Name: {student['Full_name']}, Date of birth: {student['DoB']}")

    # View marks for a specific course
    course_id = input("\nEnter the course ID to view marks: ")
    if course_id in marks:
        print(f"\nMarks for course ID {course_id}:")
        for student_id, mark in marks[course_id].items():
            # Find the student name based on the student ID
            student_name = None
            for student in students_lst:
                if student["ID"] == student_id:
                    student_name = student["Full_name"]
                    break  

            if student_name is not None:
                print(f"{student_name}: {mark}")
            else:
                print(f"Student with ID {student_id} not found.")
    else:
        print("Unknown course")

if __name__ == "__main__":
    main()