import fractions
n1=float(input("Enter a number: "))
n2=float(input("Enter another number: "))
def fraction(n1,n2):
    a = n1/n2
    b = a%2
    return b
print(fraction(n1,n2))