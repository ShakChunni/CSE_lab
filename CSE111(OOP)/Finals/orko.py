#q3
class Player:
     def init(self,name,goalsScored,tacklesWon):
         self.name = name
         self.goalsScored = goalsScored
         self.tacklesWon = tacklesWon
         self.point=0
     def calculatePoint(self):
          self.point+=(self.goalsScored*4)+(self.tacklesWon*3)
class Defender:
    def __init__(self,name,goalsScored,tacklesWon,rating):
        self.name=name
        self.goalsScored=goalsScored
        self.tacklesWon=tacklesWon
        self.rating=rating
        print("Name:",self.name,",","Rating:",self.rating)
    def calculatePoint(self):
        self.point=(self.goalsScored*4)+(self.tacklesWon*3)+(self.rating*2)
        print("Point of", self.name, ":", self.point)
class Attacker:
    def __init__(self,name,goalsScored,tacklesWon,rating):
        self.name=name
        self.goalsScored=goalsScored
        self.tacklesWon=tacklesWon
        self.rating=rating
        print("Name:", self.name,",","Rating:", self.rating)
    def calculatePoint(self):
        self.point = (self.goalsScored * 4) + (self.tacklesWon * 3) + (self.rating * 2)
        print("Point of", self.name, ":", self.point)
print('=========================')
p1 = Defender("Thiago Silva",5,12,8.5)
print('=========================')
p2 = Attacker("Cristiano Ronaldo",14,5,9.0)
print('=========================')
p3 = Attacker("Lionel Messi",12,9,9.5)
print('=========================')
p1.calculatePoint()
print('=========================')
p2.calculatePoint()
print('=========================')
p3.calculatePoint()



