n = input("Enter a number:")
n1 = int(n)
count=0
digit=0

while n1>1:
     n1/=10
     count+=1

for i in range(9):
    for j in range(count-1):
        if i==int(n[j]):
            digit+=1
            break
print(digit)