from enum import Enum


class Student:
    def __init__(self, id, name, email, group, status):
        self.id = id
        self.name = name
        self.email = email
        self.group = group
        self.status = status


class StudentType(Enum):
    ABITUR = 1
    STUDY = 2
    KICKED = 3


class Group:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class StudentRepository:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def get(self, id):
        for student in self.students:
            if student.id == id:
                return student

    def get_all(self):
        return self.students


class StudentService:
    def __init__(self, repository):
        self.repository = repository

    def add_student(self, id, name, email, group):
        student = Student(id, name, email, group)
        self.repository.add(student)

    def get_student(self, id):
        return self.repository.get(id)

    def get_all_students(self):
        return self.repository.get_all()

    def enroll_student(self, student, group):
        if student.status == StudentType.STUDY:
            return student
        student.status = StudentType.STUDY
        student.group = group

        return student

    def expel_student(self, student):
        if student.status == StudentType.KICKED or student.status == StudentType.ABITUR:
            return student
        student.status = StudentType.KICKED
        student.group = None

        return student


# Внешний слой
class StudentAPI:
    def __init__(self, student_service):
        self.student_service = student_service

    def add_student(self, id, name, email, group):
        self.student_service.add_student(id, name, email, group)

    def get_student(self, id):
        student = self.student_service.get_student(id)

        if not student:
            return f"Student with id {id} does not exist."

        return {"id": student.id, "name": student.name, "email": student.email}

    def get_all_students(self):
        students = self.student_service.get_all_students()
        return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
