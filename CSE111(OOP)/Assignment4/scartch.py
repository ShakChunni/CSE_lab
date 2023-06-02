string=input("Enter string:")
reverse=string[::-1]
string1=""
string12=""
string3=""
for i in range(0,len(string)):
    string1=string1+string[i]
    string12=string12+reverse[i]
    if string1==string12[::-1]:
        string3=string1
        break
length=len(string3)
leng=len(string)
middle=string[length:leng-length]
if string3 in middle:
    print(string3)
else:
    print("Not Palindrome")