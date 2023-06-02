# 1

class Student:
    def __init__(self, name="Just a student", dept="nothing"):
        self.__name = name
        self.__department = dept

    def set_department(self, dept):
        self.__department = dept

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return 'Name: '+self.__name+' Department: '+self.__department


class BBA_Student(Student):
    Student.set_department(Student, "BBA")

    def __init__(self, name=None):
        if name == None:
            Student.set_name(Student, "dafault")
        else:
            Student.set_name(Student, name)
        Student.__str__(Student)


print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))
