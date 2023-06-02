def goat(BBQChickenCheeseBurger=250, BeefBurger=170, NagaDrums=200):
    n1 = input("The food you want: ")
    n2 = input("You live in: ")
    x=0
    if n1=="BBQ Chicken Cheese Burger" and n2=="":
        x=250+40+20
    elif n1=="BBQ Chicken Cheese Burger" and n2=="Mohakhali":
        x=250+40+20
    elif n1=="BBQ Chicken Cheese Burger" and n2!="Mohakhali":
        x=250+60+20
    elif n1=="Beef Burger" and n2=="":
        x=170+40+13.6
    elif n1=="Beef Burger" and n2=="Mohakhali":
        x=170+13.6+40
    elif n1=="Beef Burger" and n2!="Mohakhali":
        x=170+13.6+60
    elif n1=="Naga Drums" and n2=="":
        x=200+16+40
    elif n1=="Naga Drums" and n2=="Mohakhali":
        x=200+16+40
    elif n1=="Naga Drums" and n2!="Mohakhali":
        x=200+60+16
    return x
print(goat(BBQChickenCheeseBurger=250, BeefBurger=170, NagaDrums=200))
