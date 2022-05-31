#hard2

n=input("Enter: ")
def goat(n):
    string1=string2=string_match=""
    for i in range(len(n)//3):
        string1+=n[i]
        string2+=n[-(i+1)]
        if string1==string2[::-1]:
            string_match=string1
    if string_match in n[len(string1):len(n)-len(string1)]:
        palindrome_string=string_match
    else:
        palindrome_string="Not a palindrome substring"
    return(palindrome_string)
print(goat(n))
