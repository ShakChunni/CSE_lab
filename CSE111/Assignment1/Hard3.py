n = int(input("Enter a number: "))
nBinary = bin(n)
nBinary1 = ""
count = 0
for i in nBinary:
    count += 1
for i in range(2,count):
    if nBinary[i] == "1":
        nBinary1 += "1"
ans = int(nBinary1,2)
print(ans)