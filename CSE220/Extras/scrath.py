import sys
sys.setrecursionlimit(250000)
class FinalQ:
    def print(self,array,idx):
        if(idx>len(array)):
            return
        if(idx<len(array)):
            profit = self.calcProfit(array[idx])
            print(idx+1,".","Investment :",array[idx],"; Profit :",profit)
        self.print(array,idx+1)


    def calcProfit(self,investment):

        if(investment>100000):
            return 8+self.calcProfit(investment-100)
        elif(investment>25000):
            return 4.5+self.calcProfit(investment-100)
        else:
            return 0.0
#Tester
array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)