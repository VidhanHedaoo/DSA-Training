class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

linkedlist = Linkedlist()

linkedlist.head = Node(5)
second = Node(10)
third = Node(15)
fourth = Node(20)

#connecting nodes
linkedlist.head.next = second
second.next = third
third.next = fourth

#display linkedlist 
while linkedlist.head != None:
    print(linkedlist.head.data,"->",end=" ")
    linkedlist.head = linkedlist.head.next

# 5 -> 10 -> 15 -> 20 -> 


