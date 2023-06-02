# question5

class Dolls:
    def __init__(self, n1, n2, n3=None):
        self.name = n1
        self.price = n2
        self.dolls = n3

    def detail(self):
        if self.dolls == 'multipledolls':
            return f'Dolls: {self.name}' f'\nTotal Price: {self.price} taka'
        else:
            return f'Doll: {self.name}' f'\nTotal Price: {self.price} taka'

    def __add__(self, n4):
        new_name = self.name + ' ' + n4.name
        new_price = self.price + n4.price
        object = Dolls(new_name, new_price, 'multipledolls')
        return object

    def __gt__(self, n5):
        if self.price > n5.price:
            return True
        else:
            return False


obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
