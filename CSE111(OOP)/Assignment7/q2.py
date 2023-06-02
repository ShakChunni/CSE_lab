# question2

class Teacher:
    def __init__(self, n1, n2):
        self.__name = n1
        self.__department = n2
        self.__course = []

    def addCourse(self, n3):
        self.__course.append(n3)

    def printDetail(self):
        print('=====================================')
        print('Name:', self.__name)
        print('Department:', self.__department)
        print('List of courses')
        print('=====================================')
        for i in self.__course:
            print(i.title)
        print('=====================================')


class Course:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")
c1 = Course("CSE 110 Programming Language I")
c2 = Course("CSE 111 Programming Language-II")
c3 = Course("CSE 220 Data Structures")
c4 = Course("CSE 221 Algorithms")
c5 = Course("CCSE 230 Discrete Mathematics")
c6 = Course("CSE 310 Object Oriented Programming")
c7 = Course("CSE 320 Data Communications")
c8 = Course("CSE 340 Computer Architecture")
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()
