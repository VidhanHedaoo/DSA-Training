
# Two ways to implement stack 
# 1.List/Array
# 2.Linkedlist


# stack implementation without size limit
# import sys

# class Stack:
#     def __init__(self):
#         self.mystack = []

#     def display(self):
#         for i in range((len(self.mystack)-1),-1,-1):
#             print("| ",self.mystack[i]," |")
    
#     def push(self, value):
#         self.mystack.append(value)
#         print("Push succesful")

#     def isEmpty(self):
#         if self.mystack == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty.")
#         else:
#             self.mystack.pop() 
#             print("Element Pop successful.")   

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty.")  
#         else:
#             print("Top element -> ",self.mystack[-1])          
            
#     def stackDelete(self):
#         # self.mystack = None
#         del self.mystack


# obj = Stack()
# print("Stack has created.")

# while(True):
#     print("__Stack Operations__")
#     print("1. Push.")
#     print("2. Pop.")
#     print("3. Display.")
#     print("4. Peek.")
#     print("5. Delete Stack.")
#     print("6. Exit.")

#     choice = int(input("Enter Your Choice : "))

#     if choice == 1:
#         value = int(input("Enter the value to Push : "))
#         obj.push(value)
#     elif choice == 2:
#         obj.pop()
#     elif choice == 3:
#         obj.display()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.stackDelete()
#     elif choice == 6:
#         sys.exit() 
#     else:
#         print("Invalid Choice.")      

# stack implementation with size limit         

import sys

class Stack:
    
    def __init__(self, size):
        self.mystack = []
        self.size = size

    def display(self):
        for i in range((len(self.mystack)-1),-1,-1):
            print("| ",self.mystack[i]," |")

        
    def push(self, value):
        if self.isFull():
            print("Stack is full.") 
        else:
            self.mystack.append(value)
            print("Push succesful")   

    def isFull(self):
        if len(self.mystack) >= self.size:
            return True
        else: 
            return False        

    def isEmpty(self):
        if self.mystack == []:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty.")
        else:
            self.mystack.pop() 
            print("Element Pop successful.")   

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty.")  
        else:
            print("Top element -> ",self.mystack[-1])          
            
    def stackDelete(self):
        # self.mystack = None
        del self.mystack

size = int(input("Enter the size of stack: "))
obj = Stack(size)
print("Stack has created.")

while(True):
    print("__Stack Operations__")
    print("1. Push.")
    print("2. Pop.")
    print("3. Display.")
    print("4. Peek.")
    print("5. Delete Stack.")
    print("6. Exit.")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        value = int(input("Enter the value to Push : "))
        obj.push(value)
    elif choice == 2:
        obj.pop()
    elif choice == 3:
        obj.display()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.stackDelete()
    elif choice == 6:
        sys.exit() 
    else:
        print("Invalid Choice.")     
