from repository import StudentRepository


class StudentController(object):
    def __init__(self):
        self._student_controller = StudentRepository()

    def add_student(self, student):
        self._student_controller.add_student(student)

    def remove_student(self, student):
        # de facut update sa fie ca in repo
        self._student_controller.remove_student(student)

    def update_student(self, sid):
        self._student_controller.update_student(sid)

    def get_student(self, sid):
        self._student_controller.get_student(sid)

    def get_all_students(self):
        return self._student_controller.get_all_students()

