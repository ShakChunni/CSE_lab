#question1

class Calculator:
    def __init__(self,value1, operator, value2):
        print("Lets Calculate!")
        self.value1=value1
        self.operator=operator
        self.value2=value2
        print("Value 1:",value1)
        print("Operator:",operator)
        print("Value 2:",value2)
        if operator=="+":
            print("Result:",self.add(value1, value2))
        elif operator=="-":
            print("Result:",self.subtract(value1, value2))
        elif operator=="*":
            print("Result:",self.multiply(value1, value2))
        elif operator=="/":
            print("Result:",self.divide(value1, value2))
        else:
            print("Operation not supported")

    def add(self,value1,value2):
        return value1+value2
    def subtract(self,value1,value2):
        return value1-value2
    def multiply(self,value1,value2):
        return value1*value2
    def divide(self,value1,value2):
        try:
            return value1/value2
        except ZeroDivisionError:
            return "Give a non zero value"

value1 = int(input("Enter 1st number\n"))
operator = input("Enter operation to perform (+,-,*,/)\n")
value2 = int(input("Enter 2nd number\n"))
cal = Calculator(value1,operator,value2)