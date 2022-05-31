#1

def selection_sort(array, i, length):
    min_index = i
    for j in range(i+1, length):
        if array[j] < array[min_index]:
            min_index = j
    temporary = array[min_index]
    array[min_index] = array[i]
    array[i] = temporary
    if i+1 < length:
        selection_sort(array, i+1, length)

array=[15,57,-15,177,44,-8874,4,-12,33,34,54,3,2,1]
selection_sort(array, 0, len(array))
print(array)


#2

def insertion_sort(array,length):
    if length > 1:
        insertion_sort(array, length - 1)
        last_element = array[length-1]
        next_element = length-2
        while next_element >= 0 and array[next_element] > last_element:
            array[next_element+1] = array[next_element]
            next_element = next_element - 1
        array[next_element+1] = last_element

array=[15,57,-15,177,44,-8874,4,-12,33,34,54,3,2,1]
length = len(array)
insertion_sort(array,length)
print(array)


#3 & 4

class Node:
    def __init__(self, element, next = None):
        self.element = element
        self.next = next

class Sort:
    def __init__(self, head= None, next = None):
        self.head = head
        self.next = next

    def new_node(self, element = None):
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
                        count = count+1
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


    def display(self):
        current_node = self.head
        if self.head is not None:
            while current_node is not None:
                print(current_node.element, end=", ")
                current_node = current_node.next
        else:
            print("Empty List!")

class Tester:
    list = Sort()
    lst = [14,-5,-115,0,-0,59,-1,12,5,4,548]
    for i in range(0, len(lst)):
        list.new_node(lst[i])

    list.buble_sort()
    print("Bubble sorted list: ")
    list.display()
    print("")
    print("")
    list.selection_sort()
    print("Selection sorted list: ")
    list.display()


#5

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
    lst = [14,8,9,-44,-5,-1456,0,-0,5,4-12,5,2,41,-42,4,44]
    for i in range(0, len(lst)):
        list.insertion_sort(lst[i])
    print("Insertion Sorted List: ")
    list.display()


#6

def binary_search(array, wanted_value,left_most_index, right_most_index):
    if left_most_index <= right_most_index:
        mid_value = (left_most_index + right_most_index) // 2
        if wanted_value == array[mid_value]:
            return mid_value
        elif wanted_value < array[mid_value]:
            return binary_search(array, wanted_value,left_most_index, mid_value-1)
        elif wanted_value > array[mid_value]:
            return binary_search(array, wanted_value, mid_value+1, right_most_index)
        else:
            return "Value not inside the array!"
    else:
        return "Value not inside the array!"
array = [3,6,12,14,15,18,87,120,225,244,445]
wanted_value = 15
print(binary_search(array, wanted_value, 0, len(array)-1))


#7

temporary = {}
def fib(var):
    if var in temporary:
        return temporary[var]
    elif var in range (1,3):
        new_var = 1
    elif var > 2:
        new_var = fib(var - 1) + fib(var - 2)
    else:
        return "Error: Wrong Input!"
    temporary[var] = new_var
    return new_var

for i in range(1,1000):
    print(fib(i))


