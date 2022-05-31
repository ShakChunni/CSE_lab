#meidum2

n1=input("Enter: ")
def g(n1):
    c1=0
    c2=0
    for i in n1:
        if i.isdigit():
            c1+=1
        elif i.isalpha():
            c2+=1
    if c1==0 and c2>c1:
        n1="WORD"
    elif c2==0 and c1>c2:
        n1="NUMBER"
    elif c2!=0 and c1!=0:
        n1="MIXED"
    return n1
print(g(n1))