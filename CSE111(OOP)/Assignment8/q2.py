# q2

class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def __str__(self):
        return '('+str(self.x)+' , '+str(self.y)+')'


class Vehicle2010(Vehicle):
    def moveUpperRight(self):
        Vehicle.moveUp(Vehicle)
        Vehicle.moveRight(Vehicle)

    def moveUpperLeft(self):
        Vehicle.moveUp(Vehicle)
        Vehicle.moveLeft(Vehicle)

    def moveLowerRight(self):
        Vehicle.moveDown(Vehicle)
        Vehicle.moveRight(Vehicle)

    def moveLowerLeft(self):
        Vehicle.moveDown(self)
        Vehicle.moveLeft(self)

    def equals(self, name):
        if self.__str__() == name.__str__():
            return True
        else:
            return False


print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))
print('------')
