   
# Queue implementation with size limit         

import sys

class Queue:
    
    def __init__(self, size):
        self.myQueue = []
        self.size = size

    def display(self):
        print("|",end="")
        for i in range(0,len(self.myQueue)):
        
            print(self.myQueue[i],end=" | ")
        print("")    
            

        
    def enqueue(self, value):
        if self.isFull():
            print("Queue is full.") 
        else:
            self.myQueue.append(value)
            print("Element Enqueued.")   

    def isFull(self):
        if len(self.myQueue) >= self.size:
            return True
        else: 
            return False        

    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False
        
    def delete(self):
        if self.isEmpty():
            print("Queue is Empty.")
        else:

            del self.myQueue[0]
            print("Element deleted successful.")   

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty.")  
        else:
            print("First element -> ",self.myQueue[0])          
            
    def stackDelete(self):
        # self.myQueue = None
        del self.myQueue
        print("Queue deleted Succesfully.")
        sys.exit()


size = int(input("Enter the size of Queue: "))

obj = Queue(size)
print("Queue has created.")

while(True):
    print("")
    print("__Queue Operations__")
    print("1. Enqueue.")
    print("2. Delete.")
    print("3. Display.")
    print("4. Peek.")
    print("5. Delete Queue.")
    print("6. Exit.")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        value = int(input("Enter the value to enqueue : "))
        obj.enqueue(value)
    elif choice == 2:
        obj.delete()
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
