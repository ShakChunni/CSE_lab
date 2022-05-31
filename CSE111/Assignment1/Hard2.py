n=int(input("Enter a number: "))
a=0

for i in range(1,n) :
    for j in range(1,n-i+1) :
        print(" ",end="")
    while (a!=(2*i-1)) :
        if (a==0 or a==2*i-2) :
            print("*",end="")
        else:
            print(" ",end="")
        a=a+1
    a=0
    print(""),
for i in range(1,2*n):
    print("*",end="")
print(""),
n=n-1
for i in range (n,0,-1) :
    for j in range(0,n-i+1) :
        print(" ",end="")
    a=0
    while (a!=(2*i-1)) :
        if (a==0 or a==2*i-2) :
            print("*",end="")
        else :
            print(" ",end="")
        a=a+ 1
    print(""),

