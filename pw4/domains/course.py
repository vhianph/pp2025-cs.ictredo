class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id;
        self.name = name;
        
    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}"

        