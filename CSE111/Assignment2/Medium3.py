import math

def vowel(n1):
    count = 0
    volas = 'Vowels: '
    for i in n1:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u'  or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            volas+=i
            volas+=','
            count+=1
    word = ''
    sum=0
    sum1= len(volas) -2
    while sum<sum1:
        word+=volas[sum]
        sum+=1
    if count==0:
        return "NO vowels!"
    else:
        word+=f'. Total number of vowels: {count}'
        return word
n1=input("Enter something?: ")
a=vowel(n1)
print(a)
