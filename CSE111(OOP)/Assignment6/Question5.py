#question5

class Vehicle:
    def __init__(self):
        self.position=[0,0]
    def moveUp(self):
        self.position[1]+=1
    def moveDown(self):
        self.position[1]-=1
    def moveLeft(self):
        self.position[0]-=1
    def moveRight(self):
        self.position[0]+=1
    def print_position(self):
        print(tuple(self.position))


car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()