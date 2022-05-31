class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Allocates a new node with given data
def newNode(data):
    new_node = Node(data)
    new_node.data = data
    new_node.next = None
    return new_node


# Function to insert a new node at the
# end of linked list using recursion.
def insertEnd(head, data):
    # If linked list is empty, create a
    # new node (Assuming newNode() allocates
    # a new node with given data)
    if head is None:
        return newNode(data)

    # If we have not reached end,
    # keep traversing recursively.
    else:
        head.next = insertEnd(head.next, data)
    return head


def traverse(head):
    if head is None:
        return

    # If head is not None, print current node
    # and recur for remaining list

    print(head.data, end=" ");
    traverse(head.next)


# Driver code
if __name__ == '__main__':
    head = None
    head = insertEnd(head, "Hi")
    head = insertEnd(head, "Hi")
    head = insertEnd(head, "Hi")
    head = insertEnd(head, "Hi")
    head = insertEnd(head, "Hi")
    head = insertEnd(head, "Hi")
    traverse(head)