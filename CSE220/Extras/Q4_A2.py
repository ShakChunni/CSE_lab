class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class Stack:
    head=None
    checker = {'(': ')', '{': '}', '[': ']'}
    def __init__(self,string):
        self.string=string
        self.head=Node(None)

    def push(self, element):
        if self.head is None:
            self.head = Node(element)
        else:
            n = Node(element)
            n.next = self.head
            self.head = n
    def peek(self):
        return self.head.element
    def pop(self):
            temp = self.head
            self.head = self.head.next
            temp.element = None
            temp.next = None
            return self.head.element
    def __len__(self):
        n=self.head
        count=0
        while n.next is not None:
            count+=1
        return count


    def parenthesis_check(self):
        if self.head is not None:
            i=self.head
            for i in self.string:
                if i=='[' or i=='{' or i=='(':
                    self.push(i)
                elif i==']' or i=='}' or i==')':
                    if len(i) == 0:
                        return "The expression is NOT correct"
                    else:
                        temp = self.pop()
                        if self.checker[temp] != i:
                            return "The expression is NOT correct.\nError at character # " + str(self.string.index(temp)+1) +".'" + temp + "'-not closed."
            if len(i) == 0:
                return "The expression is correct!"
            elif len(i) != 0:
                return "The expression is not Correct!\nError at character # " + str(self.string.index(temp)+1) + " '" + temp +"'-not closed"


class Test:
    var=Stack("())")
    print(var.parenthesis_check())











