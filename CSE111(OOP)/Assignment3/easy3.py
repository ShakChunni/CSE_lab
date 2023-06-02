#easy3

def goat(word):
    if len(word)<4:
        processed_word=word
    elif word.endswith("ful"):
        processed_word=word+"ly"
    else:
        processed_word=word+"ful"
    return(processed_word)

word=input("Enter: ")
print(goat(word))