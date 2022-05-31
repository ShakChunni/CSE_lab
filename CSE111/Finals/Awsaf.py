#q2
class Pizza:
    pizza_count=0
    def __init__(self,n1):
        self.toppings=n1
        Pizza.pizza_count+=1
    def set_toppings_info(self,n2,n3,n4,n5):
        self.calorie=n2
        self.fat=n3
        self.protein=n4
        self.carbs=n5
    def display(self):
        print("Toppings:",self.toppings)
        print(self.calorie , "calories")
        print(self.fat , "g fat")
        print(self.protein , "g protein")
        print(self.carbs , "g carbs")
print("Pizza Count:", Pizza.pizza_count)
print("=======================")
p1 = Pizza("Chicken")
p1.set_toppings_info(25, 1, 4, 0)
p1.display()
print("------------------------------------")
p2 = Pizza("Olives")
p2.set_toppings_info(15, 1.5, 0, 0)
p2.display()
print("------------------------------------")
p3 = Pizza("Sausage")
p3.set_toppings_info(50, 5, 2, 0)
p3.display()
print("=======================")
print("Pizza Count:", Pizza.pizza_count)