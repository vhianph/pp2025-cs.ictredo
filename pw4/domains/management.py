import math
from domains.student import Student
from domains.course import Course

class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    
    def add_student(self, student_id, name, dob):
        self.students.append(Student(student_id, name, dob))
    
    def add_course(self, course_id, name):
        self.courses.append(Course(course_id, name))
        
    def add_mark(self, course_id, student_id, mark):
        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.marks[course_id][student_id] = math.floor(mark*10)/10
        
    def list_students(self):
        return self.students
    
    def list_course(self):
        return self.courses
    
    def get_marks(self, course_id):
        return self.marks.get(course_id, {})
    
    def calculate_gpa(self):
        student_gpas = {}
        for student in self.students:
            total_credits = 0
            total_weighted_marks = 0
            for course_id, course_marks in self.marks.items():
                if student.student_id in course_marks:
                    mark = course_marks[student.student_id]
                    credit = 3  # Giả sử mỗi môn học có 3 tín chỉ
                    total_credits += credit
                    total_weighted_marks += mark * credit
            if total_credits > 0:
                gpa = total_weighted_marks / total_credits
                student_gpas[student.student_id] = round(gpa, 2)
            else:
                student_gpas[student.student_id] = 0.0
        return student_gpas
    