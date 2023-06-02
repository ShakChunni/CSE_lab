#medium3
count=int()
n=input("Enter a word: ")
for i in range(0, len(n)):
    if (n[i].isupper()):
        count=n.find(n[i])
for i in range(0, count):
    if (n[i].isupper()):
        count1=n.find(n[i])
        if (count==count1+1):
            print("BLANK")
        else:
            z=n[(count1+1):count]
            print(z)