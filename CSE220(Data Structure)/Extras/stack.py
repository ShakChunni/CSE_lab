class Stack:

    open_list = ['(', '[', '{']
    close_list= [')',']','}']
    def __init__(self,string):
        self.string = string
        self.pointer = -1
        self.stack = []

    def push(self,element):
        self.stack.append(element)
        self.pointer += 1

    def pop(self):
        value=self.stack[self.pointer]
        self.stack=self.stack[:-1]
        self.pointer-=1
        return value

    def compare(self):
        ans=False
        for i in self.string:
            if i == '[' or i == '{' or i == '(':
                self.push(i)
            elif i == ']' or i == '}' or i == ')':
                if len(self.stack)>0:
                    temp = self.stack[len(self.stack)-1]
                    if i == "[" and temp != "]":
                        ans=False
                        self.stack.pop()
                        break
                    if i=="{" and temp!="}":
                        ans=False
                        self.stack.pop()
                        break
                    if i=="(" and temp!=")":
                        ans=False
                        self.stack.pop
                        break


        if len(self.stack)>0:
            ans=False
        if ans:
            print("The expression is Correct!")
        else:
            print("The expression is not Correct! Error at character #" + i + " as " + temp + " did not open/close!")





class Test:
    list=Stack("()")
    print(list.compare())
