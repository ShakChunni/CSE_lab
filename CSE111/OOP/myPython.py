from array import *
values = array('d', [17,98,88,58,454])
newArr = array(values.typecode, (e*e*e for e in values))

for a in newArr:
    print(a)