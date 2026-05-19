# Tree and graph are non linear data structure. It's elements have heiarchical relationship betw them 
# Used in file syste

'''how to implwmwnt a tree?
   there are two ways linkedlist and list/array ....'''

class Tree:
    def __init__(self, data):
        self.data = data
        self.child = []

    def addChild(self, object):
        self.child.append(object)    
        

    def __str__(self,level = 0): #buildin fucntion that is called automatically when object is called
        ret = "  "* level + str(self.data) + "\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret    
            



# rootNode     = Tree("Drinks")    
# Hot          = Tree("Hot")
# Cold         = Tree("Cold")
# Tea          = Tree("Tea")
# Coffee       = Tree("Coffee")
# NonAlcoholic = Tree("Non Alcoholic")
# Alcoholic    = Tree("Alcoholic") 

# rootNode.addChild(Hot)
# rootNode.addChild(Cold)
# Hot.addChild(Tea)
# Hot.addChild(Coffee)
# Cold.addChild(NonAlcoholic)
# Cold.addChild(Alcoholic)

# print(rootNode)


N1 = Tree("N1")
N2 = Tree("N2")
N3 = Tree("N3")
N4 = Tree("N4")
N5 = Tree("N5")
N6 = Tree("N6")
N7 = Tree("N7")
N8 = Tree("N8")
N0 = Tree("")

N1.addChild(N2)

N1.addChild(N3)
N2.addChild(N4)
N2.addChild(N5)
N3.addChild(N0)
N3.addChild(N6)
N4.addChild(N7)
N4.addChild(N8)

print(N1)

