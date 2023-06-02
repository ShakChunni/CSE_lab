# q5

class Animal:
    def __init__(self, sound):
        self.__sound = sound

    def makeSound(self):
        return self.__sound


class Printer(Animal):
    def __init__(self):
        pass

    def printSound(self, a):
        print(a.makeSound())


class Dog(Animal):
    pass


class Cat(Animal):
    pass


d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)
