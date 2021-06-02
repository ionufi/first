from repository import StudentRepository


class StudentController(object):
    def __init__(self):
        self._student_controller = StudentRepository()

    def add_student(self, student):
        return self._student_controller.add_student(student)

    def remove_student(self, sid):
        return self._student_controller.remove_student(sid)

    def update_student(self, sid, name, surname, grade):
        return self._student_controller.update_student(sid, name, surname, grade)

    def get_student(self, sid):
        return self._student_controller.get_student(sid)

    def get_all_students(self):
        return self._student_controller.get_all_students()

