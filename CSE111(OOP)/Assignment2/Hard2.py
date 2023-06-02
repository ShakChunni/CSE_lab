import math
n1=int(input("Enter a number: "))
def goat(days):
     years=int(days / 365)
     months=int((days % 365) / 30)
     days=int((days % 365) % 30)
     return f'{years} years, {months} months and {days} days'
total=(n1)
a=goat(total)
print(a)