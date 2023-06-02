# easy1

n1=input("Enter word: ")
def goat(n1):
    c=0
    vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
    for i in n1:
        if i in vowels:
            c = c+1
            n1 = n1.replace(i, "")
    return n1+str(c)

print(goat(n1))