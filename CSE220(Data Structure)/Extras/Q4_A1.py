class Stack:
    checker = {'(':')', '{':'}', '[':']'}
    def __init__(self,string):
        self.string = string
        self.pointer = -1
        self.stack = []
    def push(self,element):
        self.stack.append(element)
        self.pointer += 1
    def pop(self):
        if len(self.stack)==0:
            return "Stack Underflow!"
        else:
            value=self.stack[self.pointer]
            self.stack=self.stack[:-1]
            self.pointer-=1
            return value

    def parenthesis_check(self):
        if len(self.string)==0:
            return "Stack Underflow!"
        else:
            x = 0
            while x<len(self.string):
                for i in self.string:
                    x+=1
                    if i=='[' or i=='{' or i=='(':
                        self.push(i)
                    elif i==']' or i=='}' or i==')':
                        if len(self.stack)==0:
                            return "The expression is NOT correct.\nError at character # " + str(x) + ".'" + i + "'-not opened."
                        else:
                            temp=self.stack.pop()
                            if self.checker[temp]!=i:
                                return "The expression is NOT correct.\nError at character # " + str(self.string.index(temp)+1) +".'" + temp + "'-not closed."
                if len(self.stack) == 0:
                    return "The expression is correct!"
                elif len(self.stack) != 0:
                    return "The expression is not Correct!\nError at character # " + str(self.string.index(temp)+1) + " '" + temp +"'-not closed"

class Test:
    array=Stack("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
    print(array.parenthesis_check())









