n = int(input("Enter a number: "))
n1 = 0
n2 = 1
c = 0
while c<n:
    print(n1)
    sum = n1 + n2
    n1 = n2
    n2 = sum
    c += 1