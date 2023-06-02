# q6

class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name

    def getName(self):
        return self.name

    def hasFormalin(self):
        return self.__formalin

    def __str__(self):
        return self.name


class Mango(Fruit):
    def __init__(self, formalin=True, name='Mango'):
        self.__formalin = formalin
        self.name = name

    def hasFormalin(self):
        return self.__formalin


class Jackfruit(Fruit):
    def __init__(self, formalin=False, name='Jackfruit'):
        self.__formalin = formalin
        self.name = name

    def hasFormalin(self):
        return self.__formalin


class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the ', f.getName(), '.')
            print(f, 's are bad for you', sep='')
        else:
            print('Eat the ', f.getName(), '.')
            print(f, 's are good for you', sep='')


m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)
