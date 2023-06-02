#Hamim

class Car:
    count=0
    def __init__(self,n1,n2):
        self.name=n1
        self.year=n2
        Car.count += 1
    def add_Services(self,n3,n4):
        self.service1=n3
        self.service2=n4
    def printCarDetail(self):
        print("Name:",self.name)
        print("Year of manufacture:",self.year)
        print("List of Services:",self.service1,",",self.service2)
print("No.of Car=", Car.count)
c1 = Car('Lamborghini', 2002)
c1.add_Services('Battery Replacement', 'A/C Recharge')
c2 = Car('Toyota Corolla', 2016)
c2.add_Services('Radiator Flush', 'Fill Service')
c3 = Car('Mitsubishi Pajero', 2018)
c3.add_Services('Filter change', 'Timing Belt Replacement')
print("=========================")
c1.printCarDetail()
print("=========================")
c2.printCarDetail()
print("=========================")
c3.printCarDetail()
print("=========================")
print("No.of Car =", Car.count)