import math
s=[]
n1=input("Enter: ")
n2=''
n3=''
for i in n1:
    if i == ' ':
        pass
    else:
        s.append(i)
        n2 += i
while len(s) != 0:
    n3 += s.pop()
if n2 == n3:
    print('Palindrome.')

else:
    print('Not a palindrome.')