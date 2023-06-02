# q2
class Account:
    count = 0
    balance: 0

    def __init__(self, n1, n2, n3, n4):
        self.name = n1
        self.age = n2
        self.occupation = n3
        self.ammount = n4
        Account.count += 1

    def addMoney(self, n5):
        self.ammount += n5
        print("Add Money successfully !!")

    def withdrawMoney(self, n6):
        if n6 > self.ammount:
            print("Not sufficient balance.")
        else:
            self.ammount -= n6
            print("Withdraw Successful !!")

    def printDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Occupation:", self.occupation)
        print("Total Amount:", self.ammount)


print('No of account holders:', Account.count)
print("=========================")
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.addMoney(300000)
p1.printDetails()
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
p2.withdrawMoney(700000)
p2.printDetails()
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
p3.withdrawMoney(250000)
p3.printDetails()
print("=========================")
print('No of account holders:', Account.count)
