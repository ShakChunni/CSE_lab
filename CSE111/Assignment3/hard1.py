#hard1
from collections import Counter

e = ''
f = ''
n1 = input("Enter a word: ")
n2 = input("Enter a word: ")
for i in n2:
    if i in n1:
        e+=i
for j in n1:
    if j in n2:
        f+=j
c= e+f
print(c)

