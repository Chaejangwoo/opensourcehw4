class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = self.english_score + self.c_score + self.python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average_score >= 90:
            return 'A'
        elif 80 <= self.average_score < 90:
            return 'B'
        elif 70 <= self.average_score < 80:
            return 'C'
        elif 60 <= self.average_score < 70:
            return 'D'
        else:
            return 'F'


class ScoreManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student with ID {student_id} has been removed.")
                return
        print("Student not found.")

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def calculate_rank(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)
        for i, student in enumerate(self.students):
            student.rank = i + 1

    def sort_students_by_total_score(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)

    def count_students_above_80(self):
        count = sum(1 for student in self.students if student.total_score >= 80)
        return count

    def display_students(self):
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}, "
                  f"Total Score: {student.total_score}, "
                  f"Average Score: {student.average_score}, "
                  f"Grade: {student.grade}, "
                  f"Rank: {student.rank}")


# 예시 사용
sms = ScoreManagementSystem()

for _ in range(5):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    english_score = int(input("Enter English score: "))
    c_score = int(input("Enter C score: "))
    python_score = int(input("Enter Python score: "))

    student = Student(student_id, name, english_score, c_score, python_score)
    sms.add_student(student)

sms.calculate_rank()
sms.display_students()

# 예시로 삭제 및 탐색 등 다른 함수들도 사용해보세요.
