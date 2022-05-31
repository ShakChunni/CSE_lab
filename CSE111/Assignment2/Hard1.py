def goat(string):
    word=''
    word1=''
    count=0
    for i in string:
        if count == 0:
            word1 = i.upper()
            word += word1
            count += 1
        elif i == 'i' and string[count + 1] == ' ':
            word1 = i.upper()
            word += word1
            count += 1
        elif string[count - 1]=='!' or string[count - 1]=='.' or string[count - 1]=='?':
            word1=i.upper()
            word+=word1
            count+=1
        else:
            word += i
            count += 1
        word1 = ''
    return word
n1=input("Enter: ")
a=goat(n1)
print(a)