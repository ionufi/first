from model import Student

#this class stores every student in a list
class StudentRepository(object):

    def __init__(self):
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def remove_student(self, sid):
        self._students.pop(sid)
        for i in range(sid, len(self._students)):
            self._students[i].set_id(i - 1)

    def update_student(self, sid, name, surname, grade):
        self._students[sid].set_name(name)
        self._students[sid].set_surname(surname)
        self._students[sid].set_grade(grade)

    def get_student(self, sid):
        return self._students[sid]

    def get_all_students(self):
        return self._students

