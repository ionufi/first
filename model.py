class Student(object):
    def __init__(self, sid, name, surname, grade):
        self._id = sid
        self._name = name
        self._surname = surname
        self._grade = grade

    def get_id(self):
        return self._id

    def set_id(self, sid):
        self._id = sid

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_surname(self):
        return self._surname

    def set_surname(self, surname):
        self._surname = surname

    def get_grade(self):
        return self._grade

    def set_grad(self, grade):
        self._grade = grade

    def __repr__(self):
        return f"Student({self.get_id()}, {self.get_name()}, {self.get_surname()}, {self.get_grade()})"

    def __str__(self):
        return f"Student({self.get_id()}, {self.get_name()}, {self.get_surname()}, {self.get_grade()})"

