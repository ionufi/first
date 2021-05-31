from model import Student

#this class stores every student in a list
class StudentRepository(object):

    def __init__(self):
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def remove_student(self, student):
        self._students.pop(student)

    def update_student(self, sid):
        self._students.remove(sid)
        self._students.insert(0, sid)

    def get_student(self, sid):
        pass

    def get_all_students(self):
        return self._students

