from array import *
arr = array('i',[])

a = int(input("Enter the length of the Array: "))
for b in range(a):
    c = int(input("Enter a value: "))
    arr.append(c)
brr = array(arr.typecode, (e*e for e in arr))
brr.reverse()
for d in brr:
    print(d)