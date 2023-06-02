class Batsman:
    def __init__(self,*in1):
        if len(in1)==2:
            self.name="New Batsman"
            self.score=in1[0]
            self.balls=in1[1]
        elif len(in1)==3:
            self.name=in1[0]
            self.score=in1[1]
            self.balls=in1[2]
    def printCareerStatistics(self):
        print("Name: {}".format(self.name))
        print("Runs Scored: {}, Balls Faced: {}".format(self.score,self.balls))
    def setName(self,in2):
        self.name=in2
    def battingStrikeRate(self):
        print((self.score/self.balls)*100)



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
