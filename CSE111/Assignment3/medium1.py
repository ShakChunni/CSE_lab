#medium1

n1=input("Enter word: ")
def goat(n1):
    upp=0
    low=0
    for i in n1:
        if i.isupper():
            upp+=1
        elif i.islower():
            low+=1
    if upp>low:
        n1=n1.upper()
    elif upp<=low:
        n1=n1.lower()
    return n1
print(goat(n1))