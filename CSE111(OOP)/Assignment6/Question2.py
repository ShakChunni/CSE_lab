#question2

class Customer:
    def __init__(self,name):
        self.name=name
        
    def greet(self,name=None):
        if name==None:
            print("Hello!")
        else:
            print("Hello",name,"!")
    def purchase(self,*product):
            print(self.name,"You purchased",len(product),"items:")
            for i in product:
                print(i)
                


customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")