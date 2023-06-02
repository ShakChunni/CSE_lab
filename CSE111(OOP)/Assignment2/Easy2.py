n2=float(input("Enter your height(cm): "))
n1=float(input("Enter your weight(KG): "))
n3=n2/100
def bmi(n1,n3):
    b = n1/(n3*n3)
    return b
a = bmi(n1,n3)
if a>30:
    print("Score is",a, ".", "You are Obese.")
elif a<=30 and a>=25:
    print("Score is", a, ".", "You are Overweight.")
elif a<=24.9 and a>=18.6:
    print("Score is", a, ".","You are Normal.")
elif a<18.5:
    print("Score is", a,".",  "You are Underweight.")