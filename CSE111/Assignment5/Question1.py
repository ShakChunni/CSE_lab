#question2

class Flower:
    pass
    #def __init__(self,n1,n2,n3):
        #self.name=n1
        #self.color=n2
        #self.num_of_petal=n3
flower1 = Flower();
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print('=====================')
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)


print("Flower 1 address is: ",flower1)
print("Flower 2 address is: ",flower2)
if(flower1==flower2):
    print("they are same")
elif(flower1!=flower2):
    print("they are diffrent")