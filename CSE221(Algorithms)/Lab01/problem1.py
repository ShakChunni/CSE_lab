import sys

def numbers(var):
    if var % 2 == 0:
        return("has even parity")
    elif var % 2 != 0:
        return("has odd parity")


def string(word):
    length = len(word)
    if length == 0:
        return("is not a palindrome")
    else:
        half_length = int(length/2)
        for i in range(0, half_length):
            if word[i] != word[length - 1 - i]:
                return("is not a palindrome")
            i += 1
        return("is a palindrome")


def palindrome_count(wordx):
    n = wordx[::-1]
    if wordx == n:
        return True
    else:
        return False

        

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
t = 0
try:
    while t < 12:
        input_val = sys.stdin.readline().rstrip()
        num_part, string_part = input_val.split(" ")
        num_part = float(num_part)
        if num_part.is_integer():
            print(int(num_part), numbers(int(num_part)), "and", string_part, string(string_part))
        else:
            print(num_part, "cannot have parity", "and", string_part, string(string_part))
        
except:
    pass
sys.stdout.close()
sys.stdin.close()

sys.stdin = open('input.txt', 'r')
sys.stdout = open('record.txt', 'w')
x = 0
odd_count, even_count, no_parity_count, pal_count, non_pal_count, total_num , total_word = [0]*7
try:
    while x < 12:
        input_x = sys.stdin.readline().rstrip()
        numx, wordx = input_x.split(" ")
        numx = float(numx)
        if numx.is_integer():
            if numx % 2 != 0:
                odd_count += 1
            elif numx % 2 == 0:
                even_count += 1
        else:
            no_parity_count += 1
        if palindrome_count(wordx):
            pal_count += 1
        elif palindrome_count(wordx) is False:
            non_pal_count += 1
        total_num = odd_count + even_count + no_parity_count
        total_word = pal_count + non_pal_count
        odd_chance = (odd_count/total_num)*100
        even_chance = (even_count/total_num)*100
        no_parity_chance = (no_parity_count/total_num)*100
        palindrome_chance = (pal_count/total_word)*100
        non_palindrome_chance = (non_pal_count/total_word)*100
except:
    pass

print("Percentage of odd parity:", odd_chance,"%")
print("Percentage of even parity:", even_chance,"%")
print("Percentage of no parity:", no_parity_chance,"%")
print("Percentage of palindrome:", palindrome_chance,"%")
print("Percentage of non-palindrome:", non_palindrome_chance,"%")

