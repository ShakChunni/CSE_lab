num1 = float(input("Enter a number: "))
op1 = input("Enter an operator: ")
num2 = float(input("Enter another number: "))
op2 = input("Enter an operator: ")
num3 = float(input("Enter another number: "))

if op1== "+" and op2== "+":
    print(num1 + num2 + num3)
elif op1== "+" and op2== "-":
    print(num1 + num2 - num3)
elif op1 == "+" and op2 == "/":
    print(num1 + num2 / num3)
elif op1 == "-" and op2 == "-":
    print(num1 - num2 - num3)
elif op1 == "-" and op2 == "/":
    print(num1 - num2 / num3)
elif op1 == "-" and op2 == "*":
    print(num1 - num2 * num3)
elif op1 == "*" and op2 == "+":
    print(num1 * num2 + num3)
elif op1 == "*" and op2 == "-":
    print(num1 * num2 - num3)
elif op1 == "*" and op2 == "*":
    print(num1 * num2 * num3)
elif op1 == "*" and op2 == "/":
    print(num1 * num2 / num3)
elif op1 == "/" and op2 == "+":
    print(num1 / num2 + num3)
elif op1 == "/" and op2 == "-":
    print(num1 / num2 - num3)
elif op1 == "/" and op2 == "*":
    print(num1 / num2 * num3)
elif op1 == "/" and op2 == "/":
    print(num1 / num2 / num3)
else:
    print("Invalid Operator")
