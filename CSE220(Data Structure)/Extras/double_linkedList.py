class Node:
    def __init__(self, element, next=None, previous=None):
        self.element = element
        self.next = next
        self.previous = previous

class Sort:
    def __init__(self, head=None, next=None, previous=None):
        self.head = head
        self.next = next
        self.previous = previous

    def new_node(self, element=None):  # No need for this one as insertion sort means when inserting we compare the values and sort it
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    def insertion_sort(self, element=None):
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
        elif self.head.element >= newNode.element:
            newNode.next = self.head
            newNode.next.previous = newNode
            self.head = newNode
        elif self.head.element < newNode.element:
            current_node = self.head
            while current_node.next is not None and current_node.next.element < newNode.element:
                current_node = current_node.next
            newNode.next = current_node.next
            if current_node.next is not None:
                newNode.next.previous = newNode
            current_node.next = newNode
            newNode.previous = current_node
        else:
            return "No Value Entered!"


    def display(self):
        current_node = self.head
        if self.head is not None:
            while current_node is not None:
                print(current_node.element, end= ", ")
                current_node = current_node.next
        else:
            print("Empty List!")


class Tester:
    list = Sort()
    lst = [14, 8, 9, -44, -5, -1456, 0, -0, 5, 4, -12, 5, 2, 41, -42, 4, 44]
    for i in range(0, len(lst)):
        list.insertion_sort(lst[i])
    print("Insertion Sorted List: ")
    list.display()