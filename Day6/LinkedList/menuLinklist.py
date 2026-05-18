import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addnode(self,data):
        self.node = Node(data)

        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.next = self.node
            self.tail = self.node    

    def addbeg(self,data):
        self.node = Node(data)

        if self.head == None:
            self.head = self.node
            self.tail = self.node
        else:
            self.node.next = self.head
            self.head = self.node    

    def addend(self,data):
        self.node = Node(data)

        if self.head == None:
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.next = self.node
            self.tail = self.node
    
    def display(self):
        while self.head != None:
            print(self.head.data,"->",end=" ")
            self.head = self.head.next


if __name__ == '__main__':

    object = Linkedlist()

    while True:
        print()
        print('1.Add Node Linkedlist')
        print('2.Add Node in Beginning ')
        print('3.Add Node in Between')
        print('4.Add Node in End')
        print('5.Display Linkedlist')
        print('6.Exit')

        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            value = int(input("Enter value for node : "))
            object.addnode(value)
            print("Node added succesfully.")
        elif ch == 2:
            value = int(input("Enter value for node : "))
            object.addbeg(value)  
            print("Node added at begging.") 
        elif ch == 4:
            value = int(input("Enter value for node : "))
            object.addend(value)
            print("Node added succesfully.")
        elif ch == 5:
            object.display()
        elif ch == 6:
            sys.exit()




 