# question1

class Student:
    ID = 0

    def __init__(self, n1, n2, n3, n4):
        self.name = n1
        self.department = n2
        self.age = n3
        self.cgpa = n4

    def get_details(self):
        Student.ID += 1
        print("ID:", Student.ID)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Age:", self.age)
        print("CGPA:", self.cgpa)

    @classmethod
    def from_String(cls, n5):
        name, department, age, cgpa = n5.split("-")
        object = cls(name, department, age, cgpa)
        return object


s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()

print("5. The difference between class and instance variable is, class variable is belongs to only one specific class while instace variable is shared between a class and subclass.")
print("6. The difference between class and instace method is, class method operates on class as a whole and it has no acess to any instance variable unless we pass the instace varaible in as a parameter. Where as, the instace method can operate on objects and has acees to instance variables.")
