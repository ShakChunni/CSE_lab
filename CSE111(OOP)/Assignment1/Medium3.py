sum = 0

n = int(input("Enter a number: "))
for j in range(1,n):
    if(n%j==0):
        sum=sum+j
if sum == n:
    print("Perfect number.")
elif sum != n:
    print("Not perfect.")