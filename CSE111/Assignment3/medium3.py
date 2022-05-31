#medium3

def slice_capital(word):
    for i in range(len(word)):
        if word[i].isupper():
            first_capital_index=i
            break
    for i in range(len(word)-1,-1,-1):
        if word[i].isupper():
            second_capital_index=i
            break
    if first_capital_index+1==second_capital_index:
        processed_word="BLANK"
    else:
        processed_word=word[first_capital_index+1:second_capital_index]
    return (processed_word)

print(slice_capital(input("Enter a string\n")))