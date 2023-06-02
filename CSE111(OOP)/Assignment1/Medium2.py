n = int(input("Enter a number: "))

count = 0
while(n>0):
   count1 = n%10
   count = count*10 + count1
   n = n // 10
print("The reverse of the given number is:",count )
