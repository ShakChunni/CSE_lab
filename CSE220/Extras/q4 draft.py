class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next

class Stack:
    def __init__(self,head):
        self.head=head

    def insert(self, element):
        newNode = Node(element)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def peek(self):
        return (self.head.element)

    def pop(self):
        if self.head is None:
            return "Stack Underflow!"
        else:
            temp = self.head
            self.head = self.head.next
            temp.element = None
            temp.next = None

    def parenthesis_check(self):
        n = self.head
        while n is not None:
            if n == '[' or n == '{' or n == '(':
                self.push(n)
            elif n == ']' or n == '}' or n == ')':
                if n is None:
                    return "This unbalance"
                else:
                    temp = self.head.pop()
                    if self.checker[temp] != n:
                        return "unbalance 2"
            n = n.next
        if n is None:
            return "Balance"
        elif n is not None:
            return "unbalance dhuke nai"

class Test:
    list = Stack("()()(")
    print(list.parenthesis_check())