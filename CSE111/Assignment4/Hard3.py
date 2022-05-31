#hard3
import math
n=input("Enter your password: ")
error=[]
if not any(i.isupper() for i in n):
    error.append("Uppercase character missing")
if not any(i.islower() for i in n):
    error.append("Lowercase character missing")
if not any(i.isdigit() for i in n):
    error.append("Digit missing")
if not any((i=="_" or i=="@" or i=="#" or i=="$") for i in n):
    error.append("Special character is missing")
if error:
    print(', '.join(error))
else:
    print("OK")