import sys

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode =  self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()   

    def __str__(self):
        values = [str(x.data) for x in self.LinkedList]
        return '\n'.join(values)      

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
        
    def push(self,data):
        node = Node(data)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty."
        else:    
            temp = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.next
            return temp
    



mystack = Stack()  
mystack.push(34)  
mystack.push(54)
mystack.push(64)
  
print(mystack)  
print(mystack.pop())