from model import Student
from controller import StudentController

class StudentView(object):
    def __init__(self):
        self._student_view = StudentController()

    def add_student(self, student):
        self._student_view.add_student(student)

    def remove_student(self, sid):
        self._student_view.remove_student(sid)

    def update_student(self, sid):
        self._student_view.update_student(sid)

    def get_student(self, sid):
        self._student_view.get_student(sid)

    def get_all_students(self):
        return self._student_view.get_all_students()

    def print_menu(self):
        menu = ""
        menu += "1: Add students\n"
        menu += "2: Remove students\n"
        menu += "3: Update student\n"
        menu += "4: Get student\n"
        menu += "5: Get all students\n"
        menu += "0: Exit aplication\n"
        return menu

    def run_application(self):
        print(self.print_menu())
        while (True):
            option = int(input("Give option:"))

            if option == 1:
                sid = int(input("Give an id: "))
                name = input("Type the name:")
                surname = input("Type the surname:")
                grade = int(input("Type the grade:"))
                student = Student(sid=sid, name=name, surname=surname, grade=grade)
                self.add_student(student)

            if option == 2:
                delete_id = input("Type the ID student you want to delete: ")
                id_cont = Student([int(delete_id)], [], [], [])
#                index = self.get_all_students().index('2')

                if int(delete_id) == id_cont:
                    self.remove_student(Student([int(delete_id)], [], [], []))
                else:
                    print("This ID do not exist!")
#                    print(id_cont)
#                    print(index)

            if option == 5:
                print(self.get_all_students())

            if option == 0:
                break
            print(self.print_menu())


