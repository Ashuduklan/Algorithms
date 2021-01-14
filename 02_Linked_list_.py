#do it by your own this is the link list both insertion operations
# singly linked list operations are as follows
# linked list : insertion deletion and traversal
# traversal
# create a node
class Node:
    def __init__(self, data):   # this is a single node which contain data and reference
        self.data = data
        self.ref = None
# now create a empty linked list
class linkedlist:
    def __init__(self):
        self.head = None

# this is the traversal of a linked list
    def printll(self):
        if self.head is None:
            print("Linked list is empty")
            return "mjaa ma"
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref
        return "Ashish"
# insert element at the beginning of the linked list
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

# insert element at the end of the linked list
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref:
                n = n.ref
            n.ref = new_node
# insert element between the nodes
    # 1. after a node
    # 2. before a node

    def after_node(self, data, x):
        n = self.head
        while n.ref is not None:
           if x == n.data:
               break
           n  = n.ref
        if n.ref is None:
            print("Your x value is not in the linked list")
        else:
            newNode = Node(data)
            newNode.ref = n.ref
            n.ref = newNode

# -------------------Start deletion operation and it's sub operations---------------------------------------------------
# if we want to delete node from a linked list:
# delete from the beginning of the linked list
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty.. you cant delete anything!!!")
        else:
            self.head =self.head.ref

# delete item from the end of the linked list
    def delete_end(self):
        if self.head is None:
            print("Oops the linked list is empty!!!")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

# delete any node from the linked list
    def DeleteNode(self, a):
        if self.head is None:
            print("Oops linked list is empty!! you can not delete the not!!")
        else:
            if a == self.head:
                self.head = self.head.ref
            else:
                n =self.head
                while n.ref is not None:
                    if a==n.ref.data:
                        break
                    else:
                        n =n.ref
                if n.ref is None:
                    print("Node is not present..")
                else:
                    n.ref = n.ref.ref


l = linkedlist()
l.add_end(12)
l.add_end(13)
l.add_end(45)
l.add_begin(87)
l.add_begin(66)
delete = int(input("Which node you want to delete"))
l.DeleteNode(delete)
print(l.printll())