# q3

class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r

    def getRealValue(self):
        return self.__realValue

    def setRealValue(self, r):
        self.__realValue = r

    def ping(self):
        print('I am in RealNumber class')

    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())


class ComplexNumber(RealNumber):
    def __init__(self, n1=None, n2=None):
        if n2 == None:
            self.n2 = 1.0
        else:
            self.n2 = float(n2)
        if n1 == None:
            self.n1 = 1.0
        else:
            self.n1 = float(n1)

    def __str__(self):
        return 'RealPart: ' + str(self.n1) + '\nImaginarypart: ' + str(self.n2)


cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5, 7)
print(cn2)
print('---------')
