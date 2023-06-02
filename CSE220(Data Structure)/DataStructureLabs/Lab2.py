class Node:
    def __init__(self, element, next):
        self.value = element
        self.next = next
# Task_02-1_a


class MyList:
    def __init__(self, var=None):
        if (var == None):
            self.head = None
            self.sum = 0
# Task_02-1_b
        elif isinstance(var, list):
            if (len(var) == 0):
                print("Array cannot be Empty!")
                return
            self.head = None
            self.sum = len(var)
            self.tail = None
            for i in range(0, len(var)):
                newNode = Node(var[i], None)
                if (self.head is None):
                    self.head = newNode
                    self.tail = newNode
                elif (self.head is not None):
                    self.tail.next = newNode
                    self.tail = newNode
# Task_02-1_c
        elif isinstance(var, MyList):
            if (var.head == None):
                print("List cannot be empty!")
                return
            self.head = None
            self.sum = 0
            self.tail = None
            var1 = var.head
            while var1 is not None:
                newNode = Node(var1.value, None)
                if self.head is None:
                    self.head = newNode
                    self.tail = newNode
                elif self.head is not None:
                    self.tail.next = newNode
                    self.tail = newNode
                var1 = var1.next
                self.sum += 1
        else:
            print("Wrong datatype passed in the constructor so creating an empty MyList!")

# Task_02-2
    def showList(self):
        var1 = self.head
        if (var1 == None):
            print("The list is Empty!")
        elif (var1 != None):
            var1 = self.head
            while var1 is not None:
                print(var1.value, end="->")
                var1 = var1.next
            print()
# Task_02-3

    def isEmpty(self):
        if (self.head == None):
            return True
        elif (self.head != None):
            return False
# Task_02-4

    def clear(self):
        if (self.head == None):
            print("The list is emptry!")
        elif (self.head != None):
            self.head = None
            print("The list has been Cleared!")
# Task_2-5
   # def insert(self,newElement):
        # if(self.head==None):
            # print("The list is Empty!")
        # elif(self.head!=None):
            # newNode=Node(newElement, None)
            # var2=self.head

            # while var2 is not None:

            # if(var2.value==newElement):
            # print("The key alreay exists!")
            # return
            # if(var2.next == None):
            # break
            # var2=var2.next
            # var2.next=newNode
            # self.sum+=1
# Task_2-5 and 6
    def insert(self, newElement, index=None):  # 2 tay same e st bhai bollo
        if (index != None):
            if (self.head == None):
                print("The list is Empty!")
            elif (self.head != None):
                if (index < 0 or index > self.sum):
                    print("The enterd index is invalid!")
                newNode = Node(newElement, None)
                var2 = self.head
                while var2 is not None:
                    if (var2.value == newElement):
                        print("The key already exsists in the list!")
                        return
                    var2 = var2.next
                if (index == 0):
                    newNode.next = self.head
                    self.head = newNode
                elif (index != 0):
                    var2 = self.head
                    for i in range(0, index-1):
                        var2 = var2.next
                    newNode.next = var2.next
                    var2.next = newNode
        else:
            if (self.head == None):
                print("The list is Empty!")
            elif (self.head != None):
                newNode = Node(newElement, None)
                var2 = self.head
                while var2 is not None:
                    if (var2.value == newElement):
                        print("The key alreay exists!")
                        return
                    if (var2.next == None):
                        break
                    var2 = var2.next
                var2.next = newNode
                self.sum += 1
# Task_02-7
    # Pari ni :(
# Task_03-1

    def evenNumber(self):
        var2 = self.head
        head1 = None
        tail1 = None
        while var2 is not None:
            if (var2.value % 2 == 0):
                newNode = Node(var2.value, None)
                if (head1 == None):
                    head1 = newNode
                    tail1 = newNode
                else:
                    tail1.next = newNode
                    tail1 = newNode
            var2 = var2.next
        var2 = head1
        while var2 is not None:
            print(var2.value, end="->")
            var2 = var2.next
# Taske_03-2

    def elementCheck(self, var3, element):
        var2 = var3.head
        n = 0
        while var2 is not None:
            if (var2.value == element):
                var2 = 1
                return True
            var2 = var2.next
        if n == 0:
            return False
# Task_03-3

    def reverse(self, var3):
        head1 = None
        var2 = var3.head
        while (var2 is not None):
            nextNode = var2.next
            var2.next = head1
            head1 = var2
            var2 = nextNode
        self.head = head1

# Task_03-4
    def sort(self):
        var2 = self.head
        while var2.next != None:
            var3 = var2.next
            while var3 != None:
                if (var2.value > var3.value):
                    temporary = var3.value
                    var3.value = var2.value
                    var2.value = temporary
                var3 = var3.next
            var2 = var2.next
# Task_03-5

    def sumation(self, n):
        var2 = n.head
        sum = 0
        while var2 is not None:
            sum = sum+var2.value
            var2 = var2.next
        return sum
# Task_03-6

    def rotation(self, side, place):
        var2 = 1
        if (side == "right"):
            while var2 <= place:
                tail = self.head
                while tail.next.next != None:
                    tail = tail.next
                temporaryHead1 = tail.next
                tail.next = None
                temporaryHead1.next = self.head
                self.head = temporaryHead1
                var2 = var2+1
        if (side == "left"):
            while var2 <= place:
                temporaryHead = self.head
                self.head = self.head.next
                tail = self.head
                while (tail.next != None):
                    tail = tail.next
                tail.next = temporaryHead
                temporaryHead.next = None
                var2 = var2+1


class Tester:
    myList = MyList()
    list = MyList([3, 2, 5, 6, 1, 8])
    list1 = MyList(list)
    # list1.showList()                           #Use this to see list1
    # print(list1.isEmpty())                 #first list  er jonne to see if the list is empty or not
    # list.clear()                               #Use this to clear the list if there is values
    # list1.showList()
    # myList.evenNumber()                           #Use this to print even numbers
    # print(list1.elementCheck(list1,6))             #Use this to check an element(First one is the list and second is the element)
    # print(list1.sumation(list1))           #Use this to find the sumation of the elements in list
    # list1.insert(6,4)                      #USE This for inserting at given index
    # list1.insert(147)                     #USE ThIS if you want to insert{NUMBER 5}
    # list1.reverse(list1)                            #Use this to reverse list
    # list1.sort()                                      #Use this  to sort(Sorting from small to big)
    # list1.rotation("left",3)               #Use this to rotate(first one is side and second is place you want to rotate)
    # list1.showList()                        #Use this to show the list when reversing or rotating as they dont print
