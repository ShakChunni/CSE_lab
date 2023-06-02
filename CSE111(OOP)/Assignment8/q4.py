# q4

class Account:
    def __init__(self, balance):
        self._balance = balance

    def getBalance(self):
        return self._balance


class CheckingAccount(Account):
    n = 0
    numberOfAccount = str(n)

    def __init__(self, amount=None):
        if amount == None:
            self._balance = 0.0
        else:
            self._balance = amount
        print("Account Balance:", end="")
        CheckingAccount.n += 1
        CheckingAccount.numberOfAccount = str(CheckingAccount.n)

    def __str__(self):
        return str(self.getBalance())


print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)
