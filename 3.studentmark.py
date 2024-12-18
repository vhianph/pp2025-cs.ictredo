import math

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Date of birth: {self.dob}"
    
class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        
    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}"
    
class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}  
        
    def input_student(self):
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            print(f"Student {i+1} information:")
            student_id = input("Enter the student ID: ")
            student_name = input("Enter the student name: ")
            dob = input("Enter date of birth of the student (dd/mm/yyyy): ")
            student = Student(student_id, student_name, dob)
            self.students.append(student)
            
    def input_course(self):
        num_course = int(input("Enter the number of courses: "))
        for i in range(num_course):
            print(f"Course {i+1} information:")
            course_id = input("Enter the course ID: ")
            course_name = input("Enter the course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)
            
    def input_marks(self):
        for course in self.courses:
            course_id = course.course_id
            print(f"Enter the marks for {course.name} (ID: {course_id}):")
            course_marks = {}
            for student in self.students:
                mark = float(input(f"Enter the mark for student {student.name} ({student.student_id}): "))
                mark = math.floor(mark * 10) / 10  # Làm tròn xuống 1 chữ số thập phân 
                course_marks[student.student_id] = mark
            self.marks[course_id] = course_marks  
            
    def list_students(self):
        print("\nList of students:")
        for student in self.students:
            print(student)
    
    def list_courses(self):
        print("\nList of courses:")
        for course in self.courses:
            print(course)
            
    def view_mark(self):
        course_id = input("\nEnter the course ID to view marks: ")
        if course_id in self.marks:
            print(f"\nMarks for course ID {course_id}:")
            for student in self.students:
                mark = self.marks[course_id].get(student.student_id, "N/A")
                print(f"{student.name}: {mark}")
        else:
            print("Unknown course ID")
            
            
    def calculate_gpa(self):  
        student_gpas = {}
        for student in self.students:
            total_credits = 0
            total_weighted_marks = 0
            for course_id, course_marks in self.marks.items():
                if student.student_id in course_marks:
                    mark = course_marks[student.student_id]
                    credit = 3  # Giả sử mỗi môn học có 3 tín chỉ - Added
                    total_credits += credit
                    total_weighted_marks += mark * credit
            if total_credits > 0:
                gpa = total_weighted_marks / total_credits
                student_gpas[student.student_id] = round(gpa, 2)
            else:
                student_gpas[student.student_id] = 0.0
        return student_gpas
    
    def sort_students_by_gpa(self):  
        student_gpas = self.calculate_gpa()  
        sorted_students = sorted(self.students, key=lambda s: student_gpas[s.student_id], reverse=True)  
        print("\nStudents sorted by GPA (descending):")  
        for student in sorted_students:  
            print(f"{student.name} (ID: {student.student_id}) - GPA: {student_gpas[student.student_id]}")  
    
    def run(self):
        self.input_student()
        self.input_course()
        self.input_marks()
        self.list_courses()
        self.list_students()
        self.view_mark()
        self.sort_students_by_gpa()
def main():
    management = StudentManagement()
    management.run()


if __name__ == "__main__":
    main()