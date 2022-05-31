
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

mod1 = num1 % 2
mod2 = num2 % 2
mod3 = num3 % 2
mod4 = num4 % 2
if mod1 == 0:
    if mod2 == 0:
      if mod3 == 0:
          if mod4 == 0:
              print("No odd numbers")


if mod1 > 0:
    if mod2 > 0:
        if mod3 > 0:
            if mod4 > 0:
                print((num1+num2+num3+num4)/4)

if mod1 > 0:
    if mod2 > 0:
        if mod3 > 0:
            if mod4 == 0:
                print((num1+num2+num3)/3)
if mod1 > 0:
    if mod2 > 0:
        if mod3 == 0:
            if mod4 > 0:
                print((num1+num2+num4)/3)
if mod1 > 0:
    if mod2 == 0:
        if mod3 > 0:
            if mod4 > 0:
                print((num1+num3+num4)/3)
if mod1 == 0:
    if mod2 > 0:
        if mod3 > 0:
            if mod4 > 0:
                print((num2+num3+num4)/3)
if mod1 > 0:
    if mod2 > 0:
        if mod3 == 0:
            if mod4 == 0:
                print((num1+num2)/2)
if mod1 > 0:
    if mod2 == 0:
        if mod3 == 0:
            if mod4 > 0:
                print((num1+num4)/2)
if mod1 > 0:
    if mod2 == 0:
        if mod3 > 0:
            if mod4 == 0:
                print((num1+num3)/2)
if mod1 == 0:
    if mod2 > 0:
        if mod3 > 0:
            if mod4 == 0:
                print((num2+num3)/2)
if mod1 == 0:
    if mod2 > 0:
        if mod3 == 0:
            if mod4 > 0:
                print((num2+num4)/2)
if mod1 == 0:
    if mod2 == 0:
        if mod3 > 0:
            if mod4 > 0:
                print((num3+num4)/2)

if mod1 > 0:
    if mod2 == 0:
        if mod3 == 0:
            if mod4 == 0:
                print(num1)
if mod1 == 0:
    if mod2 > 0:
        if mod3 == 0:
            if mod4 == 0:
                print(num2)
if mod1 == 0:
    if mod2 == 0:
        if mod3 == 0:
            if mod4 > 0:
                print(num4)
if mod1 == 0:
    if mod2 == 0:
        if mod3 > 0:
            if mod4 == 0:
                print(num3)



