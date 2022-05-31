from array import *
arr = array('i', [])
a = int(input("Enter the length of the array: "))
for b in range(a):
    c = int(input("Enter a value: "))
    arr.append(c)
val = int(input("Enter the index number for search: "))
e = 0
for d in arr:
    if d == val:
        print(e)
    else:
        print("Not found.")
        break
    e+=1
