n1=int(input("Enter a number for minimum: "))
n2=int(input("Enter a number for maximum: "))
n3=int(input("Enter a number for divisor: "))

def adds(n1,n2,n3):
    j=0
    count=0
    while(j<n2):
        if(j%n3==0):
            count=count+j
        j+=1
    return count
print(adds(n1,n2,n3))
