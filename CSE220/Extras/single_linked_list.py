class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next


class Sort:
    def __init__(self, head=None, next=None):
        self.head = head
        self.next = next

    def new_node(self, element=None):
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def buble_sort(self):
        current_node = self.head
        count = 0
        if self.head is not None:
            while current_node is not None:
                count = 0
                temporary = self.head
                while temporary.next is not None:
                    if temporary.element > temporary.next.element:
                        count = count + 1
                        temp_store = temporary.element
                        temporary.element = temporary.next.element
                        temporary.next.element = temp_store
                        temporary = temporary.next
                    else:
                        temporary = temporary.next
                if count != 0:
                    continue
                elif count == 0:
                    break

    def selection_sort(self):
        current_node = self.head
        if self.head is not None:
            while current_node is not None:
                minimum = current_node
                next_node = current_node.next
                while next_node is not None:
                    if minimum.element > next_node.element:
                        minimum = next_node
                    next_node = next_node.next
                temporary = current_node.element
                current_node.element = minimum.element
                minimum.element = temporary
                current_node = current_node.next
        else:
            return "No value entered!"

    def concate(self):
        current_node = self.head
        next_node = current_node.next
        if self.head is None:
            return
        else:
            print(str(self.head)+str(self.head), end=" ")
        current_node = current_node.next

    def display(self):
        current_node = self.head
        next_node = self.head.next
        if self.head is not None:
            while current_node is not None:
                print(current_node.element + str(next_node.element), end=" ")
                current_node = current_node.next
        else:
            print("Empty List!")


class Tester:
    list = Sort()
    lst = ["Hi", "This", "is", "Leo"]
    for i in range(0, len(lst)):
        list.new_node(lst[i])

    list.concate()
    print("Bubble sorted list: ")
    list.display()
   # print("")
   # print("")
  #  list.selection_sort()
    print("Selection sorted list: ")
    list.display()
