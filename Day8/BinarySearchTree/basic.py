'''why Binary serach tree?
   it perform faster than binary tree when inserting and deleting nodes.'''
# example tree output:
#  preorder -> 70 - 50 - 30 - 20 - 40 - 60 - 90 - 80 - 100
#  Inorder  -> 20 - 30 - 40 - 50 - 60 - 70 - 80 - 90 - 100
#  postorder-> 20 - 40 - 30 - 60 - 50 - 80 - 100 - 90 - 70


import sys
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertNode(self, rootNode , data):
        if rootNode.data == None:
            rootNode.data = data
        elif data < rootNode.data:
            if rootNode.left is None: 
                rootNode.left = BSTNode(data)
            else:
                self.insertNode(rootNode.left,data)    
        else:
            if rootNode.right is None:
                rootNode.right = BSTNode(data)    
            else:
                self.insertNode(rootNode.right,data)    

    def preOrderTraversal(self,rootNode):
        if not rootNode:
            return 
        
        print(rootNode.data,end="->")
        self.preOrderTraversal(rootNode.left)
        self.preOrderTraversal(rootNode.right)

    def InOrderTraversal(self,rootNode):
        if not rootNode:
            return 
        
        self.InOrderTraversal(rootNode.left)
        print(rootNode.data,end="->")
        self.InOrderTraversal(rootNode.right) 

    def postOrderTraversal(self,rootNode):
        if not rootNode:
            return 
        
        self.postOrderTraversal(rootNode.left)
        self.postOrderTraversal(rootNode.right)
        print(rootNode.data,end="->")       

    def search(self,rootNode,target):
            if rootNode.data is None:
                print("Tree is empty.")
            elif target < rootNode.data:
                if rootNode.left is None:
                    print("Node not found.")    
                else:
                    if rootNode.left.data == target:
                        print("Node found.")
                    else:
                        self.search(rootNode.left,target)
            else:
                if rootNode.right is None:
                    print("Node not found.")
                else:
                    if rootNode.right.data == target:
                        print("Node found.")
                    else:
                        self.search(rootNode.right, target)                       

                    
                

objectBst = BSTNode(None)  

while True:
    print()
    print("1. Insert a node.")
    print("2. PreOrder traversal.")
    print("3. InOrder traversal.")
    print("4. PostOrder traversal.")
    print("5. Search a node.")
    print("6. Exit.")

    ch = int(input("Enter your choice : "))

    if ch == 1:
        value=int(input("Enter the value : "))
        objectBst.insertNode(objectBst,value)
    elif ch == 2:
        objectBst.preOrderTraversal(objectBst)  
    elif ch == 3:
        objectBst.InOrderTraversal(objectBst)
    elif ch == 4:
        objectBst.postOrderTraversal(objectBst)
    elif ch == 5:
        value= int(input("Enter the value to be searched : "))
        objectBst.search(objectBst,value)             
    elif ch == 6:
        sys.exit()
    else:
        print("Invalid choice !!!")    
