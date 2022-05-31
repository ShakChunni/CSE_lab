#fuad
class Batsman():
    def __init__(self,n1=0,n2=0,n3="New Batsman"):
        self.name=n3
        self.runs=n2
        self.balls=n1
    def printCareerStatistics(self):
        print("Name:", self.name)
        print("Runs Scored:",self.runs)
        print("Balls Faced:",self.balls)
    def setName(self,n4):
        self.name=n4
    def battingStrikeRate(self):


b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())