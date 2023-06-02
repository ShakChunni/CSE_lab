#question4 

class Cat:
    def __init__(self,color="White",activity="sitting"):
        self.activity=activity
        self.color=color
    
    def changeColor(self,newcolor):
        self.color=newcolor
    def printCat(self):
        print("{} cat is {}".format(self.color,self.activity))


c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()